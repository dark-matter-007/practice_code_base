# WAF that takes a string and a leter as arguements, returning a copy of that string with every instance of the indicated letter removed.

S = input (  " Enter a sentence : " )
L = 'abc'
while len (L) > 1 :
        L = input ( " Enter the letter to remove : " )
        if len (L) > 1 :
             print ("\nplease give an alphabet, not a phrase")

def remove_letter (sentence, letter) :
    sentence = sentence.split (letter)
    masterstr = ''
    for part in sentence :
        masterstr += part
    return masterstr

'''
there was an alternate to this...
we could simply do : sentence.replace(letter, "")
lekin exam wale to harami h na... kaatenge marks smartness pe
'''

print (remove_letter(S, L))