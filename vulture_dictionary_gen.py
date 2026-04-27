import json

# Example: In a real run, you'd pull this from a CSV or a huge list
locations = [
    "Dallas, TX", "London, UK", "Paris, France", "Tokyo, Japan", 
    "Miami, FL", "Arlington, TX", "Barcelona, Spain"
] # Imagine 100,000 more here

def generate_global_manifest():
    # We organize by first letter for lightning-fast lookups
    dictionary = {}
    
    for loc in locations:
        first_letter = loc[0].upper()
        if first_letter not in dictionary:
            dictionary[first_letter] = []
        dictionary[first_letter].append(loc)

    with open('global_nodes.json', 'w') as f:
        json.dump(dictionary, f)
    
    print(f"✅ Created a tiered manifest with {len(locations)} nodes.")

if __name__ == "__main__":
    generate_global_manifest()
