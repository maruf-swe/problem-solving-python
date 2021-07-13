def split_and_join(line):
    separated_join = line.replace(" ", "-")
    return separated_join
    # write your code here


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
