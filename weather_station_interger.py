#!/usr/bin/env python3
"""
Simple Integer Data Type Demo
Demonstrates basic integer operations with weather data
"""

def main():
    print("INTEGER DATA TYPE APPLICATION")
    print("=" * 40)
    
    # Create integer temperature readings
    temp1 = 75
    temp2 = 82
    temp3 = 68
    temp4 = 91
    temp5 = 77
    
    print(f"Temperature readings:")
    print(f"Sensor 1: {temp1}°F")
    print(f"Sensor 2: {temp2}°F") 
    print(f"Sensor 3: {temp3}°F")
    print(f"Sensor 4: {temp4}°F")
    print(f"Sensor 5: {temp5}°F")
    
    print("\nCOMPUTATIONS:")
    # Calculate total
    total = temp1 + temp2 + temp3 + temp4 + temp5
    print(f"Total: {total}°F")
    
    # Calculate average
    count = 5
    average = total // count  # Integer division
    print(f"Average: {average}°F")
    
    # Find minimum and maximum
    minimum = min(temp1, temp2, temp3, temp4, temp5)
    maximum = max(temp1, temp2, temp3, temp4, temp5)
    print(f"Minimum: {minimum}°F")
    print(f"Maximum: {maximum}°F")
    
    # Calculate range
    range_temp = maximum - minimum
    print(f"Range: {range_temp}°F")
    
    print("\nCATEGORIES:")
    # Count temperatures by category
    hot_count = 0
    warm_count = 0
    cool_count = 0
    
    for temp in [temp1, temp2, temp3, temp4, temp5]:
        if temp >= 80:
            hot_count += 1
        elif temp >= 70:
            warm_count += 1
        else:
            cool_count += 1
    
    print(f"Hot (≥80°F): {hot_count} readings")
    print(f"Warm (70-79°F): {warm_count} readings") 
    print(f"Cool (<70°F): {cool_count} readings")
    
    print(f"\nTotal sensors: {hot_count + warm_count + cool_count}")

if __name__ == "__main__":
    main()