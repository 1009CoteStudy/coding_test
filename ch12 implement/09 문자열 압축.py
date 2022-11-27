data = input()

lenth = len(data)

for i in range(1,len(data)+1):
    for j in range((len(data))//i):
        if data[j*i:(j+1)*i+1] == data[(j+1)*i:(j+2)*i+1]:
            lenth -= i
print(lenth)