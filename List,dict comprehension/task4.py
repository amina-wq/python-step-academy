# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. 
# Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). 
# Программа должна вывести номер потерянной карточки.


def find_lost_card(n: int, cards: list[int]) -> int:
    for i in range(1, n+1):
        if i not in cards:
            return i

if __name__ == '__main__':
    num = int(input("Enter the amount of cards: "))
    print("Enter the cards that you have:")
    
    cards = []

    for i in range(num-1):
        cards.append(int(input()))

    print(find_lost_card(num, cards))
