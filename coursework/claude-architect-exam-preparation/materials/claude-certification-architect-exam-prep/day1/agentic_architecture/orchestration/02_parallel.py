"""
Exercise 2: Parallel Orchestration
Learn: Multiple agents running simultaneously
"""

import time
import concurrent.futures

def agent_check_weather(city):
    """Agent 1: Check weather"""
    print(f"🌤️  Agent 1: Checking weather for {city}...")
    time.sleep(2)  # Simulate API call taking 2 seconds
    result = {"city": city, "temp": 75, "condition": "sunny"}
    print(f"   ✓ Weather done: {result['temp']}°F, {result['condition']}")
    return result

def agent_check_traffic(city):
    """Agent 2: Check traffic"""
    print(f"🚗 Agent 2: Checking traffic for {city}...")
    time.sleep(2)  # Simulate API call taking 2 seconds
    result = {"city": city, "traffic": "moderate", "delay": "15 min"}
    print(f"   ✓ Traffic done: {result['traffic']}, {result['delay']} delay")
    return result

def agent_check_events(city):
    """Agent 3: Check local events"""
    print(f"🎭 Agent 3: Checking events for {city}...")
    time.sleep(2)  # Simulate API call taking 2 seconds
    result = {"city": city, "events": ["Concert", "Baseball game"]}
    print(f"   ✓ Events done: {len(result['events'])} events found")
    return result

def parallel_orchestrator_sequential(city):
    """
    OLD WAY: Run agents one after another (SLOW)
    """
    print("=== SEQUENTIAL APPROACH (SLOW) ===\n")
    start = time.time()

    weather = agent_check_weather(city)
    traffic = agent_check_traffic(city)
    events = agent_check_events(city)

    elapsed = time.time() - start
    print(f"\n⏱️  Total time: {elapsed:.1f} seconds")

    return {"weather": weather, "traffic": traffic, "events": events}

def parallel_orchestrator_parallel(city):
    """
    NEW WAY: Run agents in parallel (FAST!)
    """
    print("\n\n=== PARALLEL APPROACH (FAST) ===\n")
    start = time.time()

    # Run all 3 agents at the same time!
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit all tasks
        future_weather = executor.submit(agent_check_weather, city)
        future_traffic = executor.submit(agent_check_traffic, city)
        future_events = executor.submit(agent_check_events, city)

        # Wait for all to complete and get results
        weather = future_weather.result()
        traffic = future_traffic.result()
        events = future_events.result()

    elapsed = time.time() - start
    print(f"\n⏱️  Total time: {elapsed:.1f} seconds")
    print(f"⚡ Speed improvement: {6/elapsed:.1f}x faster!")

    return {"weather": weather, "traffic": traffic, "events": events}

# Test it!
if __name__ == "__main__":
    city = "San Francisco"

    # Compare both approaches
    result1 = parallel_orchestrator_sequential(city)
    result2 = parallel_orchestrator_parallel(city)
