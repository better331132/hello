from random import randrange
import datetime, time

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

d1 = datetime.datetime.strptime('1/1/1900', '%m/%d/%Y')
d2 = datetime.datetime.strptime('3/12/2018', '%m/%d/%Y')

print(random_date(d1,d2))