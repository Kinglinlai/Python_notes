on = True
while on == True:
    payload = float(input("please enter the payload mass"))
    jet_fuel = 0.72 * payload
    rocketfuel = (jet_fuel + payload) * 1.5
    total_mass = payload + jet_fuel +rocketfuel
    rapier_number = total_mass *0.133333
    print("payload = ",payload)
    print("jet fuel = ",jet_fuel)
    print("rocket fuel = ",rocketfuel)
    print("total mass = ",total_mass)
    print("rapier number = ",rapier_number)
    swi = input('continue?')
    if swi == 'n':
        on = False
    else:
        on = True
