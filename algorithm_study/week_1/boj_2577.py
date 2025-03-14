a = int(input())
b = int(input())
c = int(input())

product = list(str(a * b * c))
for i in range(0, 10):
    print(product.count(str(i)))
