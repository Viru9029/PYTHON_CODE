#Q12.) Write a Python program to print all permutations with a given repetition number of characters of a given string. 
# def permutation_repetitions(string, repetition):
#     string1 = [string]*repetition
#     for i in range(len(string)):
#         for j in range(len(string)):
#             print([string[i],string[j],string[j]],end=',')


# permutation_repetitions('xyz',2)

# def permutations(lis):
#     if len(lis) == 1:
#         return [lis]

#     output = []
#     *front, last = lis
    
#     for perm in permutations(front):
#         for i in range(len(perm) + 1):
#             new = perm[:i] + [last] + perm[i:]
#             output.append(new)

#     return sorted(output)

# string = input('Enter a string : ')
# print(permutations(string))


from itertools import product
def all_repeat(str1, rno):
  chars = list(str1)
  results = []
  for c in product(chars, repeat = rno):
    results.append(c)
  return results


string = input('Enter a string : ')
repitation_no = int(input('Enter a repetition no : '))
print(all_repeat(string,repitation_no))