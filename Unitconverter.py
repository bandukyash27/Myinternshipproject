def unitCoverter(Value,from_unit,to_unit):
    if from_unit==to_unit:
        return Value
    if from_unit=="c" and to_unit=="f":
        return (Value*9/5)+32
    if from_unit=="f" and to_unit=="c":
        return (Value-32)*5/9
if __name__=="__main__":
    print("Welcome to the Unit Converter!")
    Value=float(input('Enter the temperature:'))
    from_unit=input("Enter the unit to convert from (c/f):").lower()
    to_unit=input("Enter the unit to convert to (c/f):").lower()
    result=unitCoverter(Value,from_unit,to_unit)
    print(f"{Value}{from_unit}is equal to {result:2f}{to_unit}")


 
    