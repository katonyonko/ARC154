import io
import sys

_INPUT = """\
6
3
2
1 2
2 2
4
2 3 1 1
2 1 1 2
2
1 1
2 2
2
4
3 1 2 2
1 2 2 3
6
2 1 4 3 2 3
1 2 2 2 2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    ans='No'
    a,b=[A[0]],[B[0]]
    for i in range(N-1):
      if A[i]!=A[i+1]: a.append(A[i+1])
      if B[i]!=B[i+1]: b.append(B[i+1])
    if len(a)>1 and a[-1]==a[0]: a.pop()
    if len(b)>1 and b[-1]==b[0]: b.pop()
    if len(b)==N:
      if A==B: ans='Yes'
    else:
      for i in range(len(a)):
        tmp=0
        for j in range(len(a)):
          if a[(i+j)%len(a)]==b[tmp]:
            tmp+=1
          if tmp==len(b):
            ans='Yes'
            break
    print(ans)