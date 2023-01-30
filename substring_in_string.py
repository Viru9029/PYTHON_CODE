#Check if a Substring is Present in a Given String

# Example 1: Input : Substring = "geeks"
#            String="geeks for geeks"
# Output : yes

def string_present(string1,substring):
    if substring in string1:
        print('present substring')
    else:
        print('not present')

string_present("geeks for geeks","geeks")