A, B, C, D = map(int, input().split())

def battle(player):
    global A
    global C

    if player == 1:
        C = C - B
    else:
        A = A - D

    return None

def main():
    while True:
       battle(1)
       if C <= 0:
           print("Yes")
           break

       battle(2)
       if A <= 0:
           print("No")
           break

    return None

main()
