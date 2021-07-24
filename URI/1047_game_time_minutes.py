# s_h = start hour, s_m = start minute, f_h = finish hour, f_m = finish minute
s_h, s_m, f_h, f_m = list(map(int, input().split()))
total_hours = f_h - s_h
if (total_hours < 0):
    total_hours = 24 + (f_h - s_h)
total_minutes = f_m - s_m
if (total_minutes < 0):
    total_minutes = 60 + (f_m - s_m)
    total_hours = total_hours - 1

if (f_h == s_h and f_m == s_m):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(total_hours, total_minutes))
