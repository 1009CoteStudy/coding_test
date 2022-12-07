N = int(input())

datas = []

for _ in range(N):
    data = int(input())
    datas.append(data)

num_stack = []
command_stack = []

for i in range(1, N + 1):
    if i != datas[0]:
        num_stack.append(i)
        command_stack.append('+')
    else:
        num_stack.append(i)
        command_stack.append('+')

        if len(datas) > 0:
            cur = datas[0]
            num_stack.append(datas.pop(0))
            command_stack.append('-')

            while len(datas) > 0 and datas[0] <= cur:
                if num_stack[-1] != datas[0]:
                    break

                cur = datas[0]
                datas.pop(0)
                command_stack.append('-')

    if len(datas) == 0:
        break

if len(datas) == 0:
    for data in command_stack:
        print(data)

else:
    print('NO')