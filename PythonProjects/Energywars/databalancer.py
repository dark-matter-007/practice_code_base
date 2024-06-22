import pickle
F = open ( 'datafile.bin', 'wb+')
score = '40'
pickle.dump(score, F)
F.close()
print ('dumped score')