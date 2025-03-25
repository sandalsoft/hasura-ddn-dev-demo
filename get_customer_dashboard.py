import requests
import json

# GraphQL endpoint
url = "https://telco-0fda1a9112.axiom-hasura.private-ddn.hasura.app/graphql"

# GraphQL query
query = """
query CustomerDashboard {
  customers(
    where: {customerId: {_eq: "1"}}
    limit: 10
  ) {
    customerId
    firstName
    creditCards {
      expiry
      maskCreditCard
      number
      customerId
      createdAt
      updatedAt
    }
    customerPlans {
      cellNumber
      customerPlanId
      startDate
      endDate
      plan {
        description
      }
      customerPlanDevices {
        device {
          brand
          model
          updatedAt
        }
      }
    }
    customerLinks {
      customerPreferences {
        behavioralData {
          lastAppLogin
          lastWebsiteVisit
        }
      }
    }
  }
}
"""

# Headers (assuming no auth token is needed; add if required)
headers = {
    "Content-Type": "application/json",
}

# Payload
payload = {
    "query": query
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Check response and print
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")