# Task 5
# def f(n):
#     t = bin(n)
#     a = '000' + t[2:]
#     if n % 3 == 0:
#         r = a + a[-3:]
#     else:
#         w = n % 3
#         w = w * 3
#         v = bin(w)
#         v = v[2:]
#         r = a + v
#     r = int(r, 2)
#     return r
# n = 0
# while True:
#     n += 1
#     r = f(n)
#     if r >= 200:
#         print(r)
#         print(n)
#         break
# Ans: 26
# Task 17
# with open('DEMO_17.txt', 'r') as f:
#     rl = f.readlines()
#     for i in range(len(rl)):
#         if '\n' in rl[i]:
#             rl[i] = rl[i].replace('\n', '')
#         if '\t' in rl[i]:
#             rl[i] = rl[i].replace('\t', '')
#         rl[i] = int(rl[i])
#     s = list(set(sorted(rl)))
#     min_val = None
#     for el in s:
#         if el > 9:
#             min_val = el
#             break
#     ans = 0
#     sm = 0
#     for i in range(len(rl) - 1):
#         a = rl[i]
#         b = rl[i + 1]
#         if (len(str(b)) == 2 and len(str(a)) != 2) or (len(str(b)) != 2 and len(str(a)) == 2):
#             if (a + b) % min_val == 0:
#                 ans += 1
#                 sm = max(sm, a + b)
#     print(ans, sm) # 150 9930
# Task 16
# def f(n):
#     return 2 * (g(n - 3) + 8)
#
# def g(n):
#     if n < 10:
#         return 2 * n
#     else:
#         if n % 2 == 0:
#             return n // 2 + 12
#         return (n + 1) // 2 + 13
# print(f(15548))
# #15588