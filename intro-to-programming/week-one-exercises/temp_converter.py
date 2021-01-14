for i in range(3):
    inputFahrenheitString = input("Enter the temperature in Fahrenheit: ")
    tempInF = float(inputFahrenheitString)
    tempInC = (tempInF - 32) * (5/9)
    print("The temperature in Celsius is: ", tempInC, "degrees")
