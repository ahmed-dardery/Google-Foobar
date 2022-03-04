def solve(M, F):
    if M < F: M,F = F,M
    cnt = 0
    while M != F and min(M, F) > 0:
      #print(M, F, M//F)
      cnt += M//F
      M, F = M % F, F
      if M < F: M,F = F,M
      
    return strcnt-1 if M == 1 else "impossible"

def solution(x, y):
    return solve(int(x), int(y))
    

print(solution('4', '7'))
print(solution('1', '2'))

print(solution('4', '6'))

print(solution('4000000000000000000000000000001', '100000000000000000000000000000000000000000000000000'))
