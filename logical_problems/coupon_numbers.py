import random
from log_module import get_logger

user_log = get_logger(name="(coupon_number)", file_name="logical_problems.log")


def coupon_number():
    """
    it will generate 5 unique random number
    :return:
    """
    try:
        chr_arr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        permission = True
        while permission:
            coupon = ''
            grant = input("Grant me a permission 'Yes' or 'No': ").lower()
            if grant == "yes":
                while len(coupon) < 5:
                    new_rand = random.choice(chr_arr)
                    if new_rand in coupon:
                        continue
                    coupon += new_rand
                user_log.debug(coupon)
            else:
                permission = False
                user_log.debug("permission granted FAIL !")
                return
    except Exception as e:
        user_log.error(e)


if __name__ == "__main__":
    coupon_number()

# Result
# Grant me a permission 'Yes' or 'No': yes
# C6qac
