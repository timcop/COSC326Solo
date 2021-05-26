import sys


lower_year = 1753 #minimum year
upper_year = 3000 #maximum year
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'] #all months
long_months = ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']
short_months = ['feb', 'apr', 'jun', 'sep', 'nov']

## Date class which has numerous methods to validate a date, and print method
# to be called on valid dates.
class Date:

    def __init__(self, day, month, year, line):
        self.line = line #Store the original line read in by the user
        self.day = ''.join(day)
        self.month = ''.join(month)
        self.year = ''.join(year)

    # Print a valid date
    def printDate(self):
        self.day = int(self.day)
        if self.day < 10:
            self.day = '0' + str(self.day)
        else:
            self.day = str(self.day)
        self.month = self.month[0].upper() + self.month[1:]
        print(self.day + " " + self.month + " " + self.year)

    # Determines whether a year is valid, returns true or false.
    def validYear(self):
        try:
            int_year = int(self.year)
        except:
            printInvalid(self.line, "Year not a number")
            return False
        if len(self.year) == 4:
            if int_year < lower_year or int_year > upper_year:
                printInvalid(self.line, "Year out of range")
                return False
        elif len(self.year) != 2:
            printInvalid(self.line, "Year has to be either 2 or 4 numbers")
            return False
        return True

    # Determines whether a valid year is a leap year
    def isLeapYear(self):
        int_year = int(self.year)
        if int_year % 4 == 0:
            if int_year % 100 == 0:
                if int_year % 400 == 0:
                    return True
                return False
            return True
        return False

    # Determines if month is valid
    def validMonth(self):
        if isInt(self.month):
            int_month = int(self.month)
            if int_month < 1 or int_month > 12:
                printInvalid(self.line, "Month number out of range")
                return False
            #Convert month to string
            self.month = months[int_month-1]

        else:
            if self.month[0].isupper():
                if self.month[1:] != self.month[1:].upper() and self.month[1:] != self.month[1:].lower():
                    printInvalid(self.line, "Incorrect capitilsation")
                    return False
                else:
                    self.month = self.month.lower()
            elif self.month != self.month.lower():
                printInvalid(self.line, "Incorrect capitilsation")
                return False
            if self.month not in months:
                printInvalid(self.line, "String is not a month")
                return False
        return True

    # Determines if day is valid
    def validDay(self):
        month_lower = self.month.lower()
        try:
            int_day = int(self.day)
        except:
            printInvalid(self.line, "Day is not an integer")
            return False
        if int_day < 1 or int_day > 31:
            printInvalid(self.line, "Day out of range")
            return False
        if month_lower in short_months:
            if month_lower == 'feb':
                if self.isLeapYear():
                    if int_day > 29:
                        printInvalid(self.line, "Day out of range")
                        return False
                elif int_day > 28:
                    printInvalid(self.line, "Day out of range")
                    return False
            elif int_day > 30:
                printInvalid(self.line, "Day out of range")
                return False
        return True

    # This is called on a date and returns whether it is valid or not.
    def validDate(self):
        if not self.validYear():
            return False
        if len(self.year) == 2:
            int_year = int(self.year)
            if int_year > 49:
                int_year += 1900
            else:
                int_year += 2000
            self.year = str(int_year)
        if not self.validMonth():
            return False
        if not self.validDay():
            return False
        return True

# Returns whether the input string is an int
def isInt(line):
    try:
        int(line)
        return True
    except:
        return False

# Determines whether a character is a lower case letter
def isLetter(character):
    alphabet = (97, 122)

    if ord(character) >= alphabet[0] and ord(character) <= alphabet[1]:
        return True
    else:
        return False
# Determines whether a character is a number from 0-9
def isNumber(character):
    numbers = (48, 57)
    if ord(character) >= numbers[0] and ord(character) <= numbers[1]:
        return True
    else:
        return False

# Determines whether a character is an allowed seperator
def isSeperator(character):
    seperators = ['-', '/', ' ']
    if character in seperators:
        return True
    else:
        return False

# Determines whether a character is an end of line character
def isEndOfLine(character):
    if character == '\n':
        return True
    else:
        return False

# Prints the invalid date as well as error message
def printInvalid(line, type):
    print(line[0:-1] + " - INVALID: " + type)

## INPUT
dates = []
for line in sys.stdin:
    if not line.isspace():
        line_lower = line.lower()
        in_day = True
        in_month = False
        in_year = False
        day = []
        month = []
        year = []
        valid_date = True
        current_seperator = []
        for i, letter in enumerate(line_lower):
            if in_day:
                if isSeperator(letter):
                    if len(current_seperator) == 0:
                        current_seperator.append(letter)
                    if letter not in current_seperator:
                        printInvalid(line, "Incorrect Seperation")
                        valid_date = False
                        break
                    if len(day) == 0:
                        printInvalid(line, "Incorrect Seperation")
                        valid_date = False
                        break
                    else:
                        in_day = False
                        in_month = True
                elif isNumber(letter):
                    day += letter
                    if len(day) > 2:
                        printInvalid(line, "Too many characters for day")
                        valid_date = False
                        break
                    continue
                else:
                    printInvalid(line, "Not a day")
                    valid_date = False
                    break
            elif in_month:
                if isSeperator(letter):
                    if letter not in current_seperator:
                        printInvalid(line, "Incorrect Seperation")
                        valid_date = False
                        break
                    if len(month) == 0:
                        printInvalid(line, "Incorrect Seperation")
                        valid_date = False
                        break
                    else:
                        in_month = False
                        in_year = True
                elif isNumber(letter):
                    month += letter
                    if len(month) > 2:
                        printInvalid(line, "Too many characters for month")
                        valid_date = False
                        break
                    continue
                elif isLetter(letter):
                    month += line[i]
                    if len(month) > 3:
                        printInvalid(line, "Too many characters for month")
                        valid_date = False
                        break
                    continue
                else:
                    printInvalid(line, "Not a month")
                    valid_date = False
                    break
            elif in_year:
                if isSeperator(letter):
                    printInvalid(line, "Error, seperator encountered after year")
                    valid_date = False
                    break
                    # if letter not in current_seperator:
                    #     printInvalid(line, "Incorrect Seperation")
                    #     valid_date = False
                    #     break
                    # if len(year) == 0:
                    #     printInvalid(line, "Incorrect Seperation")
                    #     valid_date = False
                    #     break
                    # else:
                    #     in_year = False
                elif isNumber(letter):
                    year += letter
                    if len(year) > 4:
                        printInvalid(line, "Too many characters for year")
                        valid_date = False
                        break
                    continue
                else:
                    if not isEndOfLine(letter):
                        printInvalid(line, "Not a year")
                        valid_date = False
                        break
        if len(year) != 2 and len(year) != 4 and valid_date:
            printInvalid(line, "Year has to be either 2 or 4 numbers")
            valid_date = False

        if valid_date:
            date = Date(day, month, year, line)
            dates.append(date)
            if date.validDate():
                date.printDate()
