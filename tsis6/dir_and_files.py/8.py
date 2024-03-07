import os
if os.path.exists('C:\\Users\\Asus\\Desktop\\delete_file.txt') == True:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'C:\\Users\\Asus\\Desktop\\delete_file.txt')
    os.remove(path)
else:
    print("NOT FOUND")