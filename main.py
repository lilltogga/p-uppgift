import time
from car import *
####
def get_Inter(limit):
	while True:
		try:          
			val = int(input(": "))         
			if val <= limit and val >= 1:
				return val
			else:
				print("Invalid selection!")
		except:
			print("Invalid selection!")
####			
def write_status():
	file = open("log.txt","r")
	car_list = []
	info = file.readline()
	while info != "":
    attribute_list = []
		attribute_list = info.strip().split(",")
		car = Car(attribute_list[0], attribute_list[1], attribute_list[2])
		car_list.append(car)
		info = file.readline()
	file.close()
	for i in range(0, len(car_list)):
		print(str(car_list[i].namn) +" "+ str(car_list[i].reg_nr) + " "+str(car_list[i].storlek))
####
def top_menu():
	print("Welcome, please, access any of the correspondence below!")
	print("1: Checkin / Exit")
	print("2: Pay and exit")
	print("3: View history")
	print("4: Estimated payment ")
	print("5: Close.")
	select = get_Inter(5)
	return select
####
def checkin(parked_cars): 
	print("please, enter the information of your car")
	reg_nr = input("Vehicle registration plate (abc-123): ")
	name = input("Name and surename on drivers licence: ")
	print("Please choice the size of your vechical 1:small 2:medium 3:large")
	size = get_Inter(3)
	date = time.strftime("%Y/%m/%d-%H:%M:%S")
	if reg_nr not in parked_cars: # A currently parked car can not be added twise in possession of the default cause
		parked_cars[reg_nr] = Car(name,date,reg_nr,size)
		print("{} registerd a parking session at {} on the car {}".format(name,date,reg_nr))
####	
def save(parked_cars):
	log = open("file.txt", "w")
	for key, car in parked_cars.items():
		log.write("{} {}\n".format(key,car.reg_nr))
####
def pay_check():
	newDict = {}
	f = open('log.txt', 'r')
	line = f.readline()
	while line != "":
			splitLine = line.split()
			newDict[int(splitLine[0])] = ",".join(splitLine[1:])


################################## main_function ###################################
def main():
	parked_cars = {}
	selectionFunctions = [checkin]
	selectionFunctions[top_menu()-1](parked_cars)
	save(parked_cars)

main()

#### 1) ta sig in på specifik bil, aktuell-bil-variabel current-car-varibel // ccv
	while True:+=1
		print("{}: Exit".format(i)) 
		print("")
		
print("wekcome to the parking lot")

car_memory = open("file.txt", "r")  

car_list = [] 

	for line in car_memory:
		car_list.append(Car(*line.split()))
