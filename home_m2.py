#Ввод словарей
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Пётр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

#Списки и кортежи из словарей
user_list = [user1,  user2, user3, user4]
user_list_org = (user1,  user2, user3, user4)
account_list = [account1, account2, account3, account4]
account_list_orig = (account1, account2, account3, account4)

#_____________________________________________________________________
#Ввод ключа для поиска информации по нему
ask_key = input('Введите ключ (name или account): ').lower()

#Проверка ключа и вывод данных из словаря по ключу
try:
    print(f"значение ключа {ask_key} для юзера 1 = {user1[ask_key]}")
    print(f"значение ключа {ask_key} для юзера 2 = {user2[ask_key]}")
    print(f"значение ключа {ask_key} для юзера 3 = {user3[ask_key]}")
    print(f"значение ключа {ask_key} для юзера 4 = {user4[ask_key]}")
except KeyError:
    print('Введённый ключ не найден')

#_____________________________________________________________________
#Ввод ключа для поиска информации по нему
ask_num = input('Введите порядковый номер : ')

#Вывод информации о пользователе в соответствии с его порядковым номером
try:
    info_user = user_list[int(ask_num) - 1]
    info_account = account_list[int(ask_num) - 1]
    print(f'Данные по юзеру №{ask_num} :')
    print(f"имя : {info_user['name']}")
    print(f"возраст : {info_user['age']}")
    print(f"логин : {info_account['login']}")
    print(f"пароль : {info_account['password']}")
except:
    print('Пользователь с указанным номером не найден')

#_____________________________________________________________________
#Ввод номера в словаре пользователя, для дальнейшей рабты с ним 
ask_last = input('Введите номер пользователя, которого нужно переместить в конец :')

#Перемещение пользователя в словаре и вывод результатов
element = user_list.pop(int(ask_last)-1)
print(element)
print(user_list_org)
#замудрённый код в ходе опытов, нужно было бы сделать user_list.append и print, 
# но решил оставить для опыта и разнообразия.
massage = f'{user_list} {element}'
print(massage)
user_list.append(element)

#_____________________________________________________________________
#Вычисление среднего возраста пользователей
#По уму бы делать через извлечения данных из словаря в зависимости от количества их в списке user_list
# но как это сделать на основе пройденного материала не сообразил
age_summ = f"{user1['age'] + user2['age'] + user3['age'] + user4['age']}"
aver_age = int(age_summ)/len(user_list)
print(f'Средний возраст всех юзеров : {aver_age}')

#end
