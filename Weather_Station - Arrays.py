#!/usr/bin/env python3
"""
Simple Array Data Type Demo
Demonstrates basic array operations with weather temperature data
"""

import array

def main():
    print("ARRAY DATA TYPE APPLICATION")
    print("=" * 40)
    
    # Create a regular list of temperatures
    temp_list = [75, 82, 68, 91, 77, 85, 79, 73]
    print(f"Temperature list: {temp_list}")
    
    # Create an array from the list
    temp_array = array.array('i', temp_list)  # 'i' = signed integer
    print(f"Temperature array: {temp_array.tolist()}")
    print(f"Array type: {temp_array.typecode}")
    
    print("\nCOMPARING SUMS:")
    # Calculate sum using list
    list_sum = sum(temp_list)
    print(f"List sum: {list_sum}°F")
    
    # Calculate sum using array
    array_sum = sum(temp_array)
    print(f"Array sum: {array_sum}°F")
    
    # Compare results
    print(f"Sums match: {list_sum == array_sum}")
    
    print("\nARRAY OPERATIONS:")
    # Add new temperature
    temp_array.append(88)
    print(f"After adding 88°F: {temp_array.tolist()}")
    
    # Insert temperature at beginning
    temp_array.insert(0, 70)
    print(f"After inserting 70°F at start: {temp_array.tolist()}")
    
    # Remove last temperature
    removed = temp_array.pop()
    print(f"Removed {removed}°F: {temp_array.tolist()}")
    
    print("\nFINAL RESULTS:")
    print(f"Final array: {temp_array.tolist()}")
    print(f"Array length: {len(temp_array)}")
    print(f"Final sum: {sum(temp_array)}°F")
    print(f"Average temp: {sum(temp_array) / len(temp_array):.1f}°F")

if __name__ == "__main__":
    main()