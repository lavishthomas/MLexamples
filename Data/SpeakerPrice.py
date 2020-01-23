
# generate random integer values
from random import seed
from random import randint

f = open("Anit.csv", "w")
f.write("Name,Price,Watt\n")

x = range(100)
y = 0
for n in x:
    # print(n)
    y = ((n**5*2+n*10)/10 + randint(0, 2000)) ** .5
    z = n * 100 + randint(-2,4)
    # print(int(y))
    a = "Name," + str(int(y)) + "," + str(z) + "\n"
    f.write(a)
f.close()