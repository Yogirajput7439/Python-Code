def calculate_tax(salary):
    if (salary <= 30000):
        tax = (5/100)*salary
        print(f"you salary is {salary} your tax is {tax}")

    elif ( 30000 < salary < 70000):
        tax2 = (15/100)*salary
        print(f"you salary is {salary} and your tax is {tax2}")
        
    elif (salary > 70000):
        tax3 = (25/100)*salary
        print(f"your salary is {salary} and your tax is {tax3}")
        
    else:
        print("invalid salary")
        
        

salary = int(input("enter you salary : "))
calculate_tax(salary)