import numpy as np
f = open("CarPrice.csv", "w")
f.write("ShowroomPrice,OnRoadPrice,Class\n")

# Create fake income/age clusters for N people in k clusters
Class = ['EcoFriendly', 'Economy', 'SUV', 'Luxury']

s = 0


def createClusteredData(N, k):
    pointsPerCluster = float(N)/k
    for i in range(k):
        if (i == 0):
            ShowroomPrice = np.random.uniform(60000.0, 100000.0)
            s = 2
        elif (i == 1):
            ShowroomPrice = np.random.uniform(30000.0, 60000.0)
            s = 20
        elif (i == 2):
            ShowroomPrice = np.random.uniform(40000.0, 70000.0)
            s = 25
        else:
            ShowroomPrice = np.random.uniform(50000.0, 100000.0)
            s = 32
        for j in range(int(pointsPerCluster)):
            OnRoadPrice = ShowroomPrice + 1000 + \
                s * np.random.uniform(1000.0, 2000.0)
            a = (str(round(np.random.normal(ShowroomPrice, 2000.0), 2)) + "," +
                 str(round(np.random.normal(OnRoadPrice, 2000.0), 2)) + "," + Class[i]) + "\n"
            f.write(a)
    return


createClusteredData(100, 4)
