#2
num = ["ძროხა", "ძაღლი", "კატა"]
num.insert(1, "კუ")
print(num)

#3
num = [10, 20, 30, 40, 50]
print(num[0])  # პირველი
print(num[-1])  # ბოლო

#4
num = "მეგობრები"
num2 = len(num)
print(num2)

#5
num = ["მე", "მიყვარს", "გოა"]
num2 = len(num)
print(num2)

#6
num = ["reality", "laughing at the gore," "okolofutbola"]
num.insert(2, "pantera")
print(num)

#8 8გადააკეთე სტრიქონიჯერ  დიდ ასოებად მერე პატარად და საბოლოოდ პირველ ასო გაზარდე
num = "gamArjOba"
num.upper()
print(num)

num = "gamArjOba"
num.lower()
print(num)

num = "gamArjOba"
num.capitalize()
print(num)

#9 9:იპოვე სიტყვა "პითონი" წინადადებაში find() ფუნქციით და დაბეჭდე მისი მდებარეობა.

num = "CSS" "HTML" "python" "JavaScript"
num.find("python")
print(2)

#10 10:შექმენი სია და ჩასვი "კომფეტი" მეორე პოზიციაზე insert()-ით
num = ["სნიკერსი, ბაუნტი, ტვიქსი"]
num.insert(1, "კომფეტი")
print(num)

#11 11:დაწერე ფუნქცია double(n), რომელიც იღებს რიცხვს და აბრუნებს მის ორმაგს.
def double(n):
    return n * 2
print(double(5))
print(double(3.5))

#12 12:დაწერე ფუნქცია is_even(n), რომელიც აბრუნებს True თუ რიცხვი ლუწია, და False თუ კენტია.

def is_even(n):
    return n % 2 == 0
print(is_even(4)) #True
print(is_even(7)) #False




