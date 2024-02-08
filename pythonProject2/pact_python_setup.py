from pact import Consumer, Provider, Like

# Import the Employee model from your FastAPI module
from main import Employee

# Define the Consumer and Provider
consumer = Consumer("Dashboard")
provider = Provider("Employee")

# Define the interaction (contract)
with consumer.has_pact_with(provider):
    (consumer
        .upon_receiving("A request to create an employee")
        .with_request("POST", "/employees/create")
        .with_body(Like(Employee(name="John Doe", age=25, department="HR")))
        .will_respond_with(200, body={"message": "Employee created successfully"}))

    # Add more interactions for update and delete as needed

# Write the pact file
with open("dashboard_employee_contract.json", "w") as f:
    f.write(consumer.to_json())
