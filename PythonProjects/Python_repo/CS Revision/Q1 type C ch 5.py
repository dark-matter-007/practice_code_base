# WAP that reads a test file and creates another file that is identical excelpt that every sequence of consecitive blank spaces is replaced by single space.

# make the text file
file = open ( "Temptext.txt", "w")
inptext = input ("Type anything relevant to you, ranging up to a few sentences including double spaces : ")
file.write (inptext)
file.close()

#read the text file and generate the corrected file

# read
inf = open ( "Temptext.txt", "r")
text = inf.read ()
#process
processedtext = text.replace("  ", " ")
#write to output file
ouf = open ( "Processed file.txt", "w")
ouf.write (processedtext)
print (f"I wrote // {processedtext} // to the file.")
ouf.close()