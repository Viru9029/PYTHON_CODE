def signal_light(str,k):
    dist1 = {'R':'G','B':'R','G':'B'}
    dist2 = {'R':'B','B':'G','G':'R'}
    final = ""
    if k == 1:
        for i in range(len(str)):
            if str[i] in dist1:
                final += dist1.get(str[i])
    elif k == 2:
        for i in range(len(str)):
            if str[i] in dist2:
                final += dist2.get(str[i])
    return final

print(signal_light('RBRG',1))