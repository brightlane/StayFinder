import json

# 🏟️ HIGH-VALUE 2026 WORLD CUP NODES
world_cup_nodes = [
    "AT&T Stadium Dallas", "Estadio Azteca Mexico City", "MetLife Stadium New York",
    "Mercedes-Benz Stadium Atlanta", "SoFi Stadium Los Angeles", "Lumen Field Seattle",
    "Levi's Stadium San Francisco", "Gillette Stadium Boston", "Lincoln Financial Field Philadelphia",
    "Hard Rock Stadium Miami", "NRG Stadium Houston", "Arrowhead Stadium Kansas City",
    "BMO Field Toronto", "BC Place Vancouver", "Estadio BBVA Monterrey", "Estadio Akron Guadalajara"
]

# 🌍 GLOBAL STARTER LIST (Expand this to 10,000+ for full takeover)
global_cities = [
    "London", "Paris", "Tokyo", "Dubai", "Rome", "Barcelona", "Amsterdam", "Madrid",
    "Berlin", "Vienna", "Prague", "Istanbul", "Seoul", "Singapore", "Bangkok",
    "Bali", "Cancun", "Maldives", "Santorini", "Kyoto", "Venice", "Florence"
]

def build_vulture_dictionary():
    # Combine and clean
    master_list = list(set(world_cup_nodes + global_cities))
    
    # Tiered Indexing (Fast-Lookup Architecture)
    dictionary = {}
    
    for item in master_list:
        first_char = item[0].upper()
        if first_char not in dictionary:
            dictionary[first_char] = []
        dictionary[first_char].append(item)
    
    # Save as the fuel for index.html
    with open('global_nodes.json', 'w') as f:
        json.dump(dictionary, f, indent=2)
    
    print(f"🦅 SUCCESS: {len(master_list)} Nodes indexed into global_nodes.json")

if __name__ == "__main__":
    build_vulture_dictionary()
