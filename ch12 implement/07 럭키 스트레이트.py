n = input()

left = 0
right = 0
whole = 0
for i in range(len(n)//2):
    left += int(n[i])
for j in range(len(n)):
    whole += int(n[j])
right = whole - left

if left == right:
    print("LUCKY")
else:
    print("READY")