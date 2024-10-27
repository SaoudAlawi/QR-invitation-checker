import streamlit as st
import cv2
from pyzbar.pyzbar import decode
import pandas as pd

def read_qr_code(image_path):
    img = cv2.imread(image_path)
    decoded_objects = decode(img)
    if decoded_objects:
        for obj in decoded_objects:
            return obj.data.decode('utf-8')
    else:
        return None

def validate_uuid(uuid, uuid_df,csv_file):
    if uuid in uuid_df['UUID'].values:
        if uuid_df.loc[uuid_df['UUID'] == uuid, 'Used'].item():
            return "UUID already used"
        else:
            uuid_df.loc[uuid_df['UUID'] == uuid, 'Used'] = True
            uuid_df.to_csv(csv_file, index=False)  # Save the updated DataFrame
            return "UUID valid and marked as used"
    else:
        return "UUID not found in the list"

def main():
    st.title("QR Code Reader and Validator")

    # Read UUID CSV
    csv_file = "uuid.csv"  # Replace with your CSV file path
    uuid_df = pd.read_csv(csv_file)

    # Show unused UUIDs
    if uuid_df is not None:
        st.subheader("Unused UUIDs:")
        st.write(uuid_df)

    # Upload image
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image   

        image = uploaded_file.read()

        # Save the image temporarily
        with open("temp_image.jpg", "wb") as f:
            f.write(image)

        # Decode QR code
        qr_code_data = read_qr_code("temp_image.jpg")

        if qr_code_data:
            st.write("Decoded QR code:", qr_code_data)

            # Validate UUID
            validation_result = validate_uuid(qr_code_data, uuid_df,csv_file)
            st.write(validation_result)

            
        else:
            st.write("QR code not detected in the image.")

if __name__ == "__main__":
    main()