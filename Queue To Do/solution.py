def xor(n):
    return [n, 1, n+1, 0][n%4]

def xor_range(s, e):
    return xor(e) ^ xor(s-1)

def solution(start, length):
    LAST = 2000000000
    
    ans = 0
    l = length
    while l > 0 and start <= LAST:
      end = min(start + l - 1, LAST)
      ans ^= xor_range(start, end)
      start += length
      l -= 1
    return ans
