import sys

## Split lines by separator first
## Make everything lowercase
lower_year = 1753
upper_year = 3000
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct,' 'nov', 'dec']
long_months = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
short_months = ['apr', 'jun', 'sep', 'nov']
class Date:
    def __init__(self, day, month, year, line):
        self.line = line
        self.day = ''.join(day)
        self.month = ''.join(month)
        self.year = ''.join(year)

    def printDate(self):
        print(self.day + ' ' + self.month + ' ' + self.year)



    def validYear(self):
        try:
            int_year = int(self.year)
        except:
            return False
        if len(self.year) == 4:
            if int_year < lower_year or int_year > upper_year:
                return False
        elif len(self.year) != 2:
            return False
        return True

    def isLeapYear(self):
        int_year = int(self.year)
        if int_year % 4 == 0 and int_year % 100 == 0 and int_year % 400 == 0:
            return True
        return False

    def validMonth(self):
        if isInt(self.month):
            int_month = int(self.month)
            if int_month < 1 or int_month > 12:
                return False
        else:
            if self.month[0].isupper():
                if self.month[1:-1] != self.month.upper() or self.month[1:-1] != self.month.lower():
                    return False
                else:
                    self.month = self.month.lower()
            elif self.month != self.month.lower():
                return False

            if self.month not in months:
                return False

        return True

    def validDay(self):
        month_lower = self.month.lower()
        try:
            int_day = int(self.day)
        except:
            return False
        if int_day < 1 or int_day > 31:
            return False
        if month_lower in short_months:
            if month_lower == 'feb':
                if self.isLeapYear():
                    if int_day > 29:
                        return False
                elif int_day > 28:
                    return False
            elif int_day > 30:
                return False
        return True

    def validDate(self):
        if not self.validYear():
            printInvalid(self.line, "invalid-year")
            return False

        if len(self.year) == 2:
            int_year = int(self.year)
            if int_year > 49:
                int_year += 1900
            else:
                int_year += 2000
            self.year = str(int_year)
        if not self.validMonth():
            printInvalid(self.line, "invalid-month")
            return False
        if not self.validDay():
            printInvalid(self.line, "invalid-day")
            return False
        return True

def isInt(line):
    try:
        int(line)
        return True
    except:
        return False

def isLetter(character):
    alphabet = (97, 122)

    if ord(character) >= alphabet[0] and ord(character) <= alphabet[1]:
        return True
    else:
        return False

def isNumber(character):
    numbers = (48, 57)
    if ord(character) >= numbers[0] and ord(character) <= numbers[1]:
        return True
    else:
        return False

def isSeperator(character):
    seperators = ['-', '/', ' ']
    if character in seperators:
        return True
    else:
        return False

def isEndOfLine(character):
    if character == '\n':
        return True
    else:
        return False

def printInvalid(line, type):
    print(line[0:-1] + " - INVALID: " + type)



dates = []
for line in sys.stdin:
    line = line.lower()
    line_lower = line.lower()

    in_day = True
    in_month = False
    in_year = False
    day = []
    month = []
    year = []
    valid_date = True
    for i, letter in enumerate(line_lower):
        if in_day:
            if isSeperator(letter):
                if len(day) == 0:
                    continue
                else:
                    in_day = False
                    in_month = True
            elif isNumber(letter):
                day += letter
                if len(day) > 2:
                    printInvalid(line, "non-date")
                    break
                continue
            else:
                printInvalid(line, "non-date")
                valid_date = False
                break
        elif in_month:
            if isSeperator(letter):
                if len(month) == 0:
                    continue
                else:
                    in_month = False
                    in_year = True
            elif isNumber(letter):
                month += letter
                if len(month) > 3:
                    printInvalid(line, "non-date")
                    break
                continue
            elif isLetter(letter):
                month += line[i]
                if len(month) > 3:
                    printInvalid(line, "non-date")
                    break
                continue
            else:
                printInvalid(line, "non-date")
                valid_date = False

                break
        elif in_year:
            if isSeperator(letter):
                if len(year) == 0:
                    continue
                else:
                    in_year = False
            elif isNumber(letter):
                year += letter
                if len(year) > 4:
                    printInvalid(line, "non-date")
                    break
                continue
            else:
                if not isEndOfLine(letter):
                    printInvalid(line, "non_date")
                    valid_date = False

                    break
    if valid_date:
        date = Date(day, month, year, line)
        dates.append(date)
        date.printDate()
for date in dates:
    if date.validDate():
        date.printDate()
