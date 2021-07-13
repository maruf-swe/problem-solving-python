'''
QST
Read an integer .

Without using any string methods, try to print the following:
input=3
output 123

Note that "" represents the values in between.
'''

#another solution
#print(*range(1, int(input())+1), sep='')

n = int(input())
for i in range(1, n+1):
    print(i, end='')         #end = "" for this output in single line
