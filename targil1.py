# START

low_rate = 0
medium_rate = 0
high_rate = 0
valid = 0

while True:
    rating = int(input("rating?"))

    if rating == -1:
        break

    if rating < 1 or rating > 5:
        continue

    valid += 1

    if rating == 1 or rating == 2:
        low_rate += 1
    elif rating == 3:
        medium_rate += 1
    else:
        high_rate += 1

print("Valid ratings:", valid)
print("Low (1-2):", low_rate)
print("Medium (3):", medium_rate)
print("High (4-5):", high_rate)

# STOP