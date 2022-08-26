import random


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
                print(coupon)
            else:
                permission = False
                print("permission granted FAIL !")
                return
    except Exception as e:
        print(e)


if __name__ == "__main__":
    coupon_number()

#Result
# Grant me a permission 'Yes' or 'No': yes
# C6qac