# 1) ახსნა:
# ფუნქციები Python-ში არის კოდის ნაწილი, რომელსაც სახელი აქვს და აკეთებს კონკრეტულ მოქმედებას.
# ისინი გვეხმარება კოდის გამარტივებაში, ხელახლა გამოყენებაში და შეცდომების პოვნაში.

# 3) გაორმაგება
def double_values(numbers):
    result = []
    for n in numbers:
        result.append(n * 2)
    return result

# 4) მხოლოდ ლუწი რიცხვები
def even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

# 5) კვადრატში აყვანილი ელემენტები
def square_values(numbers):
    result = []
    for n in numbers:
        result.append(n ** 2)
    return result

# 6) მხოლოდ ხმოვანი ასოები
def filter_vowels(text):
    vowels = "აეიოუAEIOUaeiou"
    result = ""
    for ch in text:
        if ch in vowels:
            result += ch
    return result

# 7) მხოლოდ უარყოფითი რიცხვები
def negative_numbers(numbers):
    result = []
    for n in numbers:
        if n < 0:
            result.append(n)
    return result

# 8) მხოლოდ დადებითი რიცხვები
def positive_numbers(numbers):
    result = []
    for n in numbers:
        if n > 0:
            result.append(n)
    return result

# 9) რიცხვი კვადრატში და გამრავლებული 10-ზე
def square_and_times_ten(x):
    return (x ** 2) * 10

# 10) x აყვანილი y ხარისხში
def power(x, y):
    return x ** y