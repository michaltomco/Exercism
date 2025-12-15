DAYS: tuple[str, ...] = (
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
)
GIFTS: tuple[str, ...] = (
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
)


def recite(start_verse: int, end_verse: int) -> list[str]:
    verses: list[str] = []

    for day in range(start_verse - 1, end_verse):
        day_name = DAYS[day]

        gifts_list = []
        for i in range(day, -1, -1):
            gift = GIFTS[i]
            if i == 0 and day > 0:
                gift = "and " + gift
            gifts_list.append(gift)

        verse = f"On the {day_name} day of Christmas my true love gave to me: {', '.join(gifts_list)}."
        verses.append(verse)

    return verses
