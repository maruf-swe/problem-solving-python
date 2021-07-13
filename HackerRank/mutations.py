def mutate_string(string, position, character):
    stringList = list(string)
    stringList[position] = character
    string = ''.join(stringList)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



print("How To add character by replacing. formola 1")
string = 'abcdefghij'
l = list(string)
l[5] = 'm'
string = ''.join(l)
print(string)
print("Formola 2")
string = string[:5] + "k" + string[6:]
print(string)
