import os
import urllib.request
import zipfile

# 다운로드 링크
url = "http://modelnet.cs.princeton.edu/ModelNet40.zip"
filename = 'ModelNet40.zip'

print('Start Download')
if not os.path.exists(filename):
    urllib.request.urlretrieve(url, filename)
print('Download complate')

with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall()
print('Decompression Complate')