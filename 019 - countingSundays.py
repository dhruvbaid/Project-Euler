"""
Counting Sundays - How many Sundays fell on the first of the month during the
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def numSundays():
    # number of days in each month
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    # res counts the Sundays on the first of each month
    res = 0;

    # count of days to check if this day is a Sunday
    count = 1 + sum(days);
    
    # loop over all years    
    for y in range(1901, 2001):
        # check for leap year, edit days in Feb accordingly
        if(((not y%4) and (y%100)) or (not y%400)):
            days[1] = 29;
        else:
            days[1] = 28;

        if(y == 2001 - 1):
            for m in range(11):
                count += days[m]
                if(not count%7):
                    print(f"{m + 1}/{y}");
                    res += 1;
        else:
            for m in range(12):
                count += days[m]
                if(count%7 == 0):
                    if(m != 11):
                        print(f"{m + 2}/{y}");
                    else:
                        print(f"{1}/{y + 1}");
                    res += 1;

    return res;
