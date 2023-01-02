array = [('바나나',2),('사과',5),('당근',3)]

# 방법 1
def setting(data):
    return data[1]
result1 = sorted(array, key=setting)
print(result1)

# 방법 2
result2 = sorted(array, key=lambda x:x[1])
print(result2)