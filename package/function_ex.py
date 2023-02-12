
gearnumber = input()

def demo_function(gear):
    try:
        if int(gear)<0:
            return "Gear can not be negative"
        rpm = int(gear)*1000
    except ValueError:
        rpm = "Invalid gear"
    return rpm

# output = demo_function(gearnumber)

# print(output)

