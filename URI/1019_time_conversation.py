# another
n = int(input())
print("{}:{}:{}".format(int(n / 3600), int(n % 3600 / 60), int(n % 60)))

n = int(input("input seconds"))  # for user input msg doesn't accept
print("{}:{}:{}".format(int(n / 3600), int(n % 3600 / 60), int(n % 60)))


# another way
import datetime
print(str(datetime.timedelta(seconds=666)))

# another
seconds = int(input("input: "))
minutes = int(seconds / 60)
seconds %= 60
hours = int(minutes / 60)
print('{}:{}:{}'.format(hours, minutes, seconds))

# another
S = int(input())
H = int(S / (60 * 60))
S = S % (60 * 60)
M = int(S / 60)
S = S % 60
print("%d:%d:%d" % (H, M, S))
