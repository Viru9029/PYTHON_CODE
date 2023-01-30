def string_reverse(strings):
    sep_words = strings.split()
    final_string = []
    for i in range(0,len(sep_words)):
        final_string.append(sep_words[i][::-1])
    print(" ".join(final_string))


string_reverse("Hello World")