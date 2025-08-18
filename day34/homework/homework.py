# 1) რატომ გვჭირდება ფუნქციები?
# 👉 ფუნქციები გვიმარტივებს კოდს: ერთხელ ვწერთ და მერე ბევრჯერ ვიყენებთ.

# 3) ფუნქცია double_values (გაორმაგება)
def double_values(a, b, c):
    return [a * 2, b * 2, c * 2]

# 4) ფუნქცია - მხოლოდ ლუწები
def even_numbers(a, b, c, d):
    result = []
    if a % 2 == 0:
        result.append(a)
    if b % 2 == 0:
        result.append(b)
    if c % 2 == 0:
        result.append(c)
    if d % 2 == 0:
        result.append(d)
    return result

# 5) ფუნქცია - კვადრატში აყვანა
def squares(a, b, c):
    return [a ** 2, b ** 2, c ** 2]

# 6) ფუნქცია - ტოვებს მხოლოდ ხმოვანებს
def only_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    if len(text) > 0 and text[0] in vowels:
        result += text[0]
    if len(text) > 1 and text[1] in vowels:
        result += text[1]
    if len(text) > 2 and text[2] in vowels:
        result += text[2]
    return result

# 7) ფუნქცია - მხოლოდ უარყოფითი რიცხვები
def negative_numbers(a, b, c):
    result = []
    if a < 0:
        result.append(a)
    if b < 0:
        result.append(b)
    if c < 0:
        result.append(c)
    return result

# 8) ფუნქცია - მხოლოდ დადებითი რიცხვები
def positive_numbers(a, b, c):
    result = []
    if a > 0:
        result.append(a)
    if b > 0:
        result.append(b)
    if c > 0:
        result.append(c)
    return result

# 9) რიცხვი კვადრატში და *10-ზე
def square_times_ten(n):
    return (n ** 2) * 10

# 10) x აყვანილი y ხარისხში
def power(x, y):
    return x ** y