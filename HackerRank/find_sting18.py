def count_substring(string, sub_string):
    counter = 0
    len_string = len(string)
    len_subStr = len(sub_string)
    for i in range(0, len_string):
        if string[i:i + len_subStr] == sub_string:
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)




