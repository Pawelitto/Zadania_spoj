# def last_digit(a, b):
#     if b == 0:
#         return 1
#     elif b % 4 == 0:
#         return (a ** 4) % 10
#     else:
#         return (a ** (b % 4)) % 10

# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     print(last_digit(a, b))

[print(pow(*map(int, input().split()), 10)) for _ in range(int(input()))]
