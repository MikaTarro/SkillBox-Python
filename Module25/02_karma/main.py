# TODO здесь писать код
import random

ENLIGHTENMENT_CARMA_LEVEL = 500


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    day = 0
    total_carma = 0
    while total_carma < ENLIGHTENMENT_CARMA_LEVEL:
        day += 1

        if random.randint(1, 10) == 1:
            dice = random.choice(['IamGodError', 'DrunkError', 'CarCrashError',
                                  'GluttonyError', 'DepressionError', 'SuicideError'])
            with open('karma.log', 'a', encoding='utf-8') as file:
                file.write(f'День: {day} Исключение: {dice}\n')
                try:
                    if dice == 'IamGodError':
                        raise IamGodError
                    elif dice == 'DrunkError':
                        raise DrunkError
                    elif dice == 'CarCrashError':
                        raise CarCrashError
                    elif dice == 'GluttonyError':
                        raise GluttonyError
                    elif dice == 'DepressionError':
                        raise DepressionError
                    else:
                        dice == 'SuicideError'
                        raise SuicideError

                except IamGodError:
                    print(f'День: {day} Исключение: {dice}')
                except DrunkError:
                    print(f'День: {day} Исключение: {dice}')
                except CarCrashError:
                    print(f'День: {day} Исключение: {dice}')
                except GluttonyError:
                    print(f'День: {day} Исключение: {dice}')
                except DepressionError:
                    print(f'День: {day} Исключение: {dice}')
                except SuicideError:
                    print(f'День: {day} Исключение: {dice}')

        else:
            carma = random.randint(1, 7)
            total_carma += carma
            print(f'День: {day} Выпало кармы: {carma} Всего кармы: {total_carma}')


one_day()