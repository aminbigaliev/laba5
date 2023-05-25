def zdh1():
    import random
    a = [random.randint(1, 10) for i in range(5)]
    b = int(input('Введите число:'))
    if b in a:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
    print('Были загаданы числа:', a)


def zdh2():
    import random
    a = [random.randint(-10, 10) for i in range(15)]
    dup = [x for i, x in enumerate(a) if i != a.index(x)]
    print(a)
    print(dup)


def zdh3():
    a = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
    b = int(input('сколько выходных дней на неделе вы хотите?'))
    print('ваши выходные дни: ', a[-b:])
    print('ваши рабочие дни: ', a[:-b])


def zdh4():
    import random
    s = ["Бигалиев", "Гумерова", "Телятникова", "Назаренко", "Рахимов", "Шамбурова", "Шенфельд", "Тарнаева", "Жарко",
         "Ахмедов"]
    s1 = ["Павлова", "Денисов", "Куокканен", "Литвина", "Перцева", "Игнатьев", "Мунтян", "Ясюкевич", "Шабельская",
          "Григорчук"]
    s2 = random.sample(s, 5) + random.sample(s1, 5)
    r = len(s2)
    print("Первая группа", s)
    print("Вторая группа", s1)
    print("Команда", s2)
    print("Кол-во людей в команде", r)
    s2.sort()
    print("Команда по алфавиту", s2)
    if 'Иванов' in s2:
        k = s2.count('Иванов')
        print("Да, людей с фамилей Иванов в команде", k)
    else:
        print("Нет, Иванов не входит в команду")


zdh1()
zdh2()
zdh3()
zdh4()