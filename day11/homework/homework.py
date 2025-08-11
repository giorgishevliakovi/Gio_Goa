#while loop-ით შეგვიძლია უსასრულოდ გამოტანა ტერმინალში ნებისმიერი რამის ხოლო for loop-ით არა.

num = int(input("შეიყვანე რიცხვი: "))
if num > 18:
    print("you are big adult")
else:
    print("you are child")


i = 1
while i < 10:
    print(i)
    i = i + 1

i = 1
while i < 20:
    print(i)
    i = i + 1

i = 100
while i > 0:
    print(i)
    i = i - 1