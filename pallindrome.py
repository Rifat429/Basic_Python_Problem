def palindrome(text):
    if(len(text)<=1):
        # print(text)
        print("It is a Pallindrome")
    else:
        if (text[0]==text[-1]):
            print(text)
            palindrome(text[1:-1]) #slicing
        else:
            print("It is not a pallindrome")


palindrome("madam")
palindrome("abba")