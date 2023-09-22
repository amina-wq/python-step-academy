def find_missed_card(card_list: list):
    total_sum = (N * (N + 1)) // 2
    remaining_sum = sum(card_list)
    missing_card = total_sum - remaining_sum
    return missing_card


if __name__ == '__main__':
    N = int(input('Введите количество карточек: '))
    print('Введите имеющиеся карточки: ')
    card_list = []
    for _ in range(N - 1):
        card_list.append(int(input()))

    print(find_missed_card(card_list))