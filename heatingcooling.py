def heating_cooling(actual_temp, desired_temp):
    while not actual_temp == desired_temp:
        # while True:
        if actual_temp > desired_temp:
            print("Run A/C")
            # actual_temp = actual_temp - 1
            actual_temp -= 1
            print(actual_temp)
        elif actual_temp < desired_temp:
            print("Run heat")
            actual_temp += 1
            print(actual_temp)

    print("Standby")


# Call your function several times with different parameters in order to test it out -
# print(heating_cooling(actual_temp=50, desired_temp=65))
# print(heating_cooling(actual_temp=80, desired_temp=65))
# print(heating_cooling(actual_temp=68, desired_temp=68))

# Prompt the user for actual and desired temperatures and use their inputs to call the function again -
actual_temp = int(input("What is the temperature?"))
desired_temp = int(input("What is the desired temperature?"))

heating_cooling(actual_temp, desired_temp)
