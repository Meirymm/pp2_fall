#1
for i in range(6):
  print(i)
  i += 1
#2
for i in range(1,6):
  print(i)
#3
for i in range(1,6,2):
  print(i)
#4
for i in range(6):
  print(i)
else:
    print("Finally finished!")
#5
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") 
#6
for x in range(6):
  if x == 3: continue
  print(x)
else:
  print("Finally finished!")
