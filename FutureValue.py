# STUDENT: DUSTIN KABAN
# ID: T00663749
# COURSE: COMP 2211, ASSIGNMENT 1
# DATE: APRIL 04, 2021

def main():
    # Ask for the present value, monthly interest rate, and the months to compound
    present_value = float(input('Enter your accounts present value: '))
    monthly_rate = float(input('Enter the monthly interest rate as a decimal value: '))
    months = int(input('Enter amount of months the money will be left in the account: '))
    future_value = format(calculateFutureValue(present_value, monthly_rate, months), '.2f')
    print(future_value)


def calculateFutureValue(present_value, rate, months):
    # Return the future value given the values plugged into the formula
    return float(present_value * ((1 + rate) ** months))


main()
