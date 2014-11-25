
def input_work_details():
    hours = float(input("Please enter your hours worked: "))
    pay = float(input("Please enter your pay rate per hour: "))
    return hours,pay
    

def calculate_basic_pay(hours,pay):
    total = hours * pay
    return total


def calculate_overtime_pay(hours,pay):
    overtime_pay = pay * 1.5
    overtime_hours = hours - 40
    overtime_total = overtime_pay * overtime_hours
    basic_total = 40
    total = basic_total + overtime_total
    return total

def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_overtime_pay(hours,pay)
    return total

def display_total_pay(total):
    print(total)

    
def calculate_pay():
    hours,pay = input_work_details()
    total = calculate_total_pay(hours,pay)
    display_total_pay(total)
    

#main program

calculate_pay() 
