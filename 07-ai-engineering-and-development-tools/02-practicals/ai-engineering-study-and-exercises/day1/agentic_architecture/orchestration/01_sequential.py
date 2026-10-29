"""
Exercise 1: Sequential Orchestration
Learn: Agents running one after another (pipeline)
"""

def agent_fetch_data(user_id):
    """Agent 1: Fetch user data"""
    print(f"🔍 Agent 1: Fetching data for user {user_id}...")
    # Simulate fetching
    data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john@example.com"
    }
    print(f"   ✓ Found user: {data['name']}")
    return data

def agent_validate_data(data):
    """Agent 2: Validate the data"""
    print(f"\n✅ Agent 2: Validating data...")

    # Check required fields
    if not data.get("email"):
        raise Exception("Email missing!")

    if "@" not in data["email"]:
        raise Exception("Invalid email format!")

    print(f"   ✓ Data is valid")
    return data

def agent_process_data(data):
    """Agent 3: Process the data"""
    print(f"\n⚙️  Agent 3: Processing data...")

    # Add processed fields
    data["processed"] = True
    data["email_domain"] = data["email"].split("@")[1]

    print(f"   ✓ Processed successfully")
    print(f"   Email domain: {data['email_domain']}")
    return data

def sequential_orchestrator(user_id):
    """
    Main orchestrator that runs agents sequentially.
    Each agent depends on the previous one.
    """
    print("=== SEQUENTIAL ORCHESTRATION ===\n")
    print("Pipeline: Fetch → Validate → Process\n")

    try:
        # Step 1: Fetch
        data = agent_fetch_data(user_id)

        # Step 2: Validate (needs data from Step 1)
        data = agent_validate_data(data)

        # Step 3: Process (needs validated data from Step 2)
        result = agent_process_data(data)

        print(f"\n✅ Pipeline completed successfully!")
        print(f"📊 Final result: {result}")
        return result

    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")
        return None

# Test it!
if __name__ == "__main__":
    sequential_orchestrator(user_id=123)
