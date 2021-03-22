
def parse(bad_subj):
    result = list()
    for el in bad_subj:
        if el.find('.py') != -1:
            result.append('не нужно вводить название .py файла')
            continue
        if el[1] == '0' or el[1] == ' ' or el[1] == '-':
            el = el[0] + el[2:len(el)]
        if len(el) < 4:
            result.append('недостаточно данных')
            continue
        if el[0].isalpha() and el[1:len(el)].isdigit():
            el = el[0:3] + ' ' + el[3:len(el)]
        # if el.find('\ufeff') != -1:
        #     el.replace('\ufeff', '')
        # if el.find('\u200b') != -1:
        #     el.replace('\u200b', '')
        # if el[0:5] == '\ufeff' or el[0:5] == '\u200b':
        #     while el[0:5] == '\ufeff' or el[0:5] == '\u200b':
        #         el = el[6:len(el)]
        # el.replace('\u200b', '').replace('\n', '').replace(' ', '')
        if (el[0] == 'k' or el[0] == 'K' or el[0] == 'К') and el[1].isdigit():
            el = 'к' + el[1:len(el)]
            result.append(el)
            continue
        if (el[0] == 'v' or el[0] == 'V' or el[0] == 'В') and el[1].isdigit():
            el = 'в' + el[1:len(el)]
            result.append(el)
            continue
        if (el[0] == 'n' or el[0] == 'N' or el[0] == 'Н') and el[1].isdigit():
            el = 'н' + el[1:len(el)]
            result.append(el)
            continue
        if (el[0] == 'm' or el[0] == 'M' or el[0] == 'М') and el[1].isdigit():
            el = 'м' + el[1:len(el)]
            result.append(el)
            continue
        if (el[0] == 'b' or el[0] == 'B' or el[0] == 'Б' or el[0] == 'б' or el[0] == 'и' or el[0] == 'h' or el[0] == 'H' or el[0] == 'И') and el[1].isdigit():
            # el = 'б' + el[1:len(el)]
            result.append('таких групп не существует')
            continue
        if el[0:4] == 'ИВБО':
            el = 'в' + el[el.find('-') + 1 : el.find('-') + 3] + ' ' + el[el.find('№') + 1 : len(el)]
            result.append(el)
            continue
        if el.find('Задача') != -1 or el.find('задача') != -1 or el.find('Задание') != -1 or el.find('задание') != -1:
            result.append('неверный формат темы')
            continue
        if el.startswith("Re"):
            result.append(el[el.rfind(' ') - 2 : len(el)])
            continue
        if el[el.rfind(' ') + 1].isalpha():
            result.append(el[0:el.rfind(' ') + 1] + el[el.rfind(' ') + 2:len(el)])
            continue
        if el.find('.') - el.rfind('.') == 2:
            result.append(el[len(el) - 5 : len(el)])
            continue
        result.append(el)
    print(len(result))
    return result


bad_subj = ['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14', 'к02 21', '1.3.py', 'В 11 4',
            '\ufeff\u200b\u200bк20 21', 'B7 21', 'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23',
            '1.2.py, 1.3.py, 1.4.py', '1.1.py', 'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21', 'к2 в3',
            'В104', 'В1013', 'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py',
            'К10', 'ПитонН4 н11', 'K13 28', 'К4', 'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5', 'Re: в6 28',
            'к-11 3', '2_1.py, 2_2.py']
print(len(bad_subj))
print(parse(bad_subj))


def bwt(line):
    lst = []
    lst.append(line)
    while(1):
        tempLine = lst[len(lst)-1]
        tempChar = tempLine[len(tempLine)-1]
        tempLine = tempLine[:len(tempLine) - 1]
        tempChar += tempLine
        if(tempChar == line):
            break
        lst.append(tempChar)
    lst = sorted(lst)
    print(lst)
    result = ''
    number = lst.index(line)
    for elem in lst:
        result += elem[len(lst)-1]
    print(result + ", " + str(number))
    reverce = list(result)
    while(1):
        if(reverce.__contains__(line)):
            break
        reverce = sorted(reverce)
        for i in range(len(result)):
            reverce[i] = result[i] + reverce[i]
    print(sorted(reverce))


def generate_groups():
    list_groups = {'K': 25, 'B': 13, 'M': 2, 'H': 10}
    with open('groups.txt', 'w') as file:
        for k, v in list_groups.items():
            for n in range(1, v + 1):
                file.write('{}{}\n'.format(k, n))


generate_groups()

def generate_array(*dim):
    return [*dim]

arr = generate_array([1, 2], [3, 4], [5, 6], [7,8])
print(arr)

def only_name(**mass):
    for key, value in mass.items():
        print("{} is {}".format(key, value))

only_name(name='Kanenkov Alexander', university='MIREA')