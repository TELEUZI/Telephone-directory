import time
import pickle


def user_request ():
    print ("Приветствую, это самый лучший в мире справочник!")
    a={}
    with open('a.pickle', 'rb') as f:    
        a = pickle.load(f)
    while True:
        answer=input('''Что вы хотите сделать?
        1)Поиск
        2)Добавить контакт
        3)Удалить контакт
        4)Закрыть программу
        5)Список контактов
        ''')
        if answer=="1":
            search(a)
        elif answer=="2":
            new_contact(a)
        elif answer=="3":
            delete(a)
        elif answer=="4":
            print ("Спасибо за использование программы, сделанной T&O!")
            time.sleep(2) 
            break 
        elif answer=="5":
            print (a)
        else:
            print ("К сожалению, данный пункт меню не найден! Пожалуйста, введите цифры в промежутке от 1 до 4.")
            continue 


def search(current_database):
    search_type=input('''Выберите тип поиска:
            1) Поиск по имени
            2) Поиск по номеру'''
            )
    if search_type=="1":
        name=input("Введите имя ")
        if name in current_database:
            print ('Вы искали абонента {} с номером {}, верно?'.format(name,current_database[name]))
        else:
            print ("К сожалению, такого человека в данной телефонной книге нет!")
    elif search_type=="2":
        found=False
        number=input("Введите номер ")
        for person in current_database:
            if current_database[person]==number:
                print ('Вы искали абонента {} с номером {}, верно?'.format(person,current_database[person]))
                found=True
        if found==False:
            print ("К сожалению, такого номера в данной телефонной книге нет!")
            

def new_contact(current_database):
    name_of_the_person=input("Введите имя контакта ")
    number_of_the_person=input("Введите номер контакта ")
    current_database[name_of_the_person]=number_of_the_person
    with open('a.pickle', 'wb') as f:    
        pickle.dump(current_database, f)
    print ("Контакт успешно создан!")


def delete(current_database):
    while True:
        print ('''Введите имя контакта, который Вы хотите удалить или введите 'назад', чтобы 
вернуться в главное меню ''')
        name_of_the_person=input()
        if name_of_the_person in current_database: 
            del current_database[name_of_the_person]
            print ("Контакт успешно удалён!")
            with open('a.pickle', 'wb') as f:    
                pickle.dump(current_database, f)
            break
        elif name_of_the_person=='назад':
            break
        else:
            continue


user_request ()