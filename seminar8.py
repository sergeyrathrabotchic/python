
def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phon.txt')

    phone_book_count = len(phone_book)

    while (choice!=8):

        if choice==1:
            # print("Работает")
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname: ')
            print(*find_by_lastname(phone_book,last_name))
        elif choice==3:
            # last_name=input('lastname ')
            new_number=input('new  number: ')
            print(*find_by_number(phone_book,new_number))
	    	
        elif choice==4:
            lastname = input('Укажите фамилию: ')
            name = input('Укажите имя: ')
            phon = input('Укажите телефон: ')
            description = input('Напишите описание: ')
            print(new_data(phone_book,lastname, name, phon,  description))
        elif choice==5:
            print(write_txt('phon.txt',phone_book, phone_book_count))
        elif choice==6:
            name = ''
            lastname=input('Укажите фамилию абонента которого хотите изменить или оставте поле пустым, если хотите найти по имени: ')
            if (len(lastname) == 0):
                name=input('Укажите имя абонента которого хотите изменить : ')
            lastname_change = input('Укажите фамилию: ')
            name_change = input('Укажите имя: ')
            phon = input('Укажите телефон: ')
            description = input('Напишите описание: ')     
            print(find_end_change_by_number(phone_book,lastname,name, lastname_change, name_change,phon,description))
            # add_user(phone_book,user_data)
            # write_txt('phonebook.txt',phone_book)
        elif choice==7:
            name = ''
            lastname=input('Укажите фамилию абонента которого хотите удалить или оставте поле пустым, если хотите найти по имени: ')
            if (len(lastname) == 0):
                name=input('Укажите имя абонента которого хотите удалить : ')
            print(find_end_remove_by_number(phone_book,lastname,name))


        choice=show_menu()


def print_result(phone_book):
    result = []
    for i in phone_book:
        for arg1  in i:
            arg = arg1  + ": " + i[arg1].strip() + " | "  
            result.append(arg)
        print(*result)
        result = []

def find_by_lastname(phone_book,last_name):
    result = []
    check = False

    for i in phone_book:
        for arg1 in i:
            if(check):
                arg = arg1  + ": " + i[arg1].strip() + " | "
                result.append(arg)
            if(arg1 == 'Фамилия' and i[arg1].strip() == last_name.strip()):
                check = True 
                arg = arg1  + ": " + i[arg1].strip() + " | "
                result.append(arg)
        check = False
                
    return result
                  
def find_by_number(phone_book,last_name):
    result = []
    check = False

    for i in phone_book:
        for arg1 in i:
            if(check):
                arg = arg1  + ": " + i[arg1].strip() + " | "
                result.append(arg)
            if(arg1 == 'Телефон' and i[arg1].strip() == last_name.strip()):
                check = True
                arg = "Фамилия"  + ": " + i["Фамилия"].strip() + " | "
                result.append(arg)
                arg = "Имя"  + ": " + i["Имя"].strip() + " | "
                result.append(arg)
                arg = arg1  + ": " + i[arg1].strip() + " | "
                result.append(arg)
        check = False
                
    return result

def find_end_change_by_number(phone_book,lastname,name, lastname_change, name_change,phon,description):
    
    check = 0 

    if (len(name) == 0):
        for i in range(len(phone_book)):
            for arg1 in phone_book[i]:
                if(arg1 == 'Фамилия' and phone_book[i][arg1].strip() == lastname.strip()):
                    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
                    line = [lastname_change, name_change, phon,  description + '\n'] 
                    record = dict(zip(fields, line))
                    phone_book[i] = record
                    check = 1
                    result = "Изменение внесены"
            if (check) :
                break
    else:
        for i in range(len(phone_book)):
            for arg1 in phone_book[i]:
                if(arg1 == 'Имя' and phone_book[i][arg1].strip() == name.strip()):
                    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
                    line = [lastname_change, name_change, phon,  description + '\n'] 
                    record = dict(zip(fields, line))
                    phone_book[i] = record
                    result = "Изменение внесены"
            if (check):
                break
    if (not check):
        result = "Запись не найдена"          
    return result

def find_end_remove_by_number(phone_book,lastname, name):
    check = 0 
    if (len(name) == 0):
        for i in range(len(phone_book)):
            for arg1 in phone_book[i]:
                if(arg1 == 'Фамилия' and phone_book[i][arg1].strip() == lastname.strip()):
                    check = 1
            if (check):
                break
    else:
        for i in range(len(phone_book)):
            for arg1 in phone_book[i]:
                if(arg1 == 'Имя' and phone_book[i][arg1].strip() == name.strip()):
                    check = 1
            if (check):
                break
    if (check):
        phone_book.pop(i)
        result = "Запись удалена"
    else: 
        result = "Запись не найдена"          
    return result

def new_data(phone_book,lastname, name, phon,  description):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    line = [lastname, name, phon,  description] 
    record = dict(zip(fields, line))
    if (phone_book.append(record) == None):
        return 'Успешно добавили данные'
    else :
        return 'Ошибка' 





def show_menu():
    print("\nВыбирите необходимые дествие:\n"
          "1. Отобразите весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить абонентасправочник в текстовом формате\n"
          "6. Изменить абонентасправочник в текстовом формате\n"
          "7. Удалить абонентасправочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input())
    return choice
















# РРІР°РЅРѕРІ,       РРІР°РЅ ,   111,  РѕРїРёСЃР°РЅРёРµ РРІР°РЅРѕРІР°
# РџРµС‚СЂРѕРІ,      РџРµС‚СЂ ,    222,  РѕРїРёСЃР°РЅРёРµ РџРµС‚СЂРѕРІР°

# Р’Р°СЃРёС‡РєРёРЅР° , Р’Р°СЃРёР»РёСЃР° , 333 , РѕРїРёСЃР°РЅРёРµ Р’Р°СЃРёС‡РєРёРЅРѕР№

# РџРёС‚РѕРЅРѕРІ,    РђРЅС‚РѕРЅ,     777,    СѓРјРµРµС‚ РІ РџРёС‚РѕРЅ

















def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

	

    with open(filename,'r',encoding='utf-8') as phb:
        # print(phb)
        # print(111111)

        for line in phb:
            # print(line)
            record = dict(zip(fields, line.split(',')))
            # print(record)
			#dict(( (С„Р°РјРёР»РёСЏ,РРІР°РЅРѕРІ),(РёРјСЏ, РўРѕС‡РєР°),(РЅРѕРјРµСЂ,8928) ))
            phone_book.append(record)	

    return phone_book








def write_txt(filename , phone_book, phone_book_count):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','
            if (i < phone_book_count):
                phout.write(f'{s[:-1]}')
            else: 
                phout.write(f'{s[:-1]}\n')
    
    return "Данные сохранены"















work_with_phonebook()

























