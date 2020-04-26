def get_num():
    """
    Получить число - компьютер загадывает число
    """
    import random
    A = ''

    while len(A) != 4:
        d = str(random.randint(0, 9))

        if d not in A:
            A+=d
        else:
            continue
    return A


def check_num(num_1, num_2, f):
    """
    Проверка числа, указанного пользователем
    """
    from termcolor import cprint

    for i in range(len(num_1)):
        if num_1[i] in num_2:
            if num_1[i] == num_2[i]:
                f['bulls'] += 1
            else:
                f['cows'] += 1
    return cprint(f, color = 'cyan')



def game(A):
    from termcolor import cprint, colored
    f = {'bulls': 0, 'cows': 0}
    B = None
    step = 0
    while f['bulls'] != 4:
        step += 1
        f = {'bulls': 0, 'cows': 0}
        cprint("Введите четырехзначное число", 'green')
        B = input('Ваше число - ')

        if len(B) != 4:
            text = colored('Введите четырехзначное число!', 'red', attrs=['reverse', 'blink'])
            print(text)

        elif B.isalpha():
            text = colored('Вы ввели не число!', 'red', attrs=['reverse', 'blink'])
            print(text)

        check_num(B, A, f)

    else:
        cprint('You WIN!!!', color='magenta')
        print(f"Шагов использовано - {step}")



























