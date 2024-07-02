#actuall run the slot machine
import random

#global constant

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#HOW MANY symbol are in each reel(col)

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines)

    
    return winnings, winning_lines



#generating the outcome of the slot machine

def get_slot_machine_spin(rows, cols, symbols):
    #randomly pick number of symbols
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

#we need to now generate values inside the columns
    columns = []
    for col in range(cols):
        column = []
        #this make a copy of all symbol list so we dont use or update the orignal
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns



def print_slot_machine(columns):
    #transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end="|")

            else:
                print(column[row], end="")

        print()



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
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a valid number")

    return bet

        
def game(balance):

    
    lines = get_number_of_lines()
    #we need to check the entered bet amount is in range of the deposit money
    while True:
        bets = get_bet()
        total_bet = bets*lines

        if total_bet > balance:
            print(f"You are not allowed to bet more than your deposit amount, that is $ {balance}")

        else:
            break
        
    print(f"you are betting ${bets} on {lines} line. Total bet is {total_bet}")


    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bets, symbol_value)
    print(f"You won ${winnings}." )
    print(f"you won on lines:", *winning_lines )

    return winnings - total_bet









#call the function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("press enter to spin (q to quit).")
        if answer == "q":
            break

        balance += game(balance)

    
    print("You are left with ${balance}")


#call main function
main()
