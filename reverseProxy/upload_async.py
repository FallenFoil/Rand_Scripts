#!/usr/bin/env python

from os import listdir
from os.path import isfile, isdir

import asyncio
import sys


class textColors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


async def upload_blob(iteration, source_file_name, destination_blob_name, storage_client, bucket_name, bucket):
    try:
        print(f'{textColors.GREEN}{iteration}:{textColors.END} File {textColors.UNDERLINE}{source_file_name}{textColors.END} uploaded to {textColors.UNDERLINE}{bucket_name}/{destination_blob_name}{textColors.END}')
    except:
        print(f'{textColors.RED}ERROR::{iteration}: File{textColors.UNDERLINE}{source_file_name}{textColors.END} not uploaded{textColors.END}')


async def send_files_in_parallel(all_files, storage_client, bucket_name, bucket):
    # tasks = []
    tasks = set()
    i = 1
    for file in all_files:
        tasks.add(asyncio.ensure_future(upload_blob(iteration=f'{i}/{len(all_files)}', source_file_name=file,
                     destination_blob_name=file, storage_client=storage_client, bucket_name=bucket_name, bucket=bucket,)))
        i += 1
        if len(tasks) == 1000:
            done, tasks = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
            for d in done:
                try:
                    res = await d
                except:
                    pass

    if len(tasks) > 0:
        done, _=await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
        for d in done:
            try:
                res=await d
            except:
                pass
    print('test')

def find_files(folder_path, file_list):
    for item in listdir(folder_path):
        item_path=f'{folder_path}/{item}'
        if isdir(item_path):
            find_files(item_path, file_list)
        elif isfile(item_path):
            file_list.append(item_path)


def split_list(all_files, n):
    size=len(all_files)
    chunk_size=size // n
    split_return=[]

    for i in range(n):
        if i == n-1:
            split_return.append(all_files[i*chunk_size:])
        else:
            split_return.append(all_files[i*chunk_size:(i+1)*chunk_size])

    return split_return


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f'{textColors.BLUE}Usage:{textColors.END}')
        print(f'{textColors.BLUE}  python upload_pdfs_2_cloud_storage.py <bucket-name> <folder-to-send>{textColors.END}')
        exit()

    path = sys.argv[2]
    bucket_name = sys.argv[1]
    num_threads = 4
    all_files = []
    threads = []

    try:
        print(f'{textColors.GREEN}Bucket {bucket_name} found{textColors.END}')
        print(f'{textColors.GREEN}Using path={path}{textColors.END}')

        # find_files(path, all_files)
        all_files = ['1']*80000

        print(f'{textColors.GREEN}all_files: {len(all_files)}{textColors.END}')
        asyncio.run(send_files_in_parallel(all_files, None, bucket_name, None))
    except Exception as e:
        print(e)
