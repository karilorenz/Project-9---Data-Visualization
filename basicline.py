import matplotlib.pyplot as plt


# Lists of variables
years = [1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990,
         1995, 2000, 2005, 2010, 2015, 2020]
pops = [2773019936, 3034949748, 3339583597, 3700437046,
        4079480606, 4458003514, 4870921740, 5327231061,
        5744212979, 6143493823, 6541907027, 6956823603,
        7379797139, 7794798739]

urbanpop = [877008842, 1023945517, 1188469224, 1354215496,
            1538624994, 1754201029, 2007939063, 2290228096,
            2575505235, 2868307513, 3215905863, 3594868146,
            3981497663, 4378993944]

# Can add keyword args in plot method
plt.plot(years, pops, "--", color=(0/255, 26/255, 102/255, 80/100))
plt.plot(years, urbanpop, color=(128/255, 0/255, 0/255, 80/100))

# Add label
plt.ylabel("Population in Billions")
plt.xlabel("Population Growth by Year")

# Add Title
plt.title("World Popultaion Growth")

plt.show()