documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_name():
    number = input('Введите номер документа ')
    for data in documents:
        if data.get("number") == number:
            return data.get('name')
    return 'Документа с таким номером нет'


def get_shelf():
    number = input('Введите номер документа ')
    for key in directories:
        if number in directories.get(key):
            return f'Документ хранится на полке: {key}'
    return 'Документ не найден в базе.'


def get_list():
    for key, value in directories.items():
        for doc in documents:
            n, typ, owner = doc.get('number'), doc.get('type'), doc.get('name')
            if n in value and value is not None:
                result = f'№: {n}, тип: {typ}, владелец: {owner} полка хранения: {key}'
                print(result)


def add_shelf():
    shelf = input('Введите номер полки: ')
    if shelf not in directories:
        directories[shelf] = []
        print(f'Полка добавлена. Текущий перечень полок:{", ".join(list(directories.keys()))}')
    else:
        print(f'Такая полка уже существует. Текущий перечень полок: {", ".join(list(directories.keys()))}')


def del_shelf(shelf):
    a = directories.get(shelf)
    if len(a) == 0 or a is None:
        del directories[shelf]
        print(f'Полка удалена. Текущий перечень полок: {", ".join(list(directories.keys()))}')

    else:
        print(f'На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: {", ".join(list(directories.keys()))} ')


while True:
    comand = input('Введите название команды ')

    if comand == 'p':
        print(get_name())

    elif comand == 's':
        print(get_shelf())

    elif comand == 'l':
        get_list()

    elif comand == 'ads':
        add_shelf()
    elif comand == 'ds':
        shelf = input('Введите номер полки: ')
        del_shelf(shelf)
    elif comand == 'q':
        break
