def pall(word):
    for x in range(len(word)//2):
        if word[x] != word[len(word) - x - 1]:
            return "No"
    return"Yes"  
word = input()
print(pall(word))