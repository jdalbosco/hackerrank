def truck_tour(petrol_pumps):
    n = len(petrol_pumps)
    gas_in_tank = 0
    
    for starting_index in range(n):
        valid_route = True
        gas_in_tank = 0

        for i in range(n):
            amount, distance_to_next = petrol_pumps[(starting_index+i) % n]
            gas_in_tank += amount - distance_to_next
            if gas_in_tank < 0:
                valid_route = False
                break

        if valid_route:
            return starting_index

    return -1