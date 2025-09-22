#!/usr/bin/env python3
"""
Simple Dictionary Data Type Demo
Demonstrates dictionary operations: creating, updating, and deleting
"""

def main():
    print("DICTIONARY DATA TYPE APPLICATION")
    print("=" * 40)
    
    # Create list of weather station dictionaries
    stations = [
        {'id': 'S001', 'name': 'Downtown Station', 'value': 75.5},
        {'id': 'S002', 'name': 'Airport Station', 'value': 78.2},
        {'id': 'S003', 'name': 'Park Station', 'value': 82.1},
        {'id': 'S004', 'name': 'Harbor Station', 'value': 74.8}
    ]
    
    print("INITIAL STATIONS:")
    for station in stations:
        print(f"{station['id']}: {station['name']} - {station['value']}°F")
    
    print(f"\nTotal stations: {len(stations)}")
    
    print("\nUPDATING RECORD:")
    # Update one record (required)
    for station in stations:
        if station['id'] == 'S003':
            old_value = station['value']
            station['value'] = 85.7
            station['status'] = 'Updated'
            print(f"Updated {station['name']}: {old_value}°F → {station['value']}°F")
            break
    
    print("\nDELETING RECORD:")
    # Delete a record (required)
    station_to_delete = 'S002'
    stations_before = len(stations)
    stations = [s for s in stations if s['id'] != station_to_delete]
    stations_after = len(stations)
    
    print(f"Deleted station {station_to_delete}")
    print(f"Station count: {stations_before} → {stations_after}")
    
    print("\nCURRENT STATIONS:")
    for station in stations:
        print(f"{station['id']}: {station['name']} - {station['value']}°F")
        if 'status' in station:
            print(f"    Status: {station['status']}")
    
    print("\nCOMPUTING TOTALS:")
    # Compute total of 'value' field (required)
    total_temp = sum(station['value'] for station in stations)
    avg_temp = total_temp / len(stations)
    min_temp = min(station['value'] for station in stations)
    max_temp = max(station['value'] for station in stations)
    
    print(f"Total temperature: {total_temp:.1f}°F")
    print(f"Average temperature: {avg_temp:.1f}°F")
    print(f"Temperature range: {min_temp:.1f}°F - {max_temp:.1f}°F")
    
    print("\nDICTIONARY OPERATIONS:")
    # Dictionary access and manipulation
    first_station = stations[0]
    print(f"First station data: {first_station}")
    print(f"Station keys: {list(first_station.keys())}")
    print(f"Station values: {list(first_station.values())}")
    
    # Add new field to all stations
    for station in stations:
        station['active'] = True
    
    print(f"\nAfter adding 'active' field:")
    for station in stations:
        print(f"{station['id']}: Active = {station['active']}")
    
    print(f"\nFinal summary:")
    print(f"Active stations: {len(stations)}")
    print(f"Total temperature monitored: {total_temp:.1f}°F")

if __name__ == "__main__":
    main()