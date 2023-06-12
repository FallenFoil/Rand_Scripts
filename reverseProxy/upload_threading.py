#!/usr/bin/env python

from os import listdir
from os.path import isfile, isdir
from google.cloud import storage

import threading
import sys
import signal


class textColors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class myThread(threading.Thread):
    def __init__(self, name, files, bucket_name):
        threading.Thread.__init__(self)
        self.files = files
        self.name = name
        self.bucket_name = bucket_name
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        i = 1
        for file in self.files:
            if self.stopped():
                print(
                    f'{textColors.ORANGE}{self.name} ({i}):{textColors.END} Stopping!!')
                break
            upload_blob(thread_name=self.name, 
                        iteration=f'{i}/{len(self.files)}',
                        source_file_name=file, 
                        destination_blob_name=file, 
                        bucket_name=self.bucket_name,)
            i += 1
        self.stop()


def upload_blob(thread_name, iteration, source_file_name, destination_blob_name, bucket_name):
    try:
        blob = bucket.blob(destination_blob_name)

        generation_match_precondition = 0

        if not blob.exists(storage_client):
            blob.upload_from_filename(
                source_file_name, if_generation_match=generation_match_precondition)
            print(f'{textColors.GREEN}{thread_name} ({iteration}):{textColors.END} File {textColors.UNDERLINE}{source_file_name}{textColors.END} uploaded to {textColors.UNDERLINE}{bucket_name}/{destination_blob_name}{textColors.END}')
        else:
            print(f'{textColors.BLUE}{thread_name} ({iteration}){textColors.END}')
    except:
        print(f'{textColors.RED}ERROR::{thread_name} ({iteration}): File{textColors.UNDERLINE}{source_file_name}{textColors.END} not uploaded{textColors.END}')


def find_files(folder_path, file_list):
    for item in listdir(folder_path):
        item_path = f'{folder_path}/{item}'
        if isdir(item_path):
            find_files(item_path, file_list)
        elif isfile(item_path):
            file_list.append(item_path)


def split_list(all_files, n):
    size = len(all_files)
    chunk_size = size // n
    split_return = []

    for i in range(n):
        if i == n-1:
            split_return.append(all_files[i*chunk_size:])
        else:
            split_return.append(all_files[i*chunk_size:(i+1)*chunk_size])

    return split_return


def all_threads_stopped(threads):
    all_stopped = True

    for thread in threads:
        if not thread.stopped():
            all_stopped = False
            break

    return all_stopped


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f'{textColors.BLUE}Usage:{textColors.END}')
        print(f'{textColors.BLUE}  python upload_pdfs_2_cloud_storage.py <bucket-name> <folder-to-send>{textColors.END}')
        exit()

    path = sys.argv[2]
    num_threads = 4
    all_files = []
    threads: myThread = []

    try:
        storage_client = storage.Client()
        bucket_name = sys.argv[1]
        bucket = storage_client.bucket(bucket_name)

        if not bucket.exists():
            raise Exception('Bucket doesn\'t exists')

        print(f'{textColors.GREEN}Bucket {bucket_name} found{textColors.END}')
        print(f'{textColors.GREEN}Using path={path}{textColors.END}')

        find_files(path, all_files)
        files = split_list(all_files, num_threads)

        print(f'{textColors.GREEN}all_files: {len(all_files)}{textColors.END}')

        for i in range(1, num_threads + 1):
            print(
                f'{textColors.GREEN}files{i}: {len(files[i-1])}{textColors.END}')
            thread = myThread(f'Thread {i}', files[i-1], bucket_name)
            threads.append(thread)

        def signal_handler(sig, frame):
            print('==========================================')
            for thread in threads:
                thread.stop()

        signal.signal(signal.SIGINT, signal_handler)

        for thread in threads:
            thread.start()

        while (not all_threads_stopped(threads)):
            pass
    except Exception as e:
        print(e)
