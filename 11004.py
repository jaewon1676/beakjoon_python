# 백준 11004 K번째 수
# 정렬
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
print(s[k - 1])
