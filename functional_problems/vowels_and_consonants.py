def vowels_consonants(alphabets):
    if alphabets == 'a' or 'A':
        print("vowel")
    elif alphabets == 'e' or 'E':
        print("vowel")
    elif alphabets == 'i' or 'I':
        print("vowel")
    elif alphabets == 'o' or 'O':
        print("vowel")
    elif alphabets == 'u' or 'U':
        print("vowel")
    else:
        print("consonants")


if __name__ == '__main__':
    alphabet = input("enter the alphabets: ")
    vowels_consonants(alphabet)

# Result
# enter the alphabets: O
# vowel
