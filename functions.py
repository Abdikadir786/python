def add(a,b):
    sum =a+b
    return(sum)
print(add(5,10))
print(add(601,720))
print(add(1040,2392))




def add(a=5,b=10):
    sum=a+b
    return sum
print(add())

def add(a,b=10):
    sum=a+b
    return sum
print(add(120))

print(add(120,120))


def add(a=10,b=20):
    sum=a+b
    return sum
print(add(500,200))
print(add())

def students(*names):
    print('student 1 is ' + names[1])
students('John','Abdi','Mercy')