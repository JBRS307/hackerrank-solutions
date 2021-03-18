def findNearest(city, stations):
    stations.append(city)
    stations.sort()
    index = stations.index(city)
    if index-1 >= 0:
        left = stations[index-1]
    if index+1 < len(stations):
        right = stations[index+1]
    try:
        distLeft = city - left
    except:
        distLeft = float('inf')
    try:
        distRight = right - city
    except:
        distRight = float('inf')
    
    return min(distLeft, distRight)


def maxDistance(citiesQ, stations):
    cities = [i for i in range(citiesQ)]
    distances = set()
    for city in cities:
        if city in stations:
            distances.add(0)
        else:
            distances.add(findNearest(city, stations[:]))
    return max(distances)


#================================================================
citiesQ, _ = list(map(int, input().rstrip().split()))
stations = list(map(int, input().rstrip().split()))
stations.sort()
print(maxDistance(citiesQ, stations))