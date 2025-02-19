import tenseal as ts
import pandas as pd

# Load the dataset
df = pd.read_csv("/Users/rajivsingh/water_bill_data3.csv")

# Extract relevant columns
start_reading = df["Previous_Month_Reading"].tolist()
end_reading = df["Current_Month_Reading"].tolist()

# Calculate consumption for each customer
consumption = [end - start for start, end in zip(start_reading, end_reading)]

# Calculate average consumption of all customers
average_consumption = sum(consumption) / len(consumption)

# Total revenue generated
total_revenue = df["Bill_Amount"].sum()

# Create TenSEAL context
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60])
context.global_scale = 2**40
context.generate_galois_keys()

# Encrypt the consumption data
encrypted_consumption = [ts.ckks_vector(context, [data]) for data in consumption]

# Encrypt the total amount to be paid by each customer
amount_to_be_paid = df["Bill_Amount"].tolist()
encrypted_amount_to_be_paid = [ts.ckks_vector(context, [amount]) for amount in amount_to_be_paid]

# Encrypt the total revenue generated
encrypted_total_revenue = ts.ckks_vector(context, [total_revenue])

# Print the difference between start reading and end reading for each customer
for i in range(len(start_reading)):
    print(f"Customer {i+1}: Difference between start and end reading = {end_reading[i] - start_reading[i]}")

# Now you can perform computations on the encrypted data without decrypting it
# For example, let's compute the average consumption
encrypted_sum = encrypted_consumption[0]
for enc_data in encrypted_consumption[1:]:
    encrypted_sum += enc_data

# Compute the multiplicative inverse of the number of elements
scale = 1.0 / len(consumption)

# Multiply the encrypted sum with the scale to get the average
encrypted_avg_consumption = encrypted_sum * scale

# Decrypt and print the total amount to be paid by each customer
for i in range(len(encrypted_amount_to_be_paid)):
    decrypted_amount_to_be_paid = encrypted_amount_to_be_paid[i].decrypt()[0]
    print(f"Customer {i+1}: Total amount to be paid = {decrypted_amount_to_be_paid:.2f}")

# Decrypt the average consumption
decrypted_avg_consumption = encrypted_avg_consumption.decrypt()[0]

# Decrypt the total revenue generated
decrypted_total_revenue = encrypted_total_revenue.decrypt()[0]

# Print results
print(f"Average consumption of all customers: {decrypted_avg_consumption:.2f}")
print(f"Total revenue generated: {decrypted_total_revenue:.2f}")