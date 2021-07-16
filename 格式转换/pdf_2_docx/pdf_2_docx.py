from pdf2docx import parse
import os
import glob
from pathlib import Path

path = os.getcwd()+'/'
p = Path(path)
Filelist = p.glob('**/*.pdf')
# print(Filelist)

for file in Filelist:
    # f = str(file)
    print(f)
    # f1 = f.split('.pdf')[0]
    print(f1)
    parse(file,f1+'.docx')