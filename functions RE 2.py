

def odd_checker(number):
    if number % 2 == 0:
        print("The number you have entered is not odd")
    else:
        inv_pyramid(number)



def inv_pyramid(number):
    center = number
    while number > 0:
        astrix = "*"
        print("{0:^{1}}".format(astrix * number,center))
        number -= 2



number = int(input("Please enter a odd number: "))
odd_checker(number)

