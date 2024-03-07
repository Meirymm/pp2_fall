with open('C:\\Users\\Asus\\Desktop\\ENGLISH.txt', 'r') as file1, open('C:\\Users\\Asus\\Desktop\\lab6.txt', 'a') as file2:
    for i in file1:
        file2.write(i)

with open('C:\\Users\\Asus\\Desktop\\lab6.txt') as new:
    print(new.read())