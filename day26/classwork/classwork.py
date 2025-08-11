#1
def is_positive(number):
    if number >0:
        return True
    else:
        return False
    

#2
def max_of_two(a,b):
    if a >b:
        return a
    else:
        return b


#3
def max_of_three(a, b, c,):
    if a >=b and a >=c:
        return a
    elif b >= a and b >=c:
        return b
    else:
        return c

#4
def is_hot(temperature):
    if temperature >= 30:
        return True
    else:
        return False