# import modules
import csv
import copy

# define a dictionary
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# use a for loop to iterate over the initital keys and values of the dictionary.
for key, value in myVehicle.items(): # identify items
    print("{} : {}".format(key,value))

print("-----")

# define an empty list to hold the car inventory
myInventoryList = []

# copy the CSV file into memory
with open('car_fleet.csv') as csvFile: # keep a file open while you read data
    csvReader = csv.reader(csvFile, delimiter=',') # read a file
    lineCount = 0  
    for row in csvReader: 
        if lineCount == 0: # if linecount is at 1st row
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  # lineCount = lineCount + 1
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

print("-----")

# print the car inventory
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
    print("-----")