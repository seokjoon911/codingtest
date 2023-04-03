n = int(input())

for _ in range(n):
    money = int(input())
    changes = []

    for i in [25, 10, 5, 1]:
        changes.append(money // i) # 몫
        money = money % i # 나머지 다시 C에 저장

    print(*changes)