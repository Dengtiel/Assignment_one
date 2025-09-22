#!/usr/bin/env python3
"""
Simple Boolean Data Type Demo
Demonstrates boolean operations and threshold conditions
"""

def main():
    print("BOOLEAN DATA TYPE APPLICATION")
    print("=" * 40)
    
    # Weather data for boolean tests
    temperature = 78.5
    humidity = 65
    wind_speed = 12
    
    print("WEATHER CONDITIONS:")
    print(f"Temperature: {temperature}°F")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} mph")
    
    # Define thresholds
    temp_threshold = 75.0
    humidity_threshold = 60.0
    wind_threshold = 15.0
    
    print(f"\nTHRESHOLDS:")
    print(f"Temperature > {temp_threshold}°F")
    print(f"Humidity > {humidity_threshold}%") 
    print(f"Wind > {wind_threshold} mph")
    
    print("\nBOOLEAN CONDITIONS:")
    # Individual boolean conditions
    temp_high = temperature > temp_threshold
    humidity_high = humidity > humidity_threshold
    wind_high = wind_speed > wind_threshold
    
    print(f"Temperature high: {temp_high}")
    print(f"Humidity high: {humidity_high}")
    print(f"Wind high: {wind_high}")
    
    print("\nCOMPOUND CONDITIONS:")
    # Compound boolean conditions (required)
    hot_and_humid = temp_high and humidity_high
    uncomfortable = temp_high and humidity_high
    windy_or_humid = wind_high or humidity_high
    perfect_weather = not temp_high and not humidity_high and not wind_high
    
    print(f"Hot AND Humid: {hot_and_humid}")
    print(f"Uncomfortable: {uncomfortable}")
    print(f"Windy OR Humid: {windy_or_humid}")
    print(f"Perfect Weather: {perfect_weather}")
    
    print("\nSTATUS MESSAGES:")
    # Status based on boolean conditions
    if temp_high and humidity_high:
        status = "Above Standard - Hot and Humid"
    elif temp_high:
        status = "Above Standard - High Temperature"
    elif humidity_high:
        status = "Above Standard - High Humidity"
    else:
        status = "Below Standard - Normal Conditions"
    
    print(f"Weather Status: {status}")
    
    print("\nSAFETY CHECK:")
    # Safety assessment
    outdoor_safe = not (temp_high and humidity_high and wind_high)
    print(f"Safe for outdoor activities: {outdoor_safe}")
    
    if outdoor_safe:
        print("✓ Go ahead with outdoor plans!")
    else:
        print("⚠ Consider indoor activities instead.")

if __name__ == "__main__":
    main()