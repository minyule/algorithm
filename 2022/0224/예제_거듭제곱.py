# 거듭제곱을 재귀로 풀어봐요
def power(base, exponent):
    if exponent == 0 or base == 0:
        return 1

    if exponent % 2: # 홀수면
        newBase = power(base, (exponent - 1)/2)
        return newBase * newBase * base
    else: # 짝수번 
        newBase = power(base, exponent/2)
        return newBase * newBase

print(power(2, 5))