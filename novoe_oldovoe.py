import time
import pickle
print ("Приветствую, это самый лучший в мире справочник!")
def user_request ():
    a={}
    with open('a.pickle', 'rb') as f:    
          a = pickle.load(f)
    while True:
        ans=input('''Что вы хотите сделать?
        1)Поиск
        2)Добавить контакт
        3)Удалить контакт
        4)Закрыть программу
        5)Список контактов
        ''') #ans=answer
        if ans=="1":

            ans2=input('''Выберите тип поиска:
            1) Поиск по имени
            2) Поиск по номеру''' # Три одиночные кавычки позволяют сохранять форматирование
            )
            if ans2=="1":
                name=input("Введите имя ")
                if name in a:
                    print ('Вы искали абонента {} с номером {}, верно?'.format(name,a[name]))
                else:
                    print ("К сожалению, такого человека в данной телефонной книге нет!")
            elif ans2=="2":
                number=input("Введите номер ")
                for i in a:
                    if a[i]==number:
                        print ('Вы искали абонента {} с номером {}, верно?'.format(i,a[i]))
            else:
                print ("К сожалению, такого номера в данной телефонной книге нет!")
        elif ans=="2":
            i=input("Введите имя контакта ")
            f=input("Введите номер контакта ")
            a[i]=f
            with open('a.pickle', 'wb') as f:    
                pickle.dump(a, f)
            print ("Контакт успешно создан!")
        elif ans=="3":
            while True:
                print ('''Введите имя контакта, который Вы хотите удалить или введите 'назад', чтобы 
вернуться в главное меню ''')
                delete=input()
                if delete in a: 
                    del a[delete]
                    print ("Контакт успешно удалён!")
                    with open('a.pickle', 'wb') as f:    
                        pickle.dump(a, f)
                    break
                elif delete=='назад':
                    break
                else:
                    continue
        elif ans=="4":
            print ("Спасибо за использование программы, сделанной Жевгением Чуранковым!")
            time.sleep(2) #После выведения надписи проходит 2 секунды перед закрытием программы.
            break #Выходит из главного цикла while
        elif ans=="5":
            print (a)
        else:
            print ("К сожалению, данный пункт меню не найден! Пожалуйста, введите цифры в промежутке от 1 до 4.")
            continue #Возвращаемся к началу цикла while
user_request ()
