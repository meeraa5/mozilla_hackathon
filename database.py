def get_food_banks(school):
    food_bank_data = {
        "SJSU": [
            {"name": "Second Harvest Food Bank", "address": "123 Main St, San Jose"},
            {"name": "SJSU Food Pantry", "address": "Student Union, SJSU"}
        ]
    }
    return food_bank_data.get(school, [])

