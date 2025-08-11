#<, >, ==, !=
#< ნაკლების მნიშვნელობა
#> მეტიას მნიშვნელობა
#== უდრის ან არ უდრის მნიშვნელობა
#!= არ უდრის მნიშვნელობა



#ლოგიკური ოპერატორები: or, and
# or გამოიყენება როდესაც ჩვენ გვინდა რამოდენიმე პირობიდან თუ ერთერთი არის სწორი მაშინ გამოიტანოს true/სწორი
# and გამოიყენება როდესაც  თუ ყველა პირობა სწორია მაშინ გამოიტანს True/სწორი



print(True and 6<7 or "hello"!=5.4 and False or 7-7 < 9+2)

#true გამოვა რადგან ყველა პასუხი სწორია



#ნებისმიერთან შეგვიძლია გამოყენება



print(True and True)     # True
print(True and False)    # False
print(False and True)    # False
print(False and False)   # False

print(True or True)      # True
print(True or False)     # True
print(False or True)     # True
print(False or False)    # False

