import json

class Forecast:
    def __init__(self, name, temperature, rainfall):
        self.name = name
        self.rainfall = rainfall
        self.temperature = temperature

    def printForecast(self):
        print('The rainfall is %.2f\nThe temperature is %d' % (self.rainfall, self.temperature))

def main():
    rainfile = open('rainfall.json','r')
    rain_dict = json.load(rainfile)
    cities = []
    for i in rain_dict.keys():
        cities.append(Forecast(i, rain_dict[i][0], rain_dict[i][1]))
    max_temp_city = cities[0]
    min_temp_city = cities[0]
    rainfalls = []
    for i in cities:
        if i.temperature > max_temp_city.temperature:
            max_temp_city = i
        elif i.temperature < min_temp_city.temperature:
            min_temp_city = i
        rainfalls.append(i.rainfall)
    avg_rain = sum(rainfalls) / len(rainfalls)
    print(max_temp_city.name)
    max_temp_city.printForecast()
    print(min_temp_city.name)
    min_temp_city.printForecast()
    print('The average rainfall is ' + str(avg_rain))

main()
