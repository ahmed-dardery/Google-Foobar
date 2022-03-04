def computeF(F, S, n):
    F[0] = 0
    for i in range(2, n):
      l = F[i - 1]
      while(l and S[i] != S[l]):
          l = F[l - 1]
      F[i] = l + (S[i] == S[l])

def solution(s):
    l = len(s)
    F = [0] * l
    computeF(F, s, l)
    
    patLen = l - F[l - 1]
    cnt = l / patLen
    return cnt
