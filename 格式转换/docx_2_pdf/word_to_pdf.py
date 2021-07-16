from docx2pdf import convert
import os
from pathlib import Path

path = os.getcwd()+'/'
p = Path(path)
Filelist = p.glob('**/*.docx')
# print(Filelist)

for file in Filelist:
    f = str(file)
    # print(f)
    f1 = f.split('.docx')[0]
    # print(f1)
    convert(file, f1+'.pdf')
