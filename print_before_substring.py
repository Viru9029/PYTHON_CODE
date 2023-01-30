# Remove after substring in String


def remove_string_after_substring(str, substring):
    split_string = str.split()
    for i in range(len(split_string)):
        if split_string[i] == substring:
            res = split_string[:i] + [substring]
            print(" ".join(res))


test_str = 'geeksforgeeks is best for geeks'
sub_str = "best"
remove_string_after_substring(test_str, sub_str)
