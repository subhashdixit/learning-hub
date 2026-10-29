"""
Exercise 2: Agent Loop with Circuit Breaker
Learn: How to prevent wasting resources on broken services
"""

import time
import random

# Circuit Breaker State
circuit_breaker_failures = 0
CIRCUIT_BREAKER_THRESHOLD = 5

def check_api(data):
    """
    Simulates calling an external API.
    Sometimes fails (50% chance to show circuit breaker)
    """
    if random.random() < 0.5:
        raise Exception("API timeout!")

    return f"Processed: {data}"

def agent_with_circuit_breaker(data):
    """
    Agent that stops trying if too many failures occur.
    """
    global circuit_breaker_failures

    # Check circuit breaker first
    if circuit_breaker_failures >= CIRCUIT_BREAKER_THRESHOLD:
        print("⚡ CIRCUIT BREAKER OPEN!")
        print(f"   Too many failures ({circuit_breaker_failures}). Service is down.")
        print("   Returning cached result instead.\n")
        return f"[CACHED] {data}"

    max_retries = 3
    attempt = 0

    while attempt < max_retries:
        try:
            print(f"Attempt {attempt + 1}: Calling API...")

            result = check_api(data)

            # Success! Reset circuit breaker
            circuit_breaker_failures = 0
            print(f"✓ Success! Result: {result}\n")
            return result

        except Exception as e:
            attempt += 1
            circuit_breaker_failures += 1

            print(f"✗ Error: {e}")
            print(f"   Circuit breaker failures: {circuit_breaker_failures}/{CIRCUIT_BREAKER_THRESHOLD}")

            if circuit_breaker_failures >= CIRCUIT_BREAKER_THRESHOLD:
                print("⚡ Circuit breaker threshold reached!")
                return f"[CACHED] {data}"

            if attempt < max_retries:
                wait_time = 2 ** attempt
                print(f"   Waiting {wait_time}s before retry...\n")
                time.sleep(wait_time)
            else:
                print("✗ Max retries reached.\n")
                return None

# Test it!
if __name__ == "__main__":
    print("=== AGENT WITH CIRCUIT BREAKER ===\n")

    # Try processing 10 requests
    for i in range(1, 11):
        print(f"--- Request {i} ---")
        result = agent_with_circuit_breaker(f"data_{i}")
        time.sleep(0.5)  # Small delay between requests
