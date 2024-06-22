#   BY ASHWIN SHARMA

a, b ,c = input ("Enter space separated coefficients of x sq. , x and the constant, respectively : ").split(" ")
print ( " The roots of your equation are : ", "{:.2f}".format((-int(b) + (int(b)**2 - 4*int(a)*int(c))**(1/2)) / (2*int(a))), end="") 
print (" and ", "{:.2f}".format((-int(b) -  (int(b)**2 - 4*int(a)*int(c))**(1/2)) / (2*int(a))).format("{:.2f}"))