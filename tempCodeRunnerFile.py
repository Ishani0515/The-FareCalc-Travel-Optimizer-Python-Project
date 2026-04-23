# FareCalc - Travel Optimizer

# 1. Dictionary Mapping
rates = {
    "Economy": 10,
    "Premium": 18,
    "SUV": 25
}

# 3. Function Definition
def calculate_fare(km, vehicle_type, hour):
    
    # 4. Error Handling (vehicle type)
    if vehicle_type not in rates:
        return "Service Not Available"
    
    # Handle invalid hour (your requirement)
    if hour < 0 or hour > 23:
        return "Invalid Hour"
    
    # Base fare
    base_fare = km * rates[vehicle_type]
    
    # 2. Surge Logic
    if 17 <= hour <= 20:
        surge = 1.5
    else:
        surge = 1
    
    final_fare = base_fare * surge
    return final_fare


# ---- USER INPUT ----
try:
    distance = float(input("Enter distance (km): "))
    vehicle_type = input("Enter vehicle type (Economy, Premium, SUV): ")
    hour = int(input("Enter hour (0-23): "))

    result = calculate_fare(distance, vehicle_type, hour)

    print("\n=== PRICE RECEIPT ===")

    if result == "Service Not Available":
        print("Vehicle Type:", vehicle_type)
        print("Status: Service Not Available")

    elif result == "Invalid Hour":
        print("Invalid hour! Please enter between 0 and 23.")

    else:
        print("Vehicle Type:", vehicle_type)
        print("Distance (km):", distance)
        print("Hour of Day:", hour)

        if 17 <= hour <= 20:
            print("Surge Applied: Yes (1.5x)")
        else:
            print("Surge Applied: No")

        print("Total Fare: ₹", result)

except:
    print("Invalid Input! Please enter correct values.")