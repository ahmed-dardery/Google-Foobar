INF = 1000000000

class PushRelabel:
	class Edge:
		pass

	def __init__(self, n):
		self.g = [[] for i in range(n)]
		self.ec = [0] * n
		self.cur = [0] * n
		self.hs = [[] for i in range(2*n)]
		self.H = [0] * n
	
	def addEdge(self, s, t, cap, rcap=0):
		if s == t: return
		a, b = PushRelabel.Edge(), PushRelabel.Edge()
		a.dest, a.f, a.c, a.back = t, 0, cap, b
		b.dest, b.f, b.c, b.back = s, 0, rcap, a
		
		self.g[s].append(a)
		self.g[t].append(b)
	
	def addFlow(self, e, f):
		back = e.back
		if not (self.ec[e.dest] and f):
			self.hs[self.H[e.dest]].append(e.dest)
		e.f += f
		e.c -= f
		self.ec[e.dest] += f
		
		back.f -= f
		back.c += f
		self.ec[back.dest] -= f
	
	def calc(self, src, snk):
		v = len(self.g)
		self.H[src] = v
		self.ec[snk] = 1
		
		co = [0] * (2*v)
		co[0] = v - 1
		
		for e in self.g[src]: self.addFlow(e, e.c)
		
		hi = 0
		while True:
			while not self.hs[hi]:
				if hi == 0: return -self.ec[src]
				hi -= 1
			u = self.hs[hi].pop()
			
			while self.ec[u] > 0:
				if self.cur[u] == len(self.g[u]):
					self.H[u] = INF
					for i,e in enumerate(self.g[u]):
						if e.c and self.H[u] > self.H[e.dest] + 1:
							self.H[u] = self.H[e.dest] + 1
							self.cur[u] = i;
					co[self.H[u]] += 1
					co[hi] -= 1
					if (not co[hi]) and hi < v:
						for i in range(v):
							if hi < self.H[i] and self.H[i] < v:
								co[self.H[i]] -= 1
								self.H[i] = v + 1
					hi = self.H[u]
				else:
					ecur = self.g[u][self.cur[u]]
					if ecur.c and self.H[u] == self.H[ecur.dest] + 1:
						self.addFlow(ecur, min(self.ec[u], ecur.c))
					else: self.cur[u] += 1
		

def solution(entrances, exits, path):
	nPoints = len(path) + 2
	src, snk = nPoints - 2, nPoints - 1
	maxFlow = PushRelabel(nPoints)
	
	for i in range(len(entrances)):
		maxFlow.addEdge(src, i, INF)
	for i in range(len(exits)):
		maxFlow.addEdge(len(path) - 1 - i, snk, INF)
		
	for i in range(len(path)):
		for j in range(len(path[i])):
			if path[i][j]:
				maxFlow.addEdge(i, j, path[i][j])
	return maxFlow.calc(src, snk)


print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))