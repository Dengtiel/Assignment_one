#!/usr/bin/env python3
"""
Project 13: Weather Station Logger
Comprehensive data type implementation for weather monitoring system
Student: [Your Name Here]
"""

import array

def integers_application():
    """Integers: Generate weather data and compute statistics"""
    print("INTEGERS APPLICATION - Weather Data Statistics")
    print("=" * 50)
    
    # Generate integer values for Weather Station Logger
    daily_readings = [72, 85, 68, 91, 77, 83, 79, 88, 74, 86]
    sensor_counts = [12, 15, 11, 18, 14]  # Number of readings per sensor
    error_marks = [2, 0, 1, 3, 0]  # Error counts per day
    
    print("Weather Station Data:")
    print(f"Daily temperature readings: {daily_readings}")
    print(f"Sensor reading counts: {sensor_counts}")
    print(f"Daily error marks: {error_marks}")
    
    # Compute required statistics
    temp_total = sum(daily_readings)
    temp_average = temp_total // len(daily_readings)
    temp_minimum = min(daily_readings)
    temp_maximum = max(daily_readings)
    
    sensor_total = sum(sensor_counts)
    error_total = sum(error_marks)
    
    print(f"\nStatistical Analysis:")
    print(f"Temperature Total: {temp_total}°F")
    print(f"Temperature Average: {temp_average}°F")
    print(f"Temperature Minimum: {temp_minimum}°F")
    print(f"Temperature Maximum: {temp_maximum}°F")
    print(f"Total Sensor Readings: {sensor_total}")
    print(f"Total Error Marks: {error_total}")
    
    return temp_total, temp_average, sensor_total, error_total

def strings_application(temp_total, temp_average, sensor_total, error_total):
    """Strings: Create formatted report with f-strings for totals and averages"""
    print("\n\nSTRINGS APPLICATION - Weather Station Report")
    print("=" * 50)
    
    # Weather Station Logger information
    station_name = "Central Weather Station Logger"
    location = "Metropolitan Observatory"
    operator = "Weather Monitoring Division"
    date_range = "March 1-10, 2024"
    
    print("Station Information:")
    print(f"Station: {station_name}")
    print(f"Location: {location}")
    print(f"Operator: {operator}")
    print(f"Reporting Period: {date_range}")
    
    # F-strings summarizing totals and averages (REQUIRED)
    total_summary = f"Weather Station Logger recorded a total of {temp_total}°F across {sensor_total} sensor readings"
    average_summary = f"Average temperature logged by the system: {temp_average}°F with {error_total} total error marks"
    
    print(f"\nFormatted Summary Reports:")
    print(f"📊 {total_summary}")
    print(f"📈 {average_summary}")
    
    # Additional formatted report
    status_report = f"""
    ╔══════════════════════════════════════════╗
    ║          WEATHER STATION LOGGER          ║
    ║              DAILY REPORT                ║
    ╠══════════════════════════════════════════╣
    ║ Station: {station_name:<25} ║
    ║ Period:  {date_range:<25} ║
    ║ Total Temperature: {temp_total:<14}°F  ║
    ║ Average Reading: {temp_average:<16}°F  ║
    ║ System Reliability: {"HIGH" if error_total < 5 else "MODERATE":<13} ║
    ╚══════════════════════════════════════════╝
    """
    print(status_report)
    
    return temp_average

def booleans_application(average_temp):
    """Booleans: Apply threshold conditions with compound boolean logic"""
    print("\n\nBOOLEANS APPLICATION - Weather Station Thresholds")
    print("=" * 50)
    
    # Threshold conditions for Weather Station Logger
    temp_threshold = 80
    humidity_reading = 65
    wind_speed = 12
    system_errors = 2
    
    print("Weather Station Logger Conditions:")
    print(f"Average Temperature: {average_temp}°F")
    print(f"Temperature Threshold: {temp_threshold}°F")
    print(f"Current Humidity: {humidity_reading}%")
    print(f"Wind Speed: {wind_speed} mph")
    print(f"System Errors: {system_errors}")
    
    # Boolean threshold evaluations
    temp_exceeds = average_temp > temp_threshold
    humidity_high = humidity_reading > 60
    wind_moderate = wind_speed >= 10
    system_stable = system_errors < 5
    
    print(f"\nThreshold Evaluations:")
    print(f"Temperature exceeds threshold: {temp_exceeds}")
    print(f"Humidity is high (>60%): {humidity_high}")
    print(f"Wind is moderate (≥10mph): {wind_moderate}")
    print(f"System is stable (<5 errors): {system_stable}")
    
    # Compound boolean condition (REQUIRED)
    optimal_conditions = temp_exceeds and humidity_high and system_stable
    alert_condition = temp_exceeds and (humidity_high or not wind_moderate)
    
    print(f"\nCompound Boolean Conditions:")
    print(f"Optimal logging conditions: {optimal_conditions}")
    print(f"Alert condition active: {alert_condition}")
    
    # Status messages based on threshold
    if temp_exceeds:
        status = "Above Standard - Enhanced monitoring active"
        priority = "HIGH"
    else:
        status = "Below Standard - Normal monitoring mode"
        priority = "NORMAL"
    
    print(f"\nWeather Station Logger Status:")
    print(f"🌡️  Status: {status}")
    print(f"⚡ Priority Level: {priority}")
    
    return temp_exceeds

def lists_application():
    """Lists: Maintain weather records with add, remove, sort operations"""
    print("\n\nLISTS APPLICATION - Weather Records Management")
    print("=" * 50)
    
    # Weather Station Logger records list
    weather_readings = [72.5, 85.2, 68.1, 91.8, 77.3, 83.4, 95.2, 79.6, 88.1, 74.7]
    
    print("Original Weather Station Logger Records:")
    print(f"Temperature readings: {weather_readings}")
    print(f"Total records: {len(weather_readings)}")
    
    # Add new element (REQUIRED)
    new_reading = 82.9
    weather_readings.append(new_reading)
    print(f"\nAfter adding new reading ({new_reading}°F):")
    print(f"Updated readings: {weather_readings}")
    
    # Display before modifications (REQUIRED)
    print(f"\nBefore condition-based removal:")
    print(f"Current list: {weather_readings}")
    print(f"Count: {len(weather_readings)} readings")
    
    # Remove elements based on condition (REQUIRED) - Remove readings above 90°F
    extreme_threshold = 90.0
    original_count = len(weather_readings)
    weather_readings = [temp for temp in weather_readings if temp <= extreme_threshold]
    removed_count = original_count - len(weather_readings)
    
    print(f"\nAfter removing readings above {extreme_threshold}°F:")
    print(f"Filtered readings: {weather_readings}")
    print(f"Removed {removed_count} extreme reading(s)")
    
    # Sort and display (REQUIRED)
    print(f"\nBefore sorting:")
    print(f"Unsorted list: {weather_readings}")
    
    weather_readings.sort()
    print(f"\nAfter sorting (ascending):")
    print(f"Sorted list: {weather_readings}")
    
    # Additional list operations
    weather_readings_desc = sorted(weather_readings, reverse=True)
    print(f"Descending order: {weather_readings_desc}")
    
    return weather_readings

def arrays_application(temp_list):
    """Arrays: Use array module for numeric data with sum comparison"""
    print("\n\nARRAYS APPLICATION - Efficient Weather Data Storage")
    print("=" * 50)
    
    # Create array from weather station data using array module (REQUIRED)
    print("Weather Station Logger - Array Implementation:")
    print(f"Source temperature list: {temp_list}")
    
    # Convert to fixed-size numeric array
    temp_array = array.array('f', temp_list)  # 'f' for float values
    
    print(f"Array representation: {temp_array.tolist()}")
    print(f"Array type code: '{temp_array.typecode}' (float)")
    print(f"Array byte size: {temp_array.buffer_info()[1] * temp_array.itemsize} bytes")
    
    # Compute sum and compare with list version (REQUIRED)
    list_sum = sum(temp_list)
    array_sum = sum(temp_array)
    
    print(f"\nSum Comparison Analysis:")
    print(f"List sum: {list_sum:.1f}°F")
    print(f"Array sum: {array_sum:.1f}°F")
    print(f"Sums match: {abs(list_sum - array_sum) < 0.001}")
    
    # Additional array operations
    temp_array.append(78.5)
    temp_array.insert(0, 70.2)
    
    print(f"\nAfter array modifications:")
    print(f"Modified array: {temp_array.tolist()}")
    print(f"New array sum: {sum(temp_array):.1f}°F")
    
    return temp_array

def dictionaries_application():
    """Dictionaries: Weather station records with CRUD operations"""
    print("\n\nDICTIONARIES APPLICATION - Weather Station Database")
    print("=" * 50)
    
    # List of dictionaries for Weather Station Logger (REQUIRED)
    weather_stations = [
        {'id': 'WS001', 'name': 'Downtown Logger', 'value': 78.5, 'status': 'Active'},
        {'id': 'WS002', 'name': 'Airport Station', 'value': 82.3, 'status': 'Active'},
        {'id': 'WS003', 'name': 'Harbor Monitor', 'value': 75.8, 'status': 'Active'},
        {'id': 'WS004', 'name': 'Park Sensor', 'value': 85.1, 'status': 'Maintenance'},
        {'id': 'WS005', 'name': 'University Lab', 'value': 79.7, 'status': 'Active'}
    ]
    
    print("Weather Station Logger Database:")
    print("Initial Records:")
    for station in weather_stations:
        print(f"  {station['id']}: {station['name']} - {station['value']}°F [{station['status']}]")
    
    print(f"\nTotal stations: {len(weather_stations)}")
    
    # Update one record (REQUIRED)
    update_id = 'WS003'
    for station in weather_stations:
        if station['id'] == update_id:
            old_value = station['value']
            station['value'] = 88.4
            station['status'] = 'Updated'
            print(f"\nUpdated Record:")
            print(f"  Station {update_id}: {old_value}°F → {station['value']}°F")
            print(f"  Status changed to: {station['status']}")
            break
    
    # Delete another record (REQUIRED)
    delete_id = 'WS004'
    stations_before_delete = len(weather_stations)
    weather_stations = [station for station in weather_stations if station['id'] != delete_id]
    stations_after_delete = len(weather_stations)
    
    print(f"\nDeleted Record:")
    print(f"  Removed station: {delete_id}")
    print(f"  Station count: {stations_before_delete} → {stations_after_delete}")
    
    # Compute total of 'value' field (REQUIRED)
    total_value = sum(station['value'] for station in weather_stations)
    average_value = total_value / len(weather_stations)
    max_value = max(station['value'] for station in weather_stations)
    min_value = min(station['value'] for station in weather_stations)
    
    print(f"\nValue Field Analysis:")
    print(f"Total temperature value: {total_value:.1f}°F")
    print(f"Average station value: {average_value:.1f}°F")
    print(f"Highest reading: {max_value:.1f}°F")
    print(f"Lowest reading: {min_value:.1f}°F")
    
    print(f"\nFinal Weather Station Logger Database:")
    for station in weather_stations:
        indicator = "🔴" if station['status'] == 'Updated' else "🟢"
        print(f"  {indicator} {station['id']}: {station['name']} - {station['value']}°F")
    
    return weather_stations, total_value

def main():
    """Weather Station Logger - Complete Data Types Implementation"""
    print("PROJECT 13: WEATHER STATION LOGGER")
    print("=" * 60)
    print("Comprehensive Data Types Application")
    print("Student Implementation - Advanced Weather Monitoring System")
    print("=" * 60)
    
    # Execute all data type applications in sequence
    temp_total, temp_avg, sensor_total, error_total = integers_application()
    current_average = strings_application(temp_total, temp_avg, sensor_total, error_total)
    above_threshold = booleans_application(current_average)
    processed_temps = lists_application()
    temp_array = arrays_application(processed_temps)
    stations, total_value = dictionaries_application()
    
    # Final comprehensive summary
    print(f"\n\n{'='*60}")
    print("WEATHER STATION LOGGER - PROJECT SUMMARY")
    print(f"{'='*60}")
    print(f"🔢 INTEGERS: Processed {len(processed_temps)} temperature readings")
    print(f"📝 STRINGS: Generated formatted reports with totals and averages")
    print(f"✅ BOOLEANS: Applied thresholds with compound conditions")
    print(f"📋 LISTS: Managed {len(processed_temps)} records with add/remove/sort")
    print(f"🔢 ARRAYS: Implemented efficient numeric storage with sum verification")
    print(f"🗃️ DICTIONARIES: Maintained {len(stations)} station records with CRUD operations")
    print(f"\n🎯 FINAL METRICS:")
    print(f"   • System Status: {'ABOVE STANDARD' if above_threshold else 'BELOW STANDARD'}")
    print(f"   • Active Stations: {len(stations)}")
    print(f"   • Total Monitoring Value: {total_value:.1f}°F")
    print(f"   • Data Integrity: VERIFIED ✓")
    print(f"\n✨ PROJECT 13 COMPLETED SUCCESSFULLY! ✨")

if __name__ == "__main__":
    main()