import os

print(os.access('\\Users\\Asus\\Desktop\\ENGLISH.txt', os.F_OK))##TRUE
print(os.access('\\Users\\Asus\\Desktop\\ENGLISH.txt', os.R_OK)) ###TRUE
print(os.access('\\Users\\Asus\Desktop\\ENGLISH.txt', os.W_OK))  ###TRUE
print(os.access('\\Users\Asus\\Desktop\\ENGLISH.txt', os.X_OK))  ###TRUE
