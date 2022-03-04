from fractions import Fraction, gcd

def solution(w, h, s):
	tot = 0

	for pn in partitions(w):
		for pm in partitions(h):
			co = coeff(pn) * coeff(pm)
			
			cur = 1

			for a in ZS(pn):
				for b in ZS(pm):
					_, p = combine(a, b)
					cur *= s**p
			
			tot += Fraction(cur, co)
	return str(tot.numerator)


def partitions(n):
	for p in _partitions(n, n, []):
	    yield p

def _partitions(n, i, J):
	if i == 1:
		yield list(reversed(J + [n]))
		return
	j = 0
	while j*i <= n:
		for p in _partitions(n - j * i, i - 1, J + [j]):
		    yield p
		j += 1
		
# compresses J and returns only positive parts
def ZS(J):
	a = []
	for _, jk in enumerate(J):
		k = _ + 1
		if jk > 0:
			a.append((k, jk))
	return a

#combines a_p^x with b_q^y
def combine(a, b):
	p, x = a
	q, y = b
	
	g = gcd(p, q)
	lcm = p // g * q
	
	return lcm, x * y * g

#O(n) as sum of jk*k = n, so sum of jk <= n
def coeff(J):
	#C(J) = MUL(k^jk * jk!)
	ans = 1
	for _, jk in enumerate(J):
		k = _ + 1
		for c in range(jk):
			ans *= (c+1) * k
	return ans
