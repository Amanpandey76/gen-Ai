"""first problem statement for assignment 1 Product Collection ( List and Tuple).

product = ["Mobile","Laptop","Tablet","Smartwatch","Headphones","Camera"]
sample_product = ("Earbuds",1999,"Wireless Earbuds with Noise Cancellation")

print([product[2], product[-1]])
updated_product = ("Speaker","Tv")
product.extend(updated_product )
print(product)

new_sample_product = list(sample_product)
new_sample_product[0]="Gadget"
new_sample_product[1]="2500"
new_sample_product[2]="Affordabel price"

print(tuple(new_sample_product))

####  Recursion function.

def pro(num):
    if num==0 or num==1:
        return 1
    else:
        return num*pro(num-1)
number=int(input("enter factorail number:-"))
print(pro(number))

def fact(num):
    if num==0 or  num==1:
        return 1
    else:
        fact=1
        for i in range(2,num+1):
            fact*=i
        return fact
number = int(input("Enter a number ="))
print(fact(number))

## multiple positional arguments in function.

def add(*num):
    sum=0
    for i in num:
        sum+=i
    print(f"sum of {num} is :",sum)
add(1,2,3,4,5,6,7,8,9,10)


## multiple keyword arguments in function.

def student(**data):
    for key, value in data.items():
        print(f"{key}:{value}")
student(name="Aman", age=24, gender="Male", city="Pune", Country="India")

## Multiple positional and keyword arguments in function.

def new_data(*add, **student_data):
    sum=0
    for i in add:
        sum+=i
    print(f"{add} sum is ={sum}")
    for key, value in student_data.items():
        print(f"{key}:{value}")
new_data(10,20,30, name="Sourav", age="22", gender="Male")

##### Notice :: never put the positional argument after the keyword argument in function :: it will give you an error.

## default argument in function.


def default_arg(name="Aman"):
    print(f"Hello {name}")

default_arg()
default_arg("Sourav")

def pass_strenght_checker(password):
    special_character=["!","@","#","$","&"]

    if len(password) < 8 :
        print("your must be as least 8 charaters")

    elif not any (char.islower() for char in password):
        print("your password must have the one or more lower character")

    elif not any (char.isupper() for char in password):
        print("your password must have the one or more lower character")

    elif not any (char.isdigit() for char in password):
        print("your password must have the one or more digit")

    elif not any ( char in special_character for char in password):
        print("your password must have the one spcial character")

    else :
        print(f"your type {password} is strong")

given = input("Enter your password:")
pass_strenght_checker(given)


### any() in Python is a built-in function that checks whether at least one item in a collection is True.
  # Remember it this syntax :: any(codition for item in collection) and (not) is a keyword that check wheather items present in collection or not
def palindrome(string):
     
    string_value = string.lower().replace(" ","")

    if string_value == string_value[ :: -1]:
          print(f"{string_value} is palindrome")
    else:
         print(f"{string_value} is not palindrome")
palindrome("Amm a ")

def apply_discount(prize, discount=5):

    if discount > 60:
        print(f"this much dicount is not granted {discount}%")

    else:
        discount_prize =round(prize-(prize* discount/100))
        print(f"Rs {discount_prize}")

apply_discount(1000,70)
apply_discount(500)"""




def factorial(num):
        
    if num == 0 or num == 1:
        print( "this is not factorial number")
    elif num < 0 :
        return "error"
    
    else:
        factorial_num = num * factorial(num-1)
        return factorial_num
        
print(factorial(5))
print(factorial(0))
print(factorial(-3))

