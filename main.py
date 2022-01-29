import csv
import re

def fix_name_telephone(phonebook):
    for el in phonebook:
        name = ' '.join(el[:3])
        sep_name = name.split(' ')
        result = [sep_name[0], sep_name[1], sep_name[2],
                el[3], el[4],
                re.sub(r"(\+7|8)?\s?\(?(\d{3})\)?[-|\s]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*\(?(\w*\.)?\s?(\d*)\)?", r"+7(\2)\3-\4-\5 \6\7", el[5]),
                el[6]]
        new_contacts_list.append(result)

def fix_dublicates(phonebook):
    for el in phonebook:
        surname = el[0]
        name = el[1]
        for el_2 in phonebook:
            new_surname = el_2[0]
            new_name = el_2[1]
            if surname == new_surname and name == new_name:
                index = 2
                while index <= 6:
                    if el[index] == '':
                        el[index] = el_2[index]
                    index += 1
    for element in phonebook:
        if element not in fix_list:
            fix_list.append(element)

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    new_contacts_list = []
    fix_list = []
    fix_name_telephone(contacts_list)
    fix_dublicates(new_contacts_list)

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(fix_list)




