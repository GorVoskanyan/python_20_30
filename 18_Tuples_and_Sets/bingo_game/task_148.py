"""
В данном упражнении мы напишем программу, выполняющую симуля
цию игры в лото с одной картой. Начните с генерирования списка из всех
возможных номеров для выпадения (от B1 до O75). После этого переме
шайте номера в хаотичном порядке, воспользовавшись функцией shuffle
из модуля random. Вытаскивайте по одному номеру из списка и зачерки
вайте номера, пока карточка не окажется выигравшей. Проведите 1000 си
муляций и выведите на экран минимальное, максимальное и среднее ко
личество извлечений номеров, требующееся для выигрыша. При решении
этой задачи вы можете воспользоваться функциями из упражнений 146
и 147.
"""
from random import shuffle
from time import sleep

from task_146 import generate_card, display_card
from task_147 import is_win


def game_main_loop(card: dict) -> None:
    box = list(range(1, 76))
    shuffle(box)
    print('Welcome'.center(25, '_'))
    display_card(card)

    while not is_win(card):
        lucky = box.pop()
        print(f'{lucky:^25}')
        for value in card.values():
            if lucky in value:
                value[value.index(lucky)] = 0
        display_card(card)
        sleep(2)

    print()
    print('Game Over!'.center(25))


if __name__ == '__main__':
    card = generate_card()
    game_main_loop(card)
