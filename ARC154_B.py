import io
import sys

_INPUT = """\
6
4
abab
abba
3
arc
cra
3
arc
abc
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import Counter
  N=int(input())
  S=input()
  T=input()
  if Counter(list(S))==Counter(list(T)):
    now=N-1
    now2=N-1
    while now2>=0:
      while now2>=0 and S[now]!=T[now2]: now2-=1
      if now2<0: break
      now-=1
      now2-=1
    print(now+1)
  else: print(-1)
