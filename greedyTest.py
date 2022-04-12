N, P = int(input()), list(map(int, input().split()))

P = sorted(P)

answer = 0

for i  in range(N):
    for j in range(i+1):
        answer += P[j]
    
print(answer)