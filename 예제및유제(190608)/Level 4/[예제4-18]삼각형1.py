# 출력: 삼각형
# 입력: n

n = int(input("n: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i >= j:
            print("*", end='')
    print()



