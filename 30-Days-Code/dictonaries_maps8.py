n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {key: value for key,value in name_numbers}
while True:
    try:
        query_name = input()
        if query_name in phone_book:
            print('%s=%s' % (query_name, phone_book[query_name]))
        else:
            print('Not found')
    except:
        break



n = int(input())  # this code goes to run time error
phone_book = {}
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

for _ in range(n):
    query_name = input().lower()
    if query_name in phone_book:
        print(query_name + "=" + phone_book[query_name]) #print("{}={}".format(query_name, p_b[q_n]))
    else:
        print("Not found")


