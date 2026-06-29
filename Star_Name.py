

def l():
	for i in range(1, 13):
		ni = 19
		ni -= i
		mi = ("*"*(i+ni))
		if (i == 1 or i == 12 ):
			print(mi,end = '')
			print("")
		elif (i == 11):
				print("*"*3+" "*14+"*"*2,end ="")
				print("")
		else:
			print("*"*3+" "*3+"*"*13,end="")
			print("")
def e():
	for i in range(1, 13):
		ni = 19
		ni -= i
		mi = ("*"*(i+ni))
		if (i == 1 or i == 12 ):
			print(mi,end = '')
			print("")
		elif (i == 2 or i == 6 or i == 11):
				print("*"*3+" "*14+"*"*2,end ="")
				print("")
		else:
			print("*"*3+" "*2+"*"*14,end="")
			print("")
def v():
    rows = 12
    cols = 19    
    for i in range(1, rows + 1): 
        if i == 1 or i == 2 or i == 11 or i == 12:
            print("*" * cols)
        else:
            row = ""
            for j in range(cols):          
                if j == i - 1 or j == i or j == cols - i or j == cols - i -1:
                    row += " "
                else:
                    row += "*"
            print(row)
def a():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        n = 13
        n -= i
        if i in [1,2,11,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if  (j == i+6 or j == i +5) or (j == n-1) or (j == n-2) or (i in[8] and j in [7,8,9,10,11,12,6,5]) :
                    row += " "
                else: row += "*"
            print(row)
def b():
     for k in range(1, 13):
     	if k in[1,12]:
     		print("*"*19,end="")
     	elif k in[2,11,6]:
     		print("*"*2+" "*13+"*" *4,end = "")
     	else:
     		print("*"*2+" "*2+"*"*11+" "*2+"*"*2,end= "") 
     	print("")
def c():
     for k in range(1, 13):
     	if k in[1,12]:
     		print("*"*19,end="")
     	elif k in[2,11]:
     		print("*"*2+" "*15+"*"*2,end = "")
     	else:
     		print("*"*2+" "*3+"*"*15,end= "") 
     	print("")
def d():
     for k in range(1, 13):
     	if k in[1,12]:
     		print("*"*19,end="")
     	elif k in[2,11]:
     		print("*"*2+" "*13+"*"*4,end = "")
     	elif k in[3,10]:
     		print("*"*2+" "*2+"*"*10+" "*2+"*"*3,end= "")    	
     	else:
     		print("*"*2+" "*2+"*"*11+" "*2+"*"*2,end= "") 
     	print("")
def f():
     for k in range(1, 13):
     	if k in[1,2,12]:
     		print("*"*19,end="")
     	elif k in[2,3,6,]:
     		print("*"*1+" "*17+"*"*1,end = "")
     	else:
     		print("*"*1+" "*3+"*"*15,end = "")
     	print("")       	
def g():
	for k in range(1, 13):
		if k in[1,12,11]:
			print("*"*19,end ="")
		elif k in[2,10]:
			print("*"*1+" "*17+"*"*1,end = "")
		elif k in[4,5,3,]:
			print("*"*1+" "*2+"*"*16,end = "")
		elif k in[6]:
			print("*"*1+" "*2+"*"*7+" "*8+"*"*1,end = "")
		else:
			print("*"*1+" "*2+"*"*12+" "*3+"*"*1,end = "")
		print("")
def h():
     for k in range(1, 13):
     	if k in[1,2,11,12]:
     		print("*"*19,end="")
     	elif k in[3,4,5,7,8,9,10]:
     		print("*"*1+" "*2+"*"*13+" "*2+"*"*1,end = "")
     	else:
     		print("*"*1+" "*17+"*"*1,end = "")
     	print("")     	
def i():
     for k in range(1, 13):
     	if k in[1,12]:
     		print("*"*19,end="")
     	elif k in[2,11]:
     		print("*"*2+" "*15+"*"*2,end = "")
     	else:
     		print("*"*8+" "*3+"*"*8,end = "")
     	print("")
def j():
     for k in range(1, 13):
     	if k in[1,12]:
     		print("*"*19,end="")
     	elif k in[2]:
     		print("*"*2+" "*15+"*"*2,end = "")
     	elif k in[3,4,5,6,7,8,9]:
     		print("*"*9+" "*3+"*"*7,end= "")
     	elif k in[10]:
     		print("*"*3+" "*3+"*"*3+" "*3+"*"*7,end ='')
     	else:
     		print("*"*5+" " *5+"*"*9,end = "")
     	print("")
def x():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,11,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if  j == i+2 or j == i+3 or j == cols-i-3 or j == cols-i-2:
                    row += " "
                else: row += "*"
            print(row)
def m():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,11,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if j in [2,3,15,16] or j == i-1 or j == i or j == cols-i-1 or j == cols-i:
                    row += " "
                else: row += "*"
            print(row)
def n():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,11,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if j in [3,4] or j == i+2 or j == i+3 or j in[14,15]:
                    row += " "
                else: row += "*"
            print(row)
def o():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,11,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if j in [2,3,15,16] :
                    row += " "
                elif j in[3,4,5,6,7,8,9,10,11,12,13,14,15] and i in[3,10]:
                	row += " "
                else: row += "*"
            print(row)
def p():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if j in [2,3,4] :
                    row += " "
                elif j in[15,16,17] and i in[3,4,7,5,6]:
                	row += " "
                elif j in[5,6,7,8,9,10,11,12,13,14,15,16,17] and i in[3,7]:
                	row += " "
                else: row += "*"
            print(row)
def q():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if j in [1,2,15,14] and i != 11:
                    row += " "
                elif j in[3,4,5,6,7,8,9,10,11,12,13,14,15] and i in[3,10]:
                	row += " "
                elif (i in[8] and j in[8,9]) or (i in[9] and j in[10,9]):
                	row += " "
                elif i in[11] and j in[12,11]:
                	row += " "
                else: row += "*"
            print(row)
def r():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if j in [2,3,15,14,13] and i in [3,4,5,6,2]:
                    row += " "
                elif j in[4,5,6,7,8,9,10,11,12,13,14] and i in[2,6]:
                	row +=" "
                elif j in [2,3] and i in [7,8,9,10,11] or j == i -2 or j == i-1:
                	row += " "
                else: row += "*"
            print(row)
def s():
    rows, cols = 11, 19
    for i in range(1, rows + 1):
        if i in [1,2,11]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if (i in [3,6,9] and (j > 2 and j < 16)) or (i in[4,5] and j in[4,3,2]) or (i in[8,7] and j in[17,16,15]):
                    row += " "
                else: row += "*"
            print(row)
def t():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,11,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if (i in[3] and j > 1 and j < 17) or ((i > 3 and i < 11) and j in[9,10,8]):
                    row += " "
                else: row += "*"
            print(row)
def u():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,11,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if ((i > 2 and i < 9) and j in[2,4,14,3,16,15]) or (i in[10] and (j > 3 and j <15)) or (i in[9] and j in[3,4,5,13,14,15]):
                    row += " "
                else: row += "*"
            print(row)
def k():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        n = 17
        n -= i
        if i in [1,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if (i in[3] and j in[3,4,5,12,13]) or (i in [4] and j in [3,4,5,11,12]) or (i in[5] and j in[3,4,5,10,11]) or (i in[6] and j in[3,4,5,9,10]) or (i in[7] and j in[3,4,5,8,9]) or (i in[8] and j in[3,4,5,8,7,6]) or (i in[9] and j in[8,9,3,4,5]) or (i in[10] and j in[3,4,5,9,10]) or (i in[11] and j in[3,4,5,10,11]) :
                	row += " "
                else: row += "*"
            print(row)
def w():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,11,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if j in [2,3,16,15] or (i in[7,8,9,6,10] and j == i+4) or (i in[7,8,9,6,10] and j == i +3) or (i in[7,8,9,10,6] and j == 14-i) or (i in[7,8,9,10] and j == 15-i ) :
                    row += " "
                else: row += "*"
            print(row)
def y():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,2,11,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if i <= 6 and (j == i-1 or j == i or j == cols-i-1 or j == cols-i) or i > 6 and j in [8,9,10]:
                    row += " "
                else: row += "*"
            print(row)            
def z():
    rows, cols = 12, 19
    for i in range(1, rows + 1):
        if i in [1,12]: print("*" * cols)
        else:
            row = ""
            for j in range(cols):
                if (i in[2,11] and (j>2 and j<16)) or (i in[3,7,8,4,5,9,10,6] and (j == 15 - i or j == 16 -i or j == 14 - i)) :
                	row += " "
                else: row += "*"
            print (row)

print(f"     {("=")*31}\n        PYTHON-ASCII-NAME-PRINTER\n     {("=")*31}")
while True:
    name = input("Enter your name: ").strip().lower()

    if name and all(ch.isalpha() or ch.isspace() for ch in name):
        break

    print("Please enter a valid name (letters and spaces only).")

for letter in name:
    if letter == " ":
        print()
        continue

    globals()[letter]()
    print()



