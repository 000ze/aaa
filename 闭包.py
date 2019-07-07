'''time = 0


def insert_time(min):
    global time
    time = time + min
    return time


print(insert_time(2))
print(insert_time(10))
print(time)'''

time = 0
def study_time(time):
    def insert_time(min):
        nonlocal time
        time = time + min
        return time

    return insert_time


f = study_time(time)  # f相当于是insert_time对象
print(f.__closure__)
print(f(2))           # f(2)相当于调用了insert_time（2）
print(time)
print(f(10))          # f(10)相当于调用了insert_time（10）
print(time)
