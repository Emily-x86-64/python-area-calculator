print ("Starting the calculator...")

option = input("Enter C for Circle or T for Triangle: ")
if option == 'C':
  radius = float(input("Input radius: "))
  area = 3.14159 * radius**2
  print ("Area: %f" % area)
elif option == 'T':
  base = float(input("Enter base: "))
  height = float(input("Enter height: "))
  area = 0.5 * base * height
  print ("Area: %f" % area)
else:
  print ("You did not enter a valid shape")

print ("Exiting...")
