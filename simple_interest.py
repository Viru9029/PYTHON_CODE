#simple interest program

principle_amount = float(input("Enter Principal Amount : "))
time = float(input("Enter the time period : "))
rate_of_int = float(input("Enter the rate of interest : "))

def simple_interest(p,t,r):
    simple_int = (p*t*r)/100
    print(simple_int)
    return simple_int

simple_interest(principle_amount,time,rate_of_int)