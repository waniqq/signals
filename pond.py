print("Sire of pond")
print("-------------------")


width = float(input("Enter pond width (meters):"))
length = float(input("Enter pond length (meters):"))
depth = float(input("Enter pond depth (meters):"))
print("\n")
print("Results")
print("------------------")
area = width * length
print("Surface area of the pond:" , area , "square meters")

volume = area * depth
print("Pond contains:" , volume , "cubic meters of water")

fish = int(volume * 2)
print("Number of fish" , fish , "fish")

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

#convert the numbers of days to full days plus extra hours
full_days = int(day)
part_day = full_days - days
hours = part_day * 24
print("it will take", full_days , "days", "+", hours, "hours to fill the pond")

#round the hours to two decimal places
hours = round(hours,2)
full_h = int(hours)
part_h = hours - full_h
min = part_h * 60

min = round(min,2)
full_m = int(min)
part_m = min - full_m
second = part_m * 60

second = round(second,2)
full_s = int(second)
part_s = second - full_s

#convert the number of hours to full hours plus minutes and seconds
print("it will take", full_days , "days", "+", full_h, "hours", "+", full_m, "mins",full_s, "sec", "to fill the pond")
print("\n")
print("-------------------")
