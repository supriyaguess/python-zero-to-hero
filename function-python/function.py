#WAP to print the length of a list
cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor","ironman","captain america","shaktiman"]

print(heroes[0], end="\n")
print(heroes[1], end="\n")


def print_len(list):
    print(len(list))

print_len(heroes)
print_len(cities)

def print_list(list):
    for item in list:
        print(item, end="  ")
print_list(heroes)
print_list(cities )
print()

# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)


def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
cal_fact(6)

#WAF to convert USD to INR 

def coverter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD =", inr_val, "INR")

coverter(73)

def check_even_odd(n):
    if (n % 2 == 0):
        return "Even"
    else:
        return "Odd"
    
print(check_even_odd(4))   # Even
print(check_even_odd(7))   # Odd