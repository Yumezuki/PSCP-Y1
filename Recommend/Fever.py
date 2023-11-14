"""Fever"""
 
def fever(temp):
    """Function"""
    if temp > 35 and temp < 38:
        print("No Fever")
    elif temp > 37 and temp < 39:
        print("Mild Fever")
    elif temp > 38 and temp < 40:
        print("High Fever")
    elif temp >= 40:
        print("Very High Fever")
 
fever(float(input()))