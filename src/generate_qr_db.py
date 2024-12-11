import uuid
import pandas as pd
import qrcode
import os

# Generate 100 UUIDs and set 'Used' status to False
uuid_data = [{"UUID": str(uuid.uuid4()), "Used": False} for _ in range(150)]

# Convert the list to a DataFrame
df = pd.DataFrame(uuid_data)

# Step 1: Save UUIDs to a CSV file with a 'Used' column
csv_filename = "uuid.csv"
df.to_csv(csv_filename, index=False)
print(f"UUIDs saved to {csv_filename} with 'Used' column set to False")

# Step 2: Generate QR codes for each UUID and save as images
output_dir = "./img"
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

for idx, uuid_str in enumerate(df["UUID"], start=1):
    # Generate the QR code
    qr = qrcode.make(uuid_str)
    
    # Save the QR code as an image
    qr_filename = os.path.join(output_dir, f"qr_code_{idx}.png")
    qr.save(qr_filename)

print(f"QR code images saved in the '{output_dir}' directory.")