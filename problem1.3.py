import string

def form_dict_letter_number(filename):
    dic = {}
    with open(filename, 'r') as f:
        for line in f:
            for letter in line.lower():
                if letter.isalpha():
                    if letter in dic:
                        dic[letter] += 1
                    else:
                        dic[letter] = 1
    return dic

def print_pairs(dicList):
    for item in dicList:
        print str(item[0]) + ': ' + str(item[1])

def get_sorted_pairs(dic):
    dicList = dic.items()
    dicList = sorted(dicList, key=lambda item: item[0])
    dicList = sorted(dicList, key=lambda item: item[1], reverse=True)
    return dicList

dic = form_dict_letter_number('input.txt')
dicList = get_sorted_pairs(dic)
print_pairs(dicList)

