# 백준 2579 / 계단 오르기
# 완탐은 시간초과.
# 답지 참고, 점화식 세우기!!

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있음.
# 연속된 세 개의 계단을 모두 밟아서는 안 됨. 시작점 제외.
# 마지막 계단은 반드시 밟아야 함.
# 얻을 수 있는 최대 점수는?

import sys


# 계단의 개수
n = int(sys.stdin.readline().rstrip())
score = [0 for _ in range(n+3)]
dp = [0 for _ in range(n+3)]
# 계단 정보 (점수)
for i in range(1, n+1):
    score[i] = int(sys.stdin.readline().rstrip())


dp[1] = score[1]
dp[2] = score[1] + score[2]
# 이 부분이 핵심.
# dp 같을 때는 좁은 범위에서 점화식 생각해보기.
dp[3] = max(score[1] + score[3], score[2] + score[3])


for i in range(4, n+1):
    dp[i] = max(dp[i-3] + score[i-1] + score[i],  dp[i-2] + score[i])
print(dp[n])