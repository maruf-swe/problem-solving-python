def swap_case(s):
    after_swap = s.swapcase()
    return after_swap


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

'''
def swap_case(s):
    return s.swapcase(s)


if __name__ == '__main__':
    s = input()
    print(swap_case(s))
'''