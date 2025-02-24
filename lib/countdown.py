import time

def countdown(number):
    while number >= 1:
        print(f'{number} SECOND(S)!')
        number -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(number2):
    while number2 >= 1:
        time.sleep(1)
        print(f'{number2} SECOND(S)!')
        number2 -= 1
    print("HAPPY NEW YEAR!")