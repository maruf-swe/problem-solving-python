i = 0
j = 1
while i < 2.1:
    if i == 0 or i == 1:
        print(f'i={int(i)} j={int(j + i)}')
        print(f'i={int(i)} j={int(j + 1 + i)}')
        print(f'i={int(i)} j={int(j + 2 + i)}')
        i += 0.2
    elif i == 2:
        print(f'i={int(i)} j={int(j + i)}')
        print(f'i={int(i)} j={int(j + 1 + i)}')
        print(f'i={int(i)} j={int(j + 2 + i)}')
        i += 0.2
    else:
        print(f'i={i:.1f} j={j + i:.1f}')
        print(f'i={i:.1f} j={j + 1 + i:.1f}')
        print(f'i={i:.1f} j={j + 2 + i:.1f}')
        i += 0.2
