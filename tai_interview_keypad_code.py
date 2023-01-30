
numbers = {1: 1, 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
           7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z'], '*': '*', 0: 0, '#': '#'}

def for_single_enter_no(num):
    print(numbers.get(num))

def for_two_enter_no(num):
    covert = list(str(num))
    combination_list = []
    first_no = int(covert[0])
    second_no = int(covert[1])
    first_no_letter = numbers[first_no]
    second_no_letter = numbers[second_no]
    for i in range(len(numbers[first_no])):
        for k in range(len(numbers[first_no])):
            combination_list.append(first_no_letter[i] + second_no_letter[k])
    print(combination_list)

def letter_combination_of_number(no):
    if len(no) == 1:
        no1 = int(no)
        for_single_enter_no(no1)
    elif len(no) == 2:
        no1 = int(no)
        for_two_enter_no(no1)
    else:
        print('Other combination in progress')


n1 = 1
letter_combination_of_number('97')




