print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature:"))
rain = input("Will it rain (yes/no):")
print("Wear jeans and a T-shirt")
cold = "I recommend a jumper as well"
colder = "Take a jacket with you"
coldest = "Make it a warm coat, actually"
coldrain = "I think gloves are in order"
wet = "Don't forget your umbrella!"
if temp>20:
    if rain=="yes":
        print(wet)

elif temp<=20:
    print(cold)
    if temp<=10:
        print(colder)
        if temp<=5:
            print(coldest+"\n"+coldrain)

    if rain=="yes":
        print(wet)
