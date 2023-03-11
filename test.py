def multiply(**kwargs):
    start = 1
    for digit in kwargs:
        start *= digit
    print(start)

result = multiply(5, 1)
print(result)