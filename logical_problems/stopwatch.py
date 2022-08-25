import time


def starttopwatch():
    start = int(input("please enter 1 to start stopwatch: "))
    start_time = time.time()
    while start == 1:
        n = int(input("please enter 0 to stop: "))
        if n == 0:
            break
    elapsed_time_secs = time.time() - start_time
    print(f"{round(elapsed_time_secs, 4)} sec")


if __name__ == "__main__":
    starttopwatch()

# Result
# please enter 1 to start stopwatch: 1
# please enter 0 to stop: 0
# 1.6091 sec
