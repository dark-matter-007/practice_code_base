# Consider a scenario where a son eats five chocolates every day. The price of each chocolate 
# is different. His father pays the bill to the chocolate vendor at the end of every week. 
#  Develop a program that can generate the bills for the chocolates and send to the father. Also 
# state which loop will be used to solve this problem.

chocolateCostCounter, chocolateDump, DayCounter, netAmount = 0,[[], [], [], [], [], [], []],0, 0
currentCost =  int(input(f"Enter the cost of chocolate you are eating on day {DayCounter} : "))

while DayCounter < 7:
    chocolateCostCounter += currentCost
    print("\nEnter 0 if done for this day")
    currentCost =  int(input(f"Enter the cost of chocolate you are eating on day {DayCounter+1} : "))
    if currentCost == 0:
        DayCounter += 1
        print()
        if DayCounter != 7:
            continue
    chocolateDump[DayCounter-1].append(currentCost)
    
print (f"Sending bill to the father :", end="")
for element in chocolateDump:
    print(f"\n\nDay {chocolateDump.index(element)+1} : ")
    for i in element :
        print(i, end="  ")
        netAmount += i
        
print(f"Your net total for the week is : {netAmount}")
        