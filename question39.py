def find_starting_pump(petrol_pumps):
    total_surplus, current_surplus = 0, 0
    start_index = 0

    for i, (petrol, distance) in enumerate(petrol_pumps):
        total_surplus += petrol - distance
        current_surplus += petrol - distance
        
        if current_surplus < 0:
            start_index = i + 1
            current_surplus = 0

    return start_index if total_surplus >= 0 else -1

# Example Usage
petrol_pumps = [(4, 6), (6, 5), (7, 3), (4, 5)]  # Each tuple (petrol, distance)
print("Starting Petrol Pump Index:", find_starting_pump(petrol_pumps))
