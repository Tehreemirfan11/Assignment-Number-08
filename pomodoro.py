work_time = 25 * 60
break_time = 5 * 60
cycles = 4

for _ in range(cycles):
    print("Work for 25 minutes!")
    for _ in range(work_time* 10):
        pass

    print("Take a 5-minute break!")
    for _ in range(break_time* 10):
        pass