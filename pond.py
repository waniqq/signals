print("Sire of pond")
print("-------------------")
width = input("Enter the width(meters)")
width = int(width)
length = float(input("enter the pond length(meters) :"))
depth = float(input("enter the pond depth(meters) :"))
area = width*length
volume = area*depth
print(volume, "cubic meters of water")
print("\n")

print("filling the pond")
print("-------------------")
second = float(input("Enter the liters per second: "))
hour = second * 3600
print(hour, "liters per hour")
day = 24*hour
#convert liters/day to cubics meters per day (m^3=1000L)
day = day/1000
print(day, "cubic meters per day")
'''
The number of days to fill the pond is the volume of the pond,divided by the water flow in one day.
'''
days = volume/day
#round the number to 2 decimal palces
days = round(days,2)
print("it will take", days, "days tp fill the pond")
