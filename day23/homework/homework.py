# მისალმების ფუნქცია
def misalmeba():
    print("გამარჯობა!")

# ორის შეკრება
def shekreba(a, b):
    return a + b

# ლუწი თუ კენტი
def luwi_tu_kenti(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

# სახელი და ასაკი
def saxeli_da_asaki(name, age):
    print(name + " არის " + str(age) + " წლის.")

# მაქსიმალური მნიშვნელობა
def max_mnishvneloba(a, b, c):
    return max(a, b, c)