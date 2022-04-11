def main():
    distanceInKilometers = int(input("Please enter the distance in kilometers: ")) 
    show_miles(distanceInKilometers)


def show_miles(distanceToMiles):
    results = distanceToMiles * 0.6214
    print(results)
main()
