
import os
def Search():
    name = str(input('Введите название по которому производить поиск '))
    name = name
    with open('Search.txt', 'w') as fill:
        for path, folders, files in os.walk('c://'):
            for file in files:
                for folder in folders:
                    piss_full = os.path.join(path)
                    print(folder, file,path)
                    piss_full = piss_full + file
                    if name in file or name in path or name in folder:
                        print("Найдено совпадение", piss_full)
                        fill.write(f' {piss_full},\n')
Search()
print("Оконченно")













# d1 = {'a':7, 'b':8, 'value':9}
# d2 = dict(c=7)
# d3 = dict.fromkeys([1,2,3,4,5], 'value')
#print(user['alex']['password'], user['egor']['password'], user['nikita']['password'])
# print(price['мясо'])
# print(price['хлеб'])
# print(price['картошка'])
# print(price['молоко'])
# d1['a'] = 8
# del d1['a']
# print(d1,d2,d3)
# def buy():
#     korzina = 0
#     while True:
#         print('В магазине есть данные товары ', price)
#         enter = input('Какой товар хотите купить? Товар/Никакой ')
#         if enter in price:
#             print('Данный товар стоит ', price[enter])
#             otvet = input('Хотите положить в корзину? Да/Нет ')
#             if otvet == 'Да' or otvet == 'да':
#                 print('Товар добавлен в корзину ')
#                 korzina += price[enter]
#                 print('Корзина стоит ', korzina)
#                 #price = price - price[enter]
#             elif otvet == 'Нет' or otvet == 'нет':
#                 print('Товар не добавлен в корзину ')
#                 continue
#         elif enter == 'Никакой' or enter == 'никакой':
#             print('К оплате ', korzina,)
#             break
#         else:
#             print('Такого товара нет ')
#     return korzina
# buy()
# print(d1.items())
# print(d1.keys())
# print(d1.values())
# # d1.update(d2)
# # print(d1['c'])
# if 'c' in d1:
#     d1['c']
# y = d1.get('c', 'value')
# print(y)
# t = d1.pop('a')
# print(t, d1)
