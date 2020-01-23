# Create fake income/age clusters for N people in k clusters
# generate random integer values
from random import seed
from random import randint
import numpy as np
import decimal

f = open("LaptopPrice.csv", "w")
f.write("Price,Speed,Ram,HDD,Class\n")
Class = ['Personal', 'Business', 'Gaming']


def createClusteredData(N, k):
    pointsPerCluster = float(N)/k
    X = []
    y = []
    for i in range(k):
        Speed = i*5/k + 1 + np.random.uniform(1, .1)
        # np.random.uniform(1000, 32000)
        Ram = i*4000/k + 2000 + np.random.uniform(0, 500)
        HDD = np.random.uniform(1000, 2000)

        for j in range(int(pointsPerCluster)):
            SpeedI = round(np.random.normal(Speed, .7), 2)
            RamI = round(np.random.normal(Ram, 600))
            HDDI = round(np.random.normal(HDD, 300))
            PriceS = SpeedI*75
            PriceR = RamI/25
            PriceH = HDDI/15
            print('PriceS ' + str(PriceS) + ' PriceR ' +
                  str(PriceR) + ' PriceH ' + str(PriceH))
            Price = PriceH + PriceR + PriceS
            a = str(round(np.random.uniform(Price, 100), 2)) + ","\
                + str(SpeedI) + ","\
                + str(RamI) + ","\
                + str(HDDI) + "," \
                + str(Class[i]) + "\n"
            # print(a)
            f.write(a)
    return
createClusteredData(100, 3)
