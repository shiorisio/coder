import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T = read().rstrip().decode()

T

def f(n, r, l, z):
    # 長さnの1が座標 r から l へと移動する。
    # z回立ち止まることが許されている。
    # 獲得スコアの最大値は？
    if n % 2 == 0:
        move = r - l + z
        return (move + 1) * (n // 2)
    if r == l and r % 2 == 0:
        # ev, od, ev, od, evで固定
        k = (n - 1) // 2
        move = r - l + z
        return (move + 1) * k
    # 各地点に1回ずつ立ち寄りつつ、奇数のところでz回足踏みできる
    ev = (r // 2) - ((l - 1) // 2)
    od = (r - l + 1) - ev
    od += z
    k = (n - 1) // 2
    return ev * k + od * (k + 1)

Z = T.count('0')
one = 0
to = 0
answer = 0
for i, x in enumerate(T, 1):
    if x == '0':
        if one:
            answer += f(one, i - 1, to, Z)
            one = 0
        Z -= 1
        continue
    to += 1
    one += 1
if one:
    answer += f(one, i, to, Z)

def f(n):
    # '1' * n から減らしたときのスコア
    # ただし、最初は除く
    ret = 0
    for i in range(0, n, 2):
        ret += (n - i)
    ret -= (n + 1) // 2
    return ret

n = T.count('1')
answer += f(n)
print(answer)
