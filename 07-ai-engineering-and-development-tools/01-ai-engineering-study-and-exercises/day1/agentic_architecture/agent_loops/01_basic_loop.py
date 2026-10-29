"""
Exercise 1: Basic Agent Loop
Learn: How agents loop with retry logic
"""

import time
import random

def check_number(num):
    """
    Simulates checking if number is even.
    Sometimes fails randomly (to simulate real-world errors)
    """
    # Simulate random failure (30% chance)
    if random.random() < 0.3:
        raise Exception("Connection error! Could not check number.")

    # Check if even
    return num % 2 == 0

def agent_loop_basic(num):
    """
    Agent that checks if number is even.
    Retries up to 3 times if it fails.
    """
    max_retries = 3
    attempt = 0

    while attempt < max_retries:
        try:
            print(f"Attempt {attempt + 1}: Checking if {num} is even...")

            result = check_number(num)

            # Success!
            print(f"✓ Success! {num} is {'even' if result else 'odd'}")
            return result

        except Exception as e:
            attempt += 1
            print(f"✗ Error: {e}")

            if attempt < max_retries:
                wait_time = 2 ** attempt  # Exponential backoff: 2, 4, 8 seconds
                print(f"  Waiting {wait_time} seconds before retry...\n")
                time.sleep(wait_time)
            else:
                print("✗ Max retries reached. Giving up.")
                return None

# Test it!
if __name__ == "__main__":
    print("=== BASIC AGENT LOOP ===\n")
    agent_loop_basic(42)
