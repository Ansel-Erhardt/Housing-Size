
age = 0
numCouples = 0
numBedrooms = 0 
numPrec = 0 
sex = 0
numHouseholds = 0
sumAdults = 0
kidM = 0
kidF = 0
kidYoung = 0
kidMRoom = 0
kidFRoom = 0
kidYoungRoom = 0
numNeeded = 0

# logic for sorting a person into what room type they will fill 
if age <= 10: 
    kidYoung = kidYoung + 1 
elif age <= 18:
    if sex == 1: 
        kidM = kidM + 1 
    if sex == 2: 
        kidF = kidF + 1
else: 
    sumAdults = sumAdults + 1 

if kidM > 0:
    kidMRoom = 1
if kidF > 0: 
    kidFRoom = 1
if kidYoung > 0: 
    kidYoungRoom = 1
     
     
# the actual math to determine the room stress for a household the standards are: 
# one room for each couple/single adult and one room for young kids and one for teen boys and another for teen girls 
numNeeded = sumAdults - numCouples + kidFRoom + kidMRoom + kidYoungRoom
roomStress = (numBedrooms/numNeeded) - 1 

