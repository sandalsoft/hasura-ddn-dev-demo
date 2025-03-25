import requests
import os
import json

api_token = os.getenv("PROMPTQL_API_TOKEN")
if not api_token:
    raise ValueError("PROMPTQL_API_TOKEN not set in environment")

url = "https://api.promptql.pro.hasura.io/execute_program"

headers = {
    "Content-Type": "application/json",
}

code = """# Query to find iPhone customers
sql = \"\"\"
SELECT 
    c.customerId,
    c.firstName,
    c.lastName,
    c.email,
    c.phoneNumber,
    d.model AS iphone_model
FROM 
    customer.Customers c
JOIN 
    customer.CustomerPlans cp ON c.customerId = cp.customerId
JOIN 
    customer.CustomerPlanDevices cpd ON cp.customerPlanId = cpd.customerPlanId
JOIN 
    customer.Devices d ON cpd.deviceId = d.deviceId
WHERE 
    d.brand = 'Apple' AND d.model LIKE '%iPhone%'
ORDER BY 
    c.lastName, c.firstName
\"\"\"

iphone_customers = executor.run_sql(sql)

if len(iphone_customers) == 0:
    executor.print(\"No iPhone customers found.\")
else:
    executor.print(f\"Found {len(iphone_customers)} iPhone customers.\")
    
    # Store the results in an artifact
    executor.store_artifact(
        identifier='iphone_customers',
        title='iPhone Customers',
        artifact_type='table',
        data=iphone_customers
    )
"""

payload = {
    "code": code,
    "promptql_api_key": api_token,
    "ai_primitives_llm": {
        "provider": "hasura"
    },
    "ddn": {
        "url": "https://telco-0fda1a9112.axiom-hasura.private-ddn.hasura.app/v1/sql",
        "headers": {}
    },
    "artifacts": []
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
