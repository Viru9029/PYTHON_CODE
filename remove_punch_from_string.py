import string
print(string.punctuation)


def remove_punch(str):
    punch = string.punctuation
    for ele in str:
        if ele in punch:
            str = str.replace(ele,'')
    print(str)


test_str = "Gfg, is best : for ! Geeks ;"
remove_punch(test_str)
