from datetime import date , datetime
import sys
import operator
import inflect
p = inflect.engine()  
class Time:
    minutes = 0
    def __init__(self,bod,day):
        self.bod = bod
        self.day = day
        self.minutes = Time.cal_time(bod,day) 
    @classmethod
    def cal_time(cls,bod,day):
        delta = operator.__sub__(day,bod)
        days = delta.days
        min = days * 24 * 60
        word = p.number_to_words(min, andword="").capitalize()
        return word  

def main():
    bod=input("Date Of Birth: ").replace("/","-")
    bod1 = get_bod(bod)
    print(bod1.minutes)

def get_bod(bod):
    try:
        bod = datetime.strptime(bod, "%Y-%m-%d").date()
        day = date.today()
        return Time(bod,day)
    except ValueError:
        print("Invalid Input")
        sys.exit(1)

if __name__ == "__main__":
    main()
