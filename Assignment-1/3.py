feet=float(input("Enter length in feet:"))
unit=int(input("Enter number coressponding to unit u want to convert(1-inches,2-yards,3-miles,4-millimeters,5-centimeters,5-meters,6-kilometers):"))
list=[feet*12,feet/3,feet/5280,feet*304.8,feet*30.48,feet*0.3048,feet*0.0003048]
list_2=['inches','yards','miles','millimeters','centimeters','meters','kilometers']

if unit in range(1,7):
    print(f"converted length {list[unit-1]} {list_2[unit-1]}")