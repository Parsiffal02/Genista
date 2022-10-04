def swapThree(a, b, c):
    a = a + b + c 
    b = a - (b+c) 
    c = a - (b+c) 
    a = a - (b+c) 
    print("After swapping a =",a,", b =",b,", c =",c)
if __name__ == '__main__':
    a = 1
    b = 2
    c = 3
    print("Before swapping a =",a,", b =",b,", c =",c)
    swapThree(a, b, c)