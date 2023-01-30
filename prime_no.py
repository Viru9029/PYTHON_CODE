#prime no

def prime_no(x,y):
    prime_list = []
    for i in range(x,y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    print(prime_list)

prime_no(0,10)



#check wheter prime no or not
def check_prime_no(a):
    if a == 0 or a == 1:
        print("NOT PRIME no")
    else:
        for i in range(2,int(a/2)+1):
            if a % i == 0:
                print("No is NOT PRIME")
                break
        else:
            print("Number is PRIME")

check_prime_no(6)

