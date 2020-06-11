Rd, Rm, Ry = map(int, input().split(' '))  # rd, rm, ry = [int(x) for x in input().split(' ')]
Ed, Em, Ey = map(int, input().split(' '))
fine = 0
if Ey < Ry:
    fine = 10000
elif (Ry == Ey):
    if Rm > Em:
        fine = 500 * (Rm - Em)
    elif Rd > Ed:
        fine = 15 * (Rd - Ed)

print(fine)
