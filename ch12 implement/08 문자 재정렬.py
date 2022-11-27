n = input()

result = ""
num = 0

for i in range(len(n)):
    if n[i].isalpha() == True:
        result += n[i]
    else:
        num += int(n[i])
result += str(num)

print(result)