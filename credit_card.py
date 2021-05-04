def hide_creditcard(card_numbers):
    cards_list = []
    for card_number in card_numbers:
        last_four = card_number[-4:]
        format_creditcard = f'**** **** **** {last_four}'
        cards_list.append(format_creditcard)
    return cards_list
random_creditcard = hide_creditcard(['123456789123456','7493010494294875'])
print(random_creditcard)