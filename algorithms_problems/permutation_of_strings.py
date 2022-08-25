def permute(string_, answer):
    if len(string_) == 0:
        print(answer, end=" ")
        return

    for i in range(len(string_)):
        ch = string_[i]
        left_substring = string_[0:i]
        right_substring = string_[i + 1:]
        rest = left_substring + right_substring
        permute(rest, answer + ch)


if __name__ == "__main__":
    ans = ""
    input_string = input("Enter the string : ")
    print("All possible strings are : ")
    permute(input_string, ans)

# Result
# Enter the string : ABC
# All possible strings are :
# ABC ACB BAC BCA CAB CBA
