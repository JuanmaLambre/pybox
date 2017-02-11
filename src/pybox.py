#!/usr/bin/python

import dropbox


dbx = dropbox.Dropbox(open('.dropbox_token', 'r').read())


def ls(path=''):
    return dbx.files_list_folder(path).entries

def upload(text, path):
    dbx.files_upload(text, path)

def download(filepath):
    return dbx.get_file_and_metadata(filepath)[0]


