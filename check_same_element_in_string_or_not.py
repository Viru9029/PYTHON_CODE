test_str1 = 'e:e:k:s:g'
test_str2 = 'g:e:e:k:s'

res = sorted(test_str1.split(':')) == sorted(test_str2.split(':'))
print(res)
