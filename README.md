Overview

This is a simple Python-based Cab Fare Calculator project that calculates the total ride fare based on:

Distance travelled
Vehicle type selected
Time of booking

The program also applies surge pricing during peak hours.

Features
Supports multiple vehicle categories
Calculates fare based on distance
Applies surge pricing during peak hours
Handles invalid vehicle types
Validates time input
Displays a detailed price receipt
Exception handling for invalid user input
Vehicle Fare Rates
Vehicle Type	Rate per KM
Economy	₹10
Premium	₹18
SUV	₹25
Surge Pricing

Surge pricing is applied during peak hours:

17:00 to 20:00

During these hours:

Fare is multiplied by 1.5x
Technologies Used
Python
Functions
Dictionary
Conditional Statements
Exception Handling
User Input Handling
Project Structure
cab_fare_calculator.py
How the Program Works
User enters:
Distance in kilometers
Vehicle type
Hour of booking
Program validates the inputs.

Base fare is calculated using:

distance × vehicle rate
If booking time is between 5 PM and 8 PM:
Surge pricing is applied.
Final fare is displayed in a formatted receipt.
Sample Output
Normal Fare
Enter distance(km): 10
Enter vehicle type(Economy,Premium,SUV): Economy
Enter hour(0-23): 14

=== PRICE RECEIPT ===
Vehicle Type : Economy
Distance (km): 10
Hour of Day: 14
Surge Applied: No
Total Fare: ₹ 100
Surge Pricing Example
Enter distance(km): 10
Enter vehicle type(Economy,Premium,SUV): SUV
Enter hour(0-23): 18

=== PRICE RECEIPT ===
Vehicle Type : SUV
Distance (km): 10
Hour of Day: 18
Surge Applied: Yes (1.5x)
Total Fare: ₹ 375
Invalid Vehicle Example
Status: Service Not Available
Code Explanation
rates Dictionary

Stores fare rates for different vehicle types.

rates = {
    "Economy": 10,
    "Premium": 18,
    "SUV": 25
}
calculate_fare() Function

This function:

Validates vehicle type
Checks valid hour input
Calculates base fare
Applies surge pricing
Returns final fare
Exception Handling

The try-except block prevents the program from crashing due to invalid inputs.

Example:

except:
    print("Invalid input! Please enter correct values.")
Concepts Used
Functions
Dictionaries
Input Validation
Conditional Logic
Exception Handling
Fare Calculation Logic
Future Improvements
Add GST calculation
Add discount coupons
Support online payment simulation
Generate booking ID
Store ride history
