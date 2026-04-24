import json
import os

schema_path = "data_models/customer_schema.json"
data_path = "data/sample_customer.json"

# Load and display schema info
if os.path.exists(schema_path):
    with open(schema_path, "r") as f:
        schema = json.load(f)
    print(f"Title: {schema.get('title')}")
    print("Properties:")
    for field in schema.get("properties", {}):
        print(f"  - {field}")
else:
    print(f"Error: Could not find schema at '{schema_path}'")

# Load and validate customer data
if os.path.exists(data_path):
    with open(data_path, "r") as f:
        customer = json.load(f)

    email = customer.get("email", "")
    if "@" not in email:
        print("Data Quality Warning! Email address is missing '@' symbol.")
    else:
        print(f"\nCustomer email '{email}' passed validation.")

    total_purchases = customer.get("total_purchases")
    if not isinstance(total_purchases, (int, float)):
        print("Data Quality Warning: total_purchases must be a number.")
    else:
        print(f"total_purchases '{total_purchases}' passed validation.")
else:
    print(f"Error: Could not find data at '{data_path}'")
