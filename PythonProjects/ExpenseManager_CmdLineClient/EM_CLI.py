# Here's the program for implementing expense management, within the console


# ----------------------------------- IMPORTS -----------------------------------
import art, tabulate, csv


# ------------------------------------ FUNCTIONS --------------------------------------
def make_table_rows (input_number, its_function):
    print("Added an input table row")
    
    
def clear_scr () :
    print("\n"*100)
    
    
def launch_cash_out_input():
    # taking data input
    date = input ("Enter the date (dd mm yyyy) { leave empty if Today } : ")
    receipant = input("Enter the receipant : ")
    amount = float(input ("Enter the amount paid : "))
    purpose = input ("Enter the purpose of the expense : ")
    
    # data validation
    buffer = []
    buffer.extend([date[0:2].replace(" ",""), date[3:5].replace(" ",""), date[6:].replace(" ","")])
    date = buffer
        
    # writing the data
    f = open('cashOUTRecords.csv', 'a')
    writer = csv.writer(f)
    writer.writerow((date, receipant, amount, purpose))

def launch_cash_in_input():
    # taking data input
    date = input ("Enter the date (dd mm yyyy) { leave empty if Today } : ")
    amount = float(input ("Enter the amount received : "))
    purpose = input ("Enter the remarks for the same : ")
    
    
    # data validation
    
    buffer = []
    buffer.extend([date[0:2].replace(" ",""), date[3:5].replace(" ",""), date[6:].replace(" ","")])
    date = buffer
        
    
    # writing the data
    f = open('cashINRecords.csv', 'a')
    writer = csv.writer(f)
    writer.writerow((date, amount, purpose))
    
    
def see_cash_in_records():
    
    reader = csv.reader(open("CashINRecords.csv", "r").readlines())
    row_collector = []
    for row in reader:
        row_collector.append(row)
    print("Showing all Cash IN expenses...")
    print(tabulate.tabulate(row_collector, ["Date", "Amount", "Remarks"], "fancy_grid"))
    input("\nHit enter to continue...")
    
def see_cash_out_records():
    
    reader = csv.reader(open("cashOUTRecords.csv", "r").readlines())
    row_collector = []
    for row in reader:
        row_collector.append(row)
    print("Showing all Cash OUT expenses...")
    print(tabulate.tabulate(row_collector, ["Date", "Receipant", "Amount", "Remarks"], "fancy_grid"))
    input("\nHit enter to continue...")
    

def calculate_current_balance():
    print ("Calculating...")
    INReader = csv.reader(open("cashINRecords.csv", "r").readlines())
    OUTReader = csv.reader(open("cashOUTRecords.csv", "r").readlines())
    
    netWorth = 0
    for row in INReader:
        inputEntry = row[1]
        netWorth += float(inputEntry)
    for row in OUTReader:
        outputEntry = row[2]
        netWorth -= float(outputEntry)
    
    input(f"Your current balance is : {netWorth} \nPress any key to continue...")
        
    
# ---------------------------------- PROCEDURE ORIENTED CONTENT -----------------------------------
while True:
    clear_scr()
    art.tprint("EM  -  CLI")
    print("By :: Ashwin Sharma :: ")

    tabular_data = [
        [ "1", "Cash OUT"],
        [ "2", "Cash IN"],
        [ "3", "See Cash OUT records"],
        [ "4", "See Cash IN records"],
        [ "5", "See current balance"],
        [ "6", "Exit"]
    ]
    headers = [ "Input", "Action" ]

    print(tabulate.tabulate(tabular_data, headers, "fancy_grid"))   # this will list the inputs and their actions

    try :
        match (int(input("Enter your choice here :: "))):
            case (1):
                clear_scr()
                launch_cash_out_input()
                
            case(2):
                clear_scr()
                launch_cash_in_input()
                
            case(3):
                clear_scr()
                see_cash_out_records()
            
            case(4):
                clear_scr()
                see_cash_in_records()    
                
            case(5):
                clear_scr()
                calculate_current_balance()
                
            case(6):
                break
                
            case (_):
                input("Unknown Option...\n")
    
    except Exception as e:
        clear_scr()
        print(f"Error was : {e}")
        input("Invalid entry... Press enter to input again...")
        continue            
exit()