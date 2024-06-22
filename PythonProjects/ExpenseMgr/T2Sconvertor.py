from gtts import gTTS
mytext = input("Enter the text : ")
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save( mytext +".mp3")
print ("saved the file")