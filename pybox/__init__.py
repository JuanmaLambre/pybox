#!/usr/bin/python

import dropbox
import os


DROPBOX_TOKEN = open('pybox/.dropbox_token', 'r').read()
dbx = dropbox.Dropbox(DROPBOX_TOKEN)


def ls(path=''):
    entries = dbx.files_list_folder(path).entries
    return map(lambda e: e.name, entries)

def ls_metadata(path=''):
    return dbx.files_list_folder(path).entries

def upload(text, path):
    dbx.files_upload(text, path)

def download(filepath):
    if not filepath.startswith('/'):
        filepath = '/' + filepath
    tmpfilepath = filepath.split('/')[-1]
    dbx.files_download_to_file(tmpfilepath, filepath)
    with open(tmpfilepath, 'r') as tmpfile:
        content = tmpfile.read()
    os.remove(tmpfilepath)
    return content

