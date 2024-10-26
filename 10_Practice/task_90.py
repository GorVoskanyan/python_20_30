"""
Напишите программу, которая будет сама строить куплеты этой песенки.
В программе должна присутствовать функция для отображения одного
куплета. В качестве входного параметра она должна принимать порядковый номер дня,
а в качестве результата возвращать готовый куплет. Далее
в основной программе эта функция должна быть вызвана 12 раз подряд.
Каждая строка с очередным подарком должна присутствовать в вашей
программе лишь раз, за исключением строки «A partridge in a pear tree».
В этом случае вы можете отдельно хранить такой вид строки для первого
куплета и слегка измененный («And a partridge in a pear tree») – для всех
последующих. Импортируйте свою функцию из упражнения 89 для выполнения этого задания.
"""

from task_89 import int_to_numeral

def create_couplet(day):
    first_line = 'On the ' + int_to_numeral(day) + ' day of Christmas my true love gave to me\n'
    last_line = 'a partridge in a pear tree.' if day == 1 else 'and a partridge in a pear tree.'

    one = first_line + last_line
    two = "Two turtle doves and\n" + last_line
    three = "Three french hens\n" + two
    four = "Four calling birds\n" + three
    five = "Five golden rings\n" + four
    six = "Six geese a-laying\n" + five
    seven = "Seven swans a-swimming\n" + six
    eight = "Eight maids a-milking\n" + seven
    nine = "Nine ladies dancing\n" + eight
    ten = "Ten lords a-leaping\n" + nine
    eleven = "Eleven pipers piping\n" + ten
    twelve = "Twelve drummers drumming\n" + eleven

    if day == 1:
        return one
    elif day == 2:
        return first_line + two
    elif day == 3:
        return first_line + three
    elif day == 4:
        return first_line + four
    elif day == 5:
        return first_line + five
    elif day == 6:
        return first_line + six
    elif day == 7:
        return first_line + seven
    elif day == 8:
        return first_line + eight
    elif day == 9:
        return first_line + nine
    elif day == 10:
        return first_line + ten
    elif day == 11:
        return first_line + eleven
    elif day == 12:
        return first_line + twelve


if __name__ == '__main__':
    for day in range(1, 13):
        couplet = create_couplet(day)
        print(couplet)
        print()
