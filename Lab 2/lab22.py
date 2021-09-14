#Create Miles per Gallon Variable
mpg = 32
#Create variables for conversions
LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

#Calculation
fuel_consumption = 100 / (mpg / LITRES_PER_GALLON * KMS_PER_MILE)

#print fuel_consumption
print(fuel_consumption)

x = type(mpg)
y = type(LITRES_PER_GALLON)
z = type(KMS_PER_MILE)
k = type(fuel_consumption)
print(x,y,z,k)