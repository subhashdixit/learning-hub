"""
Exercise 3: Graceful Fallback
Learn: How to provide alternatives when primary service fails
"""

import random
import time

# Simulated cache
CACHE = {
    "weather": {"temp": 72, "condition": "sunny", "cached": True},
    "stock": {"price": 150.00, "cached": True},
}

def get_live_weather():
    """Try to get real-time weather (fails 70% of time)"""
    if random.random() < 0.7:
        raise Exception("Weather API down!")
    return {"temp": 75, "condition": "cloudy", "cached": False}

def get_cached_weather():
    """Fallback: Return cached weather data"""
    print("   → Using cached data (may be outdated)")
    return CACHE["weather"]

def get_default_weather():
    """Last resort: Return safe default"""
    print("   → Using default values")
    return {"temp": 70, "condition": "unknown", "cached": True}

def agent_with_fallback():
    """
    Agent that tries multiple fallback strategies:
    1. Live data (best)
    2. Cached data (good)
    3. Default data (acceptable)
    """
    print("Checking weather...\n")

    # Strategy 1: Try live data
    try:
        print("1️⃣ Trying live API...")
        result = get_live_weather()
        print(f"   ✓ Got live data: {result['temp']}°F, {result['condition']}")
        return result

    except Exception as e:
        print(f"   ✗ Live API failed: {e}")

    # Strategy 2: Try cache
    try:
        print("\n2️⃣ Trying cache...")
        result = get_cached_weather()
        print(f"   ✓ Got cached data: {result['temp']}°F, {result['condition']}")
        return result

    except Exception as e:
        print(f"   ✗ Cache failed: {e}")

    # Strategy 3: Use default
    print("\n3️⃣ Using default fallback...")
    result = get_default_weather()
    print(f"   ✓ Got default: {result['temp']}°F, {result['condition']}")
    return result

# Test it!
if __name__ == "__main__":
    print("=== GRACEFUL FALLBACK EXAMPLE ===\n")

    # Try 5 times to see different scenarios
    for i in range(1, 6):
        print(f"--- Attempt {i} ---")
        weather = agent_with_fallback()
        print(f"\n📊 Final result: {weather}\n")
        time.sleep(0.5)
