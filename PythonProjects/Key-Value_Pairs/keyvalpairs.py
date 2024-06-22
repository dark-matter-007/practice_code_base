from art import *

tprint("Key Vals")
print("By Ashwin Sharma\n")


def clearScr():
    print("\n"*100)

def process_input(a):
    if a == 5:
        quit()

    if a == 1:
        key, value = input("\nEnter the key : "), input("Enter the value : ")
        file = open("KeyValPairsData.txt", "a")
        file.write(key + "," + value + "\n")
        file.close()
        a = input(f"\nThe given key value pair has been saved...\n:: PRESS ENTER TO CONTINUE ::")

    if a == 2:
        key = input("Enter the key to search : ")
        file = open("KeyValPairsData.txt", "r")
        Lines = file.readlines()
        collector, maxChars = [], int(0)
        for line in Lines:
            lineSplit = line.split(",")
            if len(lineSplit[0]) > maxChars:
                maxChars = len(lineSplit[0])
            if key.lower() in lineSplit[0].lower():
                collector.append(lineSplit)

        keystr = "key"
        if len(collector) != 0:
            if len(collector) > 1:
                print(f"\n{keystr:^{maxChars}}  ::   value")
                print("_" * 50)
                for line in collector:
                    print(f"{line[0] : ^{maxChars}}  ::  {line[1]}", end="")

            else:
                print(f"\n{keystr:^{len(collector[0][0])}}  ::   value")
                print("_" * 50)
                print(f"{collector[0][0]}  ::  {collector[0][1]}")

        else:
            print("No keys were found :(")

        useless = input("\nPress enter to continue...")

    if a == 3:
        try:
            file = open("KeyValPairsData.txt", "r")
            lines = file.readlines()
            key, lineCollector, maxChars = "key", [], int(0)
            for line in lines:
                lineSplit = line.split(",")
                lineCollector.append(lineSplit)
                if len(lineSplit[0]) > maxChars:
                    maxChars = len(lineSplit[0])
            print(f"\n{key:^{maxChars}}", "  ::   value")
            print ("_"*50 + "\n")
            for lineSplitt in lineCollector:
                print(f"{lineSplitt[0]:^{maxChars}}", "  ::  ", lineSplitt[1], end="")

        except Exception as E:
            print("Error opening file...\n")

        useless = input("\nPress enter to continue...")

    if a == 4:
        key = input("Enter the key to delete : ")
        file = open("KeyValPairsData.txt", "r")
        lines = file.readlines()
        file.close()
        writableFile = open("KeyValPairsData.txt", "w")
        collector = []
        for line in lines:
            lineSplit = line.split(",")
            if lineSplit[0] != key:
                collector.append(line)
        writableFile.writelines(collector)
        writableFile.close()
        print (f"Deleted the key - {key}\nThe remaining keys are as follows - \n")
        process_input(3)



def take_input():
    print("""
    1 : insert new pairs
    2 : search by key
    3 : show all pairs
    4 : delete a pair
    5 : exit""")

    a = int(input("\nYour choice here : "))
    clearScr()
    process_input(a)


clearScr()
while True:
    take_input()
    clearScr()
