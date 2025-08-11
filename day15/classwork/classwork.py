month = int(input("შეიყვანე შენი დაბადების დღის თვე"))

if month == 1 or month == 3 or month == 12:
    print("ზამთარი")

elif month >= 3 and month <= 5:
    print("გაზაფხული")

elif month >= 6 and month <= 8:
    print("ზაფხული")

elif month >= 9 and month <= 11:
    print("შემოდგომა")

else:
    print("არასწორი რიცხვია.")



ricxvi = float(input("შეიყვანე რიცხვი 0-დან 10-მდე"))

if ricxvi > 0:
    print("დადებითია")

elif ricxvi < 0 :
    print("უარყოფითია")

else:
    print("რიცხვი ნულია")



#if არის: თუ (რაღაცა)
#else არის: სხვა შემთხვევაში
#elif არის იგივე if უბრალოდ ვიყენებთ რამდენჯერაც გვინდა ანუ, if-ს რომ დავწერთ და კიდევ გვინდა if-ის დაწერა, მაგის მაგივრად დავწერთ elif-ს უსასრულოდ

age = int(input("შეიყვანე შენი ასაკი"))
income = int(input("შეიყვანე შენი შემოსავალი"))

if age < 18 and income <10000:
    print("განთავისუფლებული ხარ")


else:
    print("გადასახადი გადასახდელია")


ricxvi = int(input("შეიყვანე რიცხვი 1 დან 10 მდე"))

if ricxvi > 10:
    print("მეტია")

elif ricxvi <10:
    print("ნაკლებია")

else:
    print("უდრის 10")