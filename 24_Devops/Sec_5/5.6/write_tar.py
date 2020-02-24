import tarfile
with tarfile.open('tarfile_add2.tar', mode='w:gz') as f:
    f.add('/etc')