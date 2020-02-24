import zipfile
newzipfile = zipfile.ZipFile('new.zip', 'w')
newzipfile.write('backupfile.py')
newzipfile.close()