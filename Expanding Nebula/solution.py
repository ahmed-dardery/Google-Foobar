class DP:
	def __init__(self, g):
		self.n = len(g)
		self.m = len(g[0])

		self.g = g
		self.mem = [[[[-1 for _ in range(self.m)] for _ in range(self.n)] for _ in range(2)] for _ in range(1 << (self.n+1))]
	
	def solve(self):
		ans = 0
		for msk in range(1 << (self.n + 1)):
			for prev in range(2):
				ans += self.dp(msk, prev, 0, 0)
		return ans
	def dp(self, msk, prev, i, j):
		nmsk = msk | 1 << i if prev else msk & ~(1 << i)
		
		if i == self.n:
			return self.dp(nmsk, 0, 0, j + 1) + self.dp(nmsk, 1, 0, j + 1)
		if j == self.m:
			return prev == 0
			
		ret = self.mem[msk][prev][i][j]
		if ret != -1: return ret
		ret = 0
		
		curBit = self.g[i][j]
		cntCur = (msk>>i & 1) + (msk>>(i+1) & 1) + prev
		if curBit == True:
			if cntCur <= 1:
				ret = self.dp(nmsk, cntCur == 0, i + 1, j)
		else:
			if cntCur <= 1:
				ret = self.dp(nmsk, cntCur == 1, i + 1, j)
			else:
				ret = self.dp(nmsk, 0, i + 1, j) + self.dp(nmsk, 1, i + 1, j)
		
		self.mem[msk][prev][i][j] = ret
		return ret

def solution(g):
	solver = DP(g)
	return solver.solve()


sample1 = solution([
[True, True, False, True, False, True, False, True, True, False],
[True, True, False, False, False, False, True, True, True, False],
[True, True, False, False, False, False, False, False, False, True],
[False, True, False, False, False, False, True, True, False, False]
]), 11567

sample2 = solution([
[True, False, True],
[False, True, False],
[True, False, True]
]), 4

sample3 = solution([
[True, False, True, False, False, True, True, True],
[True, False, True, False, False, False, True, False], 
[True, True, True, False, False, False, True, False], 
[True, False, True, False, False, False, True, False], 
[True, False, True, False, False, True, True, True]
]), 254

samples = sample1, sample2, sample3

for s in samples:
	print(s)