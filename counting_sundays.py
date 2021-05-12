def next_day(curr_day,days):
    if days % 7 == 0 :
        return curr_day
    else:
        return (curr_day + days % 7 )%7

if __name__ == "__main__":
    year = 1900
    count = 0
    day = 0
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = next_day(day,sum(months))
    year += 1
    while year < 2001 :
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
            months[1] == 29
        for month in months :
            day = next_day(day,month)
            if day == 6:
                count += 1
        year += 1
    print(count)