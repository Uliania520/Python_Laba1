gh = '110'
while gh != '0':
    gh = str(input("Выберите номер задания от 1 до 6(для выхода нажмите 0)\n"))
    if gh == '1':
        s = 3
        p = 1
        for a in range(1, 501):
            if a % 2 != 0:
                p -= 1 / s
            if a % 2 == 0:
                p += 1 / s
            s += 2
        p *= 4
        print("Число пи =", p)

    if gh == '2':
        glas = 0
        sogl = 0
        probel = 0
        text = input("Введите текст или предложение\n")
        mass = ['а', 'у', 'е', 'ы', 'о', 'э', 'я', 'и', 'ю', 'ё',
                'А', 'У', 'Е', 'Ы', 'О', 'Э', 'Я', 'И', 'Ю', 'Ё']
        mass_sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л',
                     'м', 'н', 'п', 'р', 'с', 'т', 'ф',
                     'x', 'ч', 'ц', 'ш', 'щ', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л',
                     'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф',
                     'X', 'Ч', 'Ц', 'Ш', 'Щ']
        for i in text:
            if i == ' ':
                probel += 1
            if i in mass:
                glas += 1
            else:
                if i in mass_sogl:
                    sogl += 1
        print("Количество согласных: ", sogl)
        print("Количество гласных: ", glas)
        print("Количество слов: ", probel + 1)
        if sogl == glas:
            for i in text:
                if i in mass:
                    print(i, end=' ')
        print('\n')

    if gh == '3':
        list_3 = [1.34, 'qwerty', 12, 13, 16, 'Love', 'Python']
        num = []
        words = []
        for k in list_3:
            if type(k) == str:
                words.append(k)
            else:
                num.append(k)
        print("Список чисел: ", num)
        print("Список слов: ", words)
        sum = 0
        multiplication = 1
        for r in num:
            sum += r
            multiplication *= r
        print("Сумма: ", sum, "Произведение: ", multiplication)
        numm = num
        s = 0
        while s < 3:
            print(max(numm))
            numm.remove(max(numm))
            s += 1

    if gh == '4':
        my_dict = dict(key_1=500, key_2='hello',
                       key_3='my', key_4=1000,
                       key_5=120, key_6='python',
                       key_7=3, key_8=0)
        print("Словарь: ")
        print(my_dict.items())
        print("Исходные значения: ")
        print(my_dict.values())

        sorted_values_vozr = dict(sorted(my_dict.items(), key=lambda item: (isinstance(item[1], int), item[1])))
        # значения по возрастанию
        sorted_dict_descending = dict(
            sorted(my_dict.items(), key=lambda item: (isinstance(item[1], int), item[1]), reverse=True))
        # по убыванию
        print("По возрастанию:")
        print(sorted_values_vozr)
        print("По убыванию:")
        print(sorted_dict_descending)

    if gh == '6':
        elem_tuple = ([1, 2], [3, 4], {5: 6}, [7, 8], [9, 10])
        size_tuple = len(elem_tuple)
        # print(size_tuple)
        print("Первый элемент кортежа: ", elem_tuple[0])
        print("Последний элемент кортежа: ", elem_tuple[size_tuple - 1])

    if gh == '5':
        confectionery = {'торт Snickers': {'состав': ['шоколадный бисквит', 'соленая карамель', 'орехи', 'крем-чиз'],
                                           'цена': '1. 50 руб', 'количество': '2000'}, 'торт красный бархат': {'состав':
            [
                'красный бисквит',
                'крем-чиз'],
            'цена': '1.2 руб',
            'количество': '2100'},
                         'пироженное картошка': {'состав': ['печенье',
                                                            'масло сливочное', 'сгущенка', 'какао'], 'цена': '0.9 руб',
                                                 'количество': '1000'}}
        ch = 0
        while ch != '6':
            print("1. Просмотр описания")
            print("2. Просмотр цены")
            print("3. Просмотр количества")
            print("4. Всю информацию")
            print("5. Покупка")
            print("6. До свидания")
            ch = ''
            ch = input("Сделайте выбор!\n ")
            if ch not in ['1', '2', '3', '4', '5', '6']:
                print("Пожалуйста, введите корректный выбор (от 1 до 6).")
                continue
            if ch == '1':
                for key in confectionery.keys():
                    print(key, end=' ')
                    print(confectionery[key]['состав'])
            if ch == '2':
                for k in confectionery.keys():
                    print(k, end=' ')
                    print(confectionery[k]['цена'])
            if ch == '3':
                for e in confectionery.keys():
                    print(e, end=' ')
                    print(confectionery[e]['количество'])

            if ch == '4':
                for y in confectionery.keys():
                    print(y, end=' ')
                    print(confectionery[y]['состав'], confectionery[y]['цена'], confectionery[y]['количество'])

            if ch == '5':
                product_name = input("Введите название продукции: ")
                if product_name in confectionery:
                    try:
                        quantity_to_buy = int(input("Введите количество, которое вы хотите купить (в граммах): "))
                        if quantity_to_buy <= 0:
                            print("Пожалуйста, введите положительное количество.")
                            continue  # Перезапуск цикла
                        if quantity_to_buy <= int(confectionery[product_name]['количество']):
                            price_100g = float(
                                confectionery[product_name]['цена'].replace(' руб', '').replace(',', '.'))
                            # замена руб на пустоту и запятой на точку
                            total_price = (quantity_to_buy / 100) * price_100g
                            print(f"Вы выбрали {quantity_to_buy} грамм(а) {product_name}.")
                            print(f"Общая стоимость: {total_price:.2f} руб.")
                            confectionery[product_name]['количество'] = str(
                                int(confectionery[product_name]['количество']) - quantity_to_buy)
                        else:
                            print(f"Извините, недостаточное количество {product_name} на складе.")
                    except ValueError:
                        print("Пожалуйста, введите корректное количество (целое число).")
                else:
                    print(f"Продукт {product_name} не найден в меню.")

            if ch == '6':
                print("Вы вышли из программы!")


