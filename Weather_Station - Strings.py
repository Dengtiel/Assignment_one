#!/usr/bin/env python3
"""
Simple String Data Type Demo
Demonstrates basic string operations and f-string formatting
"""

def main():
    print("STRING DATA TYPE APPLICATION")
    print("=" * 40)
    
    # Create string variables
    station_name = "Downtown Weather Station"
    location = "City Center"
    date = "2024-03-15"
    time = "14:30"
    
    print("BASIC STRINGS:")
    print(f"Station: {station_name}")
    print(f"Location: {location}")
    print(f"Date: {date}")
    print(f"Time: {time}")
    
    # Temperature data for string formatting
    temp_total = 385
    temp_count = 5
    temp_avg = temp_total / temp_count
    
    print("\nF-STRING FORMATTING:")
    # F-strings with totals and averages (required)
    total_report = f"Total temperature across {temp_count} sensors: {temp_total}°F"
    average_report = f"Average temperature reading: {temp_avg:.1f}°F"
    
    print(total_report)
    print(average_report)
    
    print("\nSTRING OPERATIONS:")
    # String concatenation
    full_location = location + ", " + station_name
    print(f"Full location: {full_location}")
    
    # String methods
    station_upper = station_name.upper()
    station_lower = station_name.lower()
    print(f"Uppercase: {station_upper}")
    print(f"Lowercase: {station_lower}")
    
    # String length
    name_length = len(station_name)
    print(f"Station name length: {name_length} characters")
    
    print("\nFORMATTED REPORT:")
    # Multi-line string with f-strings
    report = f"""
Weather Report
--------------
Station: {station_name}
Location: {location}
Date: {date} at {time}
Total Readings: {temp_total}°F
Average: {temp_avg:.1f}°F
Status: Active
    """
    print(report.strip())
    
    print("\nSTRING COMPARISON:")
    status1 = "Active"
    status2 = "ACTIVE"
    print(f"'{status1}' == '{status2}': {status1 == status2}")
    print(f"Case-insensitive match: {status1.lower() == status2.lower()}")

if __name__ == "__main__":
    main()