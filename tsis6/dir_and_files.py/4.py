with open('C:\\Users\\Asus\\Desktop\\ENGLISH.txt', 'r') as f:
    file = f.read()
    l = 0
    for string in file:
        l += len(string)
    print(l)