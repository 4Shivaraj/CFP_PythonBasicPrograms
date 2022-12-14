import time
from log_module import get_logger

user_log = get_logger(name="(stop_watch)", file_name="logical_problems.log")


def start_stop_watch():
    """
    it will print elapsed time between start and stopping tine of stop watch
    :return: none
    """
    try:
        start = int(input("please enter 1 to start stopwatch: "))
        start_time = time.time()
        while start == 1:
            n = int(input("please enter 0 to stop: "))
            if n == 0:
                break
        elapsed_time_secs = time.time() - start_time
        user_log.debug(f"{round(elapsed_time_secs, 4)} sec")
    except Exception as e:
        user_log.error(e)


if __name__ == "__main__":
    start_stop_watch()

# Result
# please enter 1 to start stopwatch: 1
# please enter 0 to stop: 0
# 1.6091 sec
