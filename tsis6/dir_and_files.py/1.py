import os

for dirpath, dirnames, filenames in os.walk('/Users/Asus/Desktop'):
    print('Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()