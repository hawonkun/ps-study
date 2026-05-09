import sys
input = sys.stdin.readline

# 인접 노드 확인 함수 (두 수가 한 자리수만 다른 지 판별)
def is_connected(a, b):
    for n in range(4): # n: n번째 자리 숫자, 네 번째 자리수까지 반복 (0 ~ 3)
        an = a % (10 ** (n + 1)) // (10 ** n) # an: a에서 n번째 자리수
        bn = b % (10 ** (n + 1)) // (10 ** n) # bn: b에서 n번째 자리수
        if a - an * (10 ** n) == b - bn * (10 ** n): # a에서 n번째 자리를 없앤 수와 n번째 자리를 없앤 수가 같은가?
            return True
    return False

# BFS
def bfs():
    pass

# 4자리 구하기 (에라토스테네스의 체 사용)
start = 1000
end = 9999

prime = [True] * (end + 1)
prime[0] = prime[1] = False

for i in range(2, int(end**0.5) + 1):
    if prime[i]:
        for j in range(i*i, end + 1, i):
            prime[j] = False

stops = [i for i in range(start, end + 1) if prime[i]]

# 인접 행렬 만들기
adj_matrix = [[False] * len(stops) for _ in range(len(stops))]

for i, v in enumerate(stops):
    for j, u in enumerate(stops):
        if is_connected(v, u):
            adj_matrix[i][j] = True