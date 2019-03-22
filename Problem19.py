# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.

# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

counter = 0

for years in range(1901, 2001, 1):
    for months in range(0, 12, 1):
        if years % 4 == 0 or years % 400 == 0 and months == 2:
            month[2] = 29
        else:
            month[2] = 28

        for days in range(1, month[months], 1):
            day = [
                "monday",
                "tuesday",
                "wednesday",
                "thursday",
                "friday",
                "saturday",
                "sunday",
            ]
            a = (14 - months) // 12
            y = years - a
            m = months + 12 * a - 2
            result = (
                ((days + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12)) % 7
            ) - 1
            if day[result] == "sunday" and days == 1:
                counter += 1

print(counter)
