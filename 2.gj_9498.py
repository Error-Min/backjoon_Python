num = int(input())

if(num >= 90):
    print("A")
elif(num <= 89 and 80 <= num ):
    print("B")
elif(num <= 79 and 70 <= num ):
    print("C")
elif(num <= 69 and 60 <= num ):
    print("D")
else:
    print("F")