numbers = list(range(1, 51))
picked_numbers = []

for number in numbers:
    if any([x*2 == number or x/2 == number for x in picked_numbers]):
        continue
    else:
        picked_numbers.append(number)

print(len(picked_numbers))
print(picked_numbers)