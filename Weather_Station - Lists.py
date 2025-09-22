#!/usr/bin/env python3
"""
Simple List Data Type Demo
Demonstrates list operations: adding, removing, and sorting
"""

def main():
    print("LIST DATA TYPE APPLICATION")
    print("=" * 40)
    
    # Create initial list of temperatures
    temperatures = [75, 82, 68, 91, 77]
    print(f"Original temperatures: {temperatures}")
    print(f"List length: {len(temperatures)}")
    
    print("\nADDING ELEMENTS:")
    # Add new temperature (required)
    new_temp = 85
    temperatures.append(new_temp)
    print(f"Added {new_temp}°F: {temperatures}")
    
    # Add multiple temperatures
    more_temps = [79, 73]
    temperatures.extend(more_temps)
    print(f"Added {more_temps}: {temperatures}")
    
    # Insert at specific position
    temperatures.insert(0, 70)
    print(f"Inserted 70°F at start: {temperatures}")
    
    print("\nREMOVING ELEMENTS:")
    # Remove temperatures above 90°F (required condition)
    print("Removing temperatures above 90°F...")
    original_length = len(temperatures)
    temperatures = [temp for temp in temperatures if temp <= 90]
    removed_count = original_length - len(temperatures)
    print(f"Removed {removed_count} high temperature(s)")
    print(f"After removal: {temperatures}")
    
    # Remove specific value
    if 68 in temperatures:
        temperatures.remove(68)
        print(f"Removed 68°F: {temperatures}")
    
    print("\nSORTING:")
    # Display before sorting (required)
    print(f"Before sorting: {temperatures}")
    
    # Sort ascending
    temperatures_asc = sorted(temperatures)
    print(f"Sorted ascending: {temperatures_asc}")
    
    # Sort descending  
    temperatures_desc = sorted(temperatures, reverse=True)
    print(f"Sorted descending: {temperatures_desc}")
    
    # Sort in place
    temperatures.sort()
    print(f"After in-place sort: {temperatures}")
    
    print("\nLIST OPERATIONS:")
    # List statistics
    total = sum(temperatures)
    average = total / len(temperatures)
    minimum = min(temperatures)
    maximum = max(temperatures)
    
    print(f"Total: {total}°F")
    print(f"Average: {average:.1f}°F")
    print(f"Min: {minimum}°F, Max: {maximum}°F")
    
    # List access
    print(f"First temperature: {temperatures[0]}°F")
    print(f"Last temperature: {temperatures[-1]}°F")
    print(f"Middle temperatures: {temperatures[1:-1]}")
    
    print(f"\nFinal list: {temperatures}")
    print(f"Final length: {len(temperatures)}")

if __name__ == "__main__":
    main()