n = int(input("input seconds"))
print("{}:{}:{}".format(int(n / 3600), int(n % 3600 / 60), int(n % 60)))

# another way
import datetime
print(str(datetime.timedelta(seconds=666)))
