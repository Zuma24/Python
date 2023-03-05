#1
a = int(input("Введите число 1 "))
b = int(input("Введите число 2 "))
c = int(input("Введите число 3 "))
print(a+b+c)

#2
a = int(input("Введите число 1 "))
b = int(input("Введите число 2 "))
print(a%2==b%2)

#3
a = int(input("Введите число 1 "))
b = int(input("Введите число 2 "))
if a>b:
    print(b)
else:
    print(a)

#4
a = int(input("Введите число "))
if a>999 and a<10000:
    print("YES")
else:
    print("NO")

#5
n = int(input("n= "))
m = int(input("m= "))
print(f"{m//n} дней")

#6
a = int(input("1 класс= "))
b = int(input("2 класс= "))
c = int(input("3 класс= ")) 
print(f"Необходимое число парт в 1 классе - {-(a)//2*-1}")
print(f"Необходимое число парт в 2 классе - {-(b)//2*-1}")
print(f"Необходимое число парт в 3 классе - {-(c)//2*-1}")
print(f"Необходимое число парт {-(a)//2*-1 + -(b)//2*-1 + -(c)//2*-1}")


