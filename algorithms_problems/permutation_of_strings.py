def permute(string_, answer):
    """
    if the reverse of the string is the same as string is permutation of string.
    :param string_: is user string input
    :param answer: empty string for storing the permuted string after the loop and recursion completion.
    :return: will return permutation of strings(ABC ACB BAC BCA CAB CBA).
    """
    try:
        if len(string_) == 0:
            print(answer, end=" ")
            return

        for i in range(len(string_)):
            ch = string_[i]
            left_substring = string_[0:i]
            right_substring = string_[i + 1:]
            rest = left_substring + right_substring
            permute(rest, answer + ch)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    ans = ""
    input_string = input("Enter the string : ")
    print("All possible strings are : ")
    permute(input_string, ans)

# Result
# Enter the string : ABC
# All possible strings are :
# ABC ACB BAC BCA CAB CBA
