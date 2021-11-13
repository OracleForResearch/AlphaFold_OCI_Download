#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse


def pg_bar(array_length:int, counter:int)->None:
    '''
    File extraction progress bar

    :param array_length: Length of the input array
    :param counter: Current index of the array
    :return: None
    '''
    percentage = round((float(counter) / array_length) * 100, 2)
    pg = "|" * int(percentage)
    space = "-" * (100 - len(pg))
    bar = "\r 0% [{0}{1}] 100%   File extraction progress: {2}%".format(pg, space, percentage)
    sys.stdout.write(bar)
    sys.stdout.flush()
    return None


def download_mmcifPDB(folder_path:str)->None:
    '''
    Download mmCIF files from Oracle Open Data Bucket

    :param folder_path: Path to the folder where database should be stored
    :return: None
    '''
    cmd = "rclone --fast-list --transfers=128 --checkers=128 --buffer-size=2G " \
          "--max-backlog=999999 copy oss:pdb/data/structures/all/mmCIF/ {0}/".format(folder_path)
    os.system(cmd)
    return None


def extractor_pdb_mmcif(folder_path:str)->None:
    '''
    Extract 'gz' files

    :param folder_path: Path to the folder containing  *.cif.gz files
    :return: None
    '''

    if folder_path[-1] == "/":
        folder_path = folder_path
    else:
        folder_path = folder_path + "/"

    flist = os.listdir(folder_path)
    print("Extracting '*.cif.gz' files .... ")
    flist_len = len(flist)
    for i in range(flist_len):
        file = flist[i]
        cmd = "gunzip {0}/{1}".format(folder_path, file)
        p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        p.communicate()
        pg_bar(array_length=flist_len, counter=i)
    return None


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("-path", help="Path to the pdb_mmcif folder", required=True, type=str)
    paser = args.parse_args()

    download_mmcifPDB(paser.path)
    extractor_pdb_mmcif(paser.path)
