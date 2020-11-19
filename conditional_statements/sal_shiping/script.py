def ground_shiping(weight):
  if (weight <= 2):
    cost = weight * 1.50 + 20
    return cost
  elif (weight > 2) and (weight <= 6):
    cost = weight * 3.0 + 20
    return cost
  elif (weight > 6) and (weight <= 10):
    cost = weight * 4.0 + 20
    return cost
  else:
    cost = weight * 4.75 + 20
    return cost
print(ground_shiping(8.4))
premimum_ground_shiping = 125.00  
def drone_shiping(weight):
  if (weight <= 2):
    cost = weight * 4.50 + 0
    return cost
  elif (weight > 2) and (weight <= 6):
    cost = weight * 9.0 + 0
    return cost
  elif (weight > 6) and (weight <= 10):
    cost = weight * 12.0 + 0
    return cost
  else:
    cost = weight * 14.25 + 0
    return cost
print(drone_shiping(8.5))
def cheapest_method(weight):
  if (ground_shiping(weight) < drone_shiping(weight)) and (ground_shiping(weight) < premimum_ground_shiping):
    print("ground shiping is the cheapest")
    return ground_shiping(weight)
  elif (drone_shiping(weight) < premimum_ground_shiping):
    print("drone shipping is the cheapest")
    return drone_shiping(weight)
  else:
    print("premium_ground_shiping is the cheapest")
    return premimum_ground_shiping



print(cheapest_method(4.8))    
