def builder(n, m, seq=[], start=0):
    if m == 0:
        yield seq
    for i in range(start, n):
        for x in builder(n, m - 1, seq + [i], i + 1):
            yield x

def solution(num_buns, num_required):
    sol = [[] for i in range(num_buns)]
    v = 0
    for it in builder(num_buns, num_buns-num_required+1):
        for i in it:
            sol[i].append(v)
        v += 1
    return sol
