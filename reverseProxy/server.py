import configparser
import os
import sys

from http.server import HTTPServer, SimpleHTTPRequestHandler
from google.cloud import storage
from google.api_core.exceptions import NotFound
from datetime import datetime, timezone

# DEV ONLY!!
import requests

class ProxyException(Exception):
    def __init__(self, httpCode, message="Found the following HTTP code: "):
        self.httpCode = httpCode
        self.message = message
        super().__init__(self.message + httpCode)

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/pdf'):
            query = self.path.split('?')
            try:
                if len(query) > 1:    
                    urlParams = self.__getUrlParams(query[1])
                    if 'name' in urlParams and 'lang' in urlParams:
                        # DEV ONLY!!
                        if len(sys.argv) > 1 and sys.argv[1] == 'dev':
                            # Use HTTP server to get the PDF
                            self.__TEST_getPdfFromHttpServer(urlParams['lang'], urlParams['name'])
                            return

                        # Google Cloud Storage
                        pdf = self.__getPdfFromBucket(urlParams['lang'], urlParams['name'])

                        self.send_response(200)
                        self.send_header('Content-type', 'application/pdf')
                        self.send_header('Content-Length', len(pdf))
                        self.send_header('Date', datetime.now(timezone.utc))
                        self.end_headers()

                        self.wfile.write(pdf)
                    else:
                        raise ProxyException(400)
                else:
                    raise ProxyException(400)
            except NotFound:
                self.send_response(404)
                print(f'\nFile not found\n')
                sys.stdout.flush()
            except ProxyException as e:
                self.send_response(e.httpCode)
                print(f'\n{e.message}{e.httpCode}\n')
                sys.stdout.flush()
            except Exception as e:
                print(f'\n{e}\n')
                sys.stdout.flush()
                self.send_response(500)
        else:
            super(CustomHTTPRequestHandler, self).do_GET()
    
    def __getUrlParams(self, query):
        urlParams = dict()
        parts = query.split('&')
        for keyValue in parts:
            keyValueArr = keyValue.split('=')
            urlParams[keyValueArr[0]] = keyValueArr[1]
        return urlParams
    
    def __TEST_getPdfFromHttpServer(self, lang, fileName):
        response = requests.get('http://localhost:3000/' + lang + '/' + fileName + '.pdf')
                        
        if not (response.status_code >= 200 and response.status_code <= 299):
            raise ProxyException(response.status_code)

        self.send_response(response.status_code)

        self.send_header('Content-type', 'application/pdf')
        for header in response.headers:
            self.send_header(header, response.headers[header])
        self.end_headers()

        self.wfile.write(response.content)
    
    def __getPdfFromBucket(self, lang, fileName):
        # step 1: import files (settings and service account)
        gcpsettings = configparser.RawConfigParser()
        gcpsettings.read('env.yml')

        # step 2: create storage_client
        storage_client = storage.Client()

        # step 3: fetch bucket
        bucket = storage_client.get_bucket(
            gcpsettings.get('gcp-' + os.environ['ENV'], 'bucket-name'))

        # step 4: fetch blob
        blob = bucket.blob(gcpsettings.get('gcp-' + os.environ['ENV'], 'bucket-path') + f'/{lang}/{fileName}.pdf')

        # step 5: download and return file
        return blob.download_as_bytes()


def main():
    PORT = 8080
    Handler = CustomHTTPRequestHandler

    with HTTPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    main()