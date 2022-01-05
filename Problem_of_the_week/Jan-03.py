def doubler(str):
    temp = ''
    for i in str:
        temp = temp + i + i
    print(temp)

print(doubler("now"))
print(doubler("abc123"))