def calcDist(citiesQ, cities):
    distances = [0]*citiesQ
    for i in range(citiesQ):
        if cities[i] != 1:
            if i == 0:
                distances[i] = 10**9
            else:
                distances[i] = distances[i-1]+1
    return distances
            

#================================================================
citiesQ, _ = list(map(int, input().rstrip().split()))
stations = list(map(int, input().rstrip().split()))
cities = [0]*citiesQ
for val in stations:
    cities[val] = 1

distLeft = calcDist(citiesQ, cities)
distRight = calcDist(citiesQ, cities[::-1])
distRight = distRight[::-1]

dist = set()
for i in range(citiesQ):
    dist.add(min(distLeft[i], distRight[i]))

print(max(dist))