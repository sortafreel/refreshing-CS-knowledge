cards = list(range(10, 100))
picked_cards = []

for card in cards:
    if any([x + card == 100 for x in picked_cards]):
        continue
    else:
        picked_cards.append(card)

print(len(picked_cards))