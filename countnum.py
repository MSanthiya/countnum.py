x = int(input("Please Enter any Number: "))
Count = 1
while(x > 0):
    x= x // 10
    Count = Count + 1
    print(" Number of Digits in a Given Number ", Count)
