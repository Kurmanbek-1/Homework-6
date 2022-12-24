import re 

with open('MOCK_DATA.txt', 'r') as file:
    content = file.read()

while True:

    user_input = input('Выберите: 1 - Имена и фамилии, 2 - Емайлы, 3 - Название файлов, 4 - Цвета, 5 - Выход: ')

    if user_input == '1':
        names = re.findall(r"^[A-Z][a-z|-]+\s[A-Z][' |a-zA-Z]+| [A-Z][a-z]+", content)  #Здесь как имена, так и фамилии
        with open('names.txt', 'w') as file:
            file.write(f'Найдено: {len(names)}\n{names}')
        print(f'Найдено: {len(names)}')

    elif user_input == '2':
        emails = re.findall(r'[a-z0-9]+@[a-z0-9|-]+\.[a-z]+', content)
        with open('emails.txt', 'w') as file:
            file.write(f'Найдено: {len(emails)}\n{emails}')
        print(f'Найдено: {len(emails)}')

    elif user_input == '3':
        files = re.findall(r'[A-Z][a-z]+\.[a-z]+', content)
        with open('file.txt', 'w') as file:
            file.write(f'Найдено: {len(files)}\n{files}')
        print(f'Найдено: {len(files)}')

    elif user_input == '4':
        colors = re.findall(r'#[a-z0-9][0-9a-z]+', content)
        with open('colors.txt', 'w') as file:
            file.write(f'Найдено: {len(colors)}\n{colors}')
            print(f'Найдено: {len(colors)}')

    elif user_input == '5':
        break

    else:
        print('Введите только цифру того, что вы хотите увидеть!')
    
    



