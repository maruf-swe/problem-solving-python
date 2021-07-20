N1, N2, N3, N4 = list(map(float, input().split()))
average = (((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10)
print("Media: %.1lf" % average)
if (average >= 7.0):
    print("Aluno aprovado.")
elif (average < 5.0):
    print("Aluno reprovado.")
elif (average >= 5.0 and average <= 6.9):
    print("Aluno em exame.")
    N5 = float(input())
    print("Nota do exame: %.1lf" % N5)
    one_more = (average + N5) / 2
    if (one_more >= 5.0):
        print("Aluno aprovado.")
    if (one_more <= 4.9):
        print("Aluno reprovado.")
    print("Media final: %.1lf" % one_more)
