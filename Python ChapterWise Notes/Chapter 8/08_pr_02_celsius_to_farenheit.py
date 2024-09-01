def temp(celsius):
    farenheit = (celsius*(9/5))+32
    return farenheit
cel = int(input("Enter temperature in celsius\n"))
a = temp(cel)
print("Temperature in Farenheit is "+str(a))