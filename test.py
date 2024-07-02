
#global constant

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#collecting user input
def deposit():
    while True:
        amount = input("What would you like to deposit ? $")
        #check if amount is a number
        if amount.isdigit():
            #because by default it comes as a string so we have to convert it in integer
            amount = int(amount)


            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        else:
            print("Please enter a number. ")

    return amount

#how much do they want to bet

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")

        else:
            print("Please enter a valid number")

    return lines


#amount they want to bet on each line.

def get_bet():
    while True:
        bet = input("Enter a bet amount, how much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a valid number")

    return bet

        



#call the function
def main():
    balance = deposit()
    lines = get_number_of_lines()
    #we need to check the entered bet amount is in range of the deposit money
    
    bets = get_bet()

    total_bet = bets*lines
    print(f"you are betting ${bets} on {lines} line. Total bet is {total_bet}")


#call main function
main()
