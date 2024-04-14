#Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
n = input()
nlist = list(n)
nlist.reverse()
q = int(''.join(map(str, nlist)))

print(q)


#Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
n =input() # исходная строка
reversed=''.join(reversed(n))
print(reversed)



# Создайте словарь содержащий данные о человеке.
# В качестве строковых ключей используйте его имя, возраст, пол, рост, вес, размер ноги.
Human = {'Name': 'Nikita',
  'age': 34,
  'pol': 'men',
  'height': 178,
  'weight': 85,
  'foot size': 43}

print(Human['Name'])
print(Human['age'])
print(Human['pol'])
print(Human['height'])
print(Human['weight'])
print(Human['foot size'])

#Добавьте в словарь ключ и значение размера ноги

Human['foot size'] = 44
print(Human)

del Human['age']


