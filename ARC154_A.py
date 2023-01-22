import io
import sys

_INPUT = """\
6
2
13
22
8
20220122
21002300
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N=int(input())
  A=list(map(int,list(input())))
  B=list(map(int,list(input())))
  A,B=[max(A[i],B[i]) for i in range(N)],[min(A[i],B[i]) for i in range(N)]
  print(sum([A[i]*pow(10,(N-i-1),mod)%mod for i in range(N)])*sum([B[i]*pow(10,(N-i-1),mod)%mod for i in range(N)])%mod)