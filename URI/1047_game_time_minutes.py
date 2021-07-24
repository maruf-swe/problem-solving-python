s_h, s_m, f_h, f_m = list(map(int, input().split()))
fh = f_h - s_h
if (fh < 0):
    fh = 24 + (f_h - s_h)
fm = f_m - s_m
if (fm < 0):
    fm = 60 + (f_m - s_m)
    fh = fh - 1
if (f_h == s_h and f_m == s_m):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(fh, fm))
