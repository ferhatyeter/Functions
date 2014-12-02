
def output_symbols(integer,symbol):
    for counter in range(integer):
        print(symbol,end="")
        
integer = int(input("Please enter an integer: "))
symbol = input("Please enter a symbol: ")

output_symbols(integer,symbol)

