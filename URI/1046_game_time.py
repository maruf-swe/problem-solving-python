start, finish = list(map(int, input().split()))
if start < finish:
    time = finish - start
else:
    time = finish + 24 - start
print("O JOGO DUROU", time, "HORA(S)")
