print("Fish pond model")
print("================================================")
width = float(input("Enter pond width (meters): "))
length = float(input("Enter pond length(meters): "))
depth = float(input("Enter pond depth(meters): "))
print("\n")
print("Results")
print("-------")
area = width*length
print("surface area of the ponf is", area, "square meters")

volume = area*depth
print(("Pond contains"), volume, "cubic meters")

fish = volume*2
print('Number of fish:', fish)
print("----------------------------------------------")
