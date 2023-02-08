# Condition Statements 
coldWeather=  ['Sweater','Jacket','Gloves','Socks','Earmuffs']
hotWeather=   ['Water Bottle','Sunglasses','Cap','Umbrella','Sunscreen']
coolWeather=  ['easy-breezy dress']
inputTemp=input(print('Enter temperature in your surrounding,in degree celsius'))
try:
   int(inputTemp)>100
except TypeError as e :
     print("Something went wrong")
if int(inputTemp) < 5 :
    print('It is freezing,better to stay at home')
elif 5 < int(inputTemp) and int(inputTemp) < 10:
     for i in coldWeather:
         print('It is cold outside, use ',i,'or')
elif 10 < int(inputTemp) and int(inputTemp) < 25:
     for i in coolWeather:
         print('It is a sunny day, use ',i)
elif 25 < int(inputTemp) and int(inputTemp) < 50:
     for i in hotWeather:
         print('It is a hot outside, use ',i)  
else:
  print("Something went wrong")
 
 
print("Have a GOOD DAY")
print(':)')





