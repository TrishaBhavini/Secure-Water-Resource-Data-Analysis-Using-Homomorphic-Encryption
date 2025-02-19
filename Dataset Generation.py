import csv
import tenseal as ts
import pandas as pd
import random

def generate_location():
  locations = ["Rural", "Urban", "City", "Town"]
  return random.choice(locations)

def generate_meter_type():
  types = ["Mechanical", "Digital"]
  return random.choice(types)

def generate_service_type():
  types = ["Residential", "Commercial", "Industrial"]
  return random.choice(types)

def calculate_water_bill(total_consumption):
  """
  Calculates the water bill amount based on consumption tiers.

  Args:
      total_consumption: The total water consumption in gallons (int).

  Returns:
      The water bill amount (float).
  """
  if total_consumption <= 100:
    return total_consumption * 2.25
  elif total_consumption <= 200:
    return (100 * 2.25) + ((total_consumption - 100) * 4.5)
  elif total_consumption <= 400:
    return (100 * 2.25) + (100 * 4.5) + ((total_consumption - 200) * 4.5)
  elif total_consumption <= 500:
    return (100 * 2.25) + (100 * 4.5) + (200 * 4.5) + ((total_consumption - 400) * 6)
  elif total_consumption <= 600:
    return (100 * 2.25) + (100 * 4.5) + (200 * 4.5) + (100 * 6) + ((total_consumption - 500) * 8)
  else:
    return (100 * 2.25)  + (100 * 4.5) + (200 * 4.5) + (100 * 6) + (100 * 8) + ((total_consumption - 600) * 9)

def generate_data(customer_id):
  customer_name = f"Customer {customer_id}"
  location = generate_location()
  previous_reading = random.randint(100, 1000)
  current_reading = previous_reading + random.randint(50, 200)
  consumption = current_reading - previous_reading

  # Randomly set payment status (50% chance of unpaid)
  payment_status = "Unpaid" if random.random() < 0.5 else "Paid"

  meter_type = generate_meter_type()
  service_type = generate_service_type()

  bill_amount = calculate_water_bill(consumption)

  # Calculate excess water usage cost (assuming free base usage)
  free_usage = 100  # Define free water usage limit
  excess_usage = max(0, consumption - free_usage)  # Calculate excess usage if any
  excess_cost = excess_usage * 5  # Set excess water cost per gallon

  return {
      "Customer_ID": customer_id,
      "Customer_Name": customer_name,
      "Location": location,
      "Previous_Month_Reading": previous_reading,
      "Current_Month_Reading": current_reading,
      "Consumption_Gallons": consumption,
      "Bill_Amount": bill_amount,
      "Payment_Status": payment_status,
      "Meter_Type": meter_type,
      "Service_Type": service_type,
      "Excess_Usage_Gallons": excess_usage,
      "Excess_Water_Cost": excess_cost
  }

with open("water_bill_data", "w", newline="") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=[
      "Customer_ID",
      "Customer_Name",
      "Location",
      "Previous_Month_Reading",
      "Current_Month_Reading",
      "Consumption_Gallons",
      "Bill_Amount",
      "Payment_Status",
      "Meter_Type",
      "Service_Type",
      "Excess_Usage_Gallons",
      "Excess_Water_Cost"
  ])
  writer.writeheader()  # Move this line one level to the left
  for i in range(1, 101):
    data = generate_data(i)
    writer.writerow(data)

print("Water bill dataset generated successfully!")
