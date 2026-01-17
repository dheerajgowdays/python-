# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list of months Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
def main():
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            date=input("Date: ")
            if "/" in date:
                m,d,y=date.split("/")
                m=int(m)
                d=int(d)
                y=int(y)
                if m<=12 and d<=31:
                    print(f"{y}-{m:02}-{d:02}")
                    break
                else:
                    continue
            elif "," in date:
                d1,y=date.split(',',1)
                ma,d=d1.split(" ")
                d=int(d)
                y=int(y)
                for i in months:
                    if i in date and d<=31:
                        m=int(months.index(i)) + 1
                        print(f"{y}-{m:02}-{d:02}")
                        break
                else:
                    continue
                break
            else:
                 continue
        except ValueError:
            continue
main()
