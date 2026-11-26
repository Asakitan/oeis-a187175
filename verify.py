"""Exact finite shape certificate for every board size, OEIS A187175."""
from collections import Counter
from itertools import product

MOVES=((2,1),(-1,2),(-2,-1),(1,-2))

def multiplicities():
    result=Counter()
    for word in product(MOVES,repeat=4):
        x=y=0
        points=[(x,y)]
        for a,b in word:
            x+=a
            y+=b
            points.append((x,y))
        if len(set(points))!=5:
            continue
        spans=tuple(max(c)-min(c) for c in zip(*points))
        result[tuple(sorted(spans))]+=1
    return result

if __name__=="__main__":
    h=multiplicities()
    assert h=={(2,6):4,(2,7):8,(3,5):16,(3,6):8,(3,7):8,
               (4,4):16,(4,5):8,(4,6):12,(4,8):4,(5,5):8,(5,6):8},h
    q=[sum(h.values()),-sum(k*(w+d) for (w,d),k in h.items()),
       sum(k*w*d for (w,d),k in h.items())]
    assert max(d for w,d in h)==8 and q==[100,-920,1984],q
    a=[sum(k*max(n-w,0)*max(n-d,0) for (w,d),k in h.items()) for n in range(11)]
    assert a[:8]==[0,0,0,0,0,16,136,456]
    den=[1,-3,3,-1]
    num=[sum(den[i]*a[n-i] for i in range(min(n+1,4))) for n in range(11)]
    p=[0]*5+[2,12,18,15,3,0]
    assert num==[8*p[n]-4*(p[n-1] if n else 0) for n in range(11)],num
    print("A187175: all 256 words checked; 100 shapes; exact GF numerator verified.")
