# читаем адресную книгу в формате CSV в список contacts_list
import csv
from pprint import pprint
import re
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

pattern1 = r'(\+7|8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s?\(?(доб.\s\d{4})?\)?'
substitution = r'+7(\2)\3-\4-\5 \6'

new_contacts_list = []
for string_contact in contacts_list:
    fio_list = ' '.join(string_contact[0:3]).split()

    if len(fio_list) != 3:
        fio_list.append('')
    full_list = fio_list + string_contact[3:]
    full_list[5] = re.sub(pattern1, substitution, full_list[5])

    for new_contacts in new_contacts_list:
        if new_contacts[0:2] == fio_list[:2]:
            re_new_contacts = []
            for x,y in zip(new_contacts, full_list):
                if x == '':
                    re_new_contacts.append(y)
                re_new_contacts.append(x)
            full_list = re_new_contacts
            new_contacts_list.remove(new_contacts)
    new_contacts_list.append(full_list)

# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)


