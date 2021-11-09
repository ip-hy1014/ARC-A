n = int(input())
l = []
for i in range(1,555556):
  i = str(i)
  num = list(i)
  if all(x==num[0] for x in num):
    l.append(i)
print(l[n-1])

#別解
import math
n = int(input())
# N番目のゾロ目数の桁数
x = math.ceil(n/9)
# N番目のゾロ目数の数字
y = n%9
if y==0:
    y=9
# 答えの文字列
ans = ""
# 答えはyがx桁並んだものとなる
for _ in range(x):
    ans += str(y)
print(ans)