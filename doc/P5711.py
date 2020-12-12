yr = int(input())

if yr % 100 == 0:
    if yr % 400 == 0:
        print(1)
    else:
        print(0)
else:
    if yr % 4 == 0:
        print(1)
    else:
        print(0)