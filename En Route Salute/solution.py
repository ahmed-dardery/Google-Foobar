def solution(s):
    ans = 0
    right = 0
    for c in s:
      if c == '>':
        right += 1
      elif c == '<':
        ans += right
    return ans*2
