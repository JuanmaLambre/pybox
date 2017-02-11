import pybox


def test_ls_metadata():
    """Check ls_metadata feature"""
    entries = pybox.ls_metadata('/test')
    files = map(lambda e: e.name, entries)
    assert 'test_download.txt' in files

def test_ls():
    """Check ls feature"""
    files = pybox.ls('/test')
    assert 'test_download.txt' in files

def test_download():
    """Check download feature"""
    content = pybox.download('/test/test_download.txt')
    assert content == 'happy text'

def test_upload():
    """Check upload feature"""
    pybox.upload('happy upload', '/test/should_be_deleted.txt')
    entries = pybox.dbx.files_list_folder('/test/').entries
    entries = map(lambda e: e.name, entries)
    assert 'should_be_deleted.txt' in entries
    pybox.dbx.files_delete('/test/should_be_deleted.txt')

