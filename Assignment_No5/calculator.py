from math import ceil
import requests
class Calulator:     
    def add(self,x,y):
        self.x = x
        self.y = y
        print("{0} + {1} = ".format(self.x, self.y),self.x+self.y)
    
    def sub(self,x,y):
        self.x = x
        self.y = y
        print("{0} - {1} = ".format(self.x, self.y),self.x-self.y)

    def mul(self,x,y):
        self.x = x
        self.y = y
        print("{0} * {1} = ".format(self.x, self.y),self.x*self.y)

    def div(self,x,y):
        self.x = x
        self.y = y
        print("{0} / {1} = ".format(self.x, self.y),self.x/self.y)

    def mod(self,x,y):
        self.x = x
        self.y = y
        print("{0} % {1} = ".format(self.x, self.y),self.x%self.y)

    def floor_div(self,x,y):
        self.x = x
        self.y = y
        print("{0} // {1} = ".format(self.x, self.y),self.x//self.y)

    def square(self,a):
        self.a = a
        print("{0} square is : ".format(self.a),a**2)

    def square_rt(self,a):
        self.a = a
        print("{0} square root is : ".format(self.a),a**0.5)

    def cube(self,a):
        self.a = a
        print("{0} cube is : ".format(self.a),a**3)

    def cube_rt(self,a):
        self.a = a
        print("{0} cube root is : ".format(self.a),ceil(a**0.333333))

    def nth_degree(self,x,y):
        self.x = x
        self.y = y
        print("{0} nth degree is : ".format(self.x, self.y),self.x**self.y)

    def nth_root(self,x,y):
        self.x = x
        self.y = y
        print("{0} nth root is : ".format(self.x, self.y),self.x**(1/self.y))

    def area_of_trangle(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        s = (side1 + side2 + side3) / 2 
        area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
        print("Area of trangle is : ",area)

    def find_percentage(self,value,total_value):
        self.value = value
        self.total_value = total_value
        print("{0} percentage is : ".format(self.value, self.total_value),(self.value/self.total_value)*100,'%')

    

        
currency_country_name = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP',
 'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP',
  'PLN', 'RON', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

operator = print("""\t\t\ta.	For Addition Press ' + '
                        b.	For Subtraction Press ' - '
                        c.	For Multiplication Press ' * '
                        d.	For Division Press ' / '
                        e.	For Finding remainder Press ' % '
                        f.	For floor division Press ' // '
                        g.	For Square Press ' sq '
                        h.	For Square root Press ' sqrt '
                        i.	For Cube Press ' cu '
                        j.	For Cube root Press ' curt '
                        k.	Nth Degree of number ( N * N ) Press ' nthd '
                        l.	Nth root of number ' nrt '
                        Note : Enter the expression by using space sepearated.
                        For example : 23 + 26 , 50 - 10 , 25 * 5 , 20 / 2 , 5 % 4 ,
                        29.5 // 2 , 5 sq , 25 sqrt , 2 cu , 2 curt , 10 nthd 2 , 10 nrt 2 ,.etc

                        Currency Names : 'AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP',
                        'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP',
                        'PLN', 'RON', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR'
                        Currency Convert eg: 100 'INR' 'USA'

                        Area of triangle eg : side1 side2 side3 art , 10 2 3 art

                        Find Percentage eg : value per total_value , 75 per 100
                        """)

Expression = input('Enter the Expression : ').split()

if Expression[1] in ['+', '-', '*', '/','%','//','nthd','nrt','per']:
    first_no = int(Expression[0])
    second_no = int(Expression[2])
elif Expression[1] in ['sq','sqrt','cu','curt']:
    first_no = int(Expression[0])
elif Expression[3] in ['art']:
    side1 = int(Expression[0])
    side2 = int(Expression[1])
    side3 = int(Expression[2])
    
Result = Calulator()

if Expression[1] == '+':
    Result.add(first_no,second_no)
elif Expression[1] == '-':
    Result.sub(first_no,second_no)
elif Expression[1] == '*':
    Result.mul(first_no,second_no)
elif Expression[1] == '/':
    Result.div(first_no,second_no)
elif Expression[1] == '%':
    Result.mod(first_no,second_no)
elif Expression[1] == '//':
    Result.floor_div(first_no,second_no)
elif Expression[1] == 'sq':
    Result.square(first_no)
elif Expression[1] == 'sqrt':
    Result.square_rt(first_no)
elif Expression[1] == 'cu':
    Result.cube(first_no)
elif Expression[1] == 'curt':
    Result.cube_rt(first_no)
elif Expression[1] == 'nthd':
    Result.nth_degree(first_no,second_no)
elif Expression[1] == 'nrt':
    Result.nth_root(first_no,second_no)
elif Expression[1] in currency_country_name:
    amount = float(Expression[0])
    from_currency = str(Expression[1])
    to_currency = str(Expression[2])
    response= requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
    print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
elif Expression[3] == 'art':
    Result.area_of_trangle(side1,side2,side3)
elif Expression[1] == 'per':
    Result.find_percentage(first_no,second_no)