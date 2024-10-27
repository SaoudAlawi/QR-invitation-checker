# QR Code Reader and Validator

This is a Streamlit application that allows users to upload an image of a QR code, decode it, and validate the decoded content against a list of UUIDs stored in a CSV file. If the UUID is valid and unused, it will be marked as used.

## Features

- Upload an image file containing a QR code.
- Decode the QR code and display its content.
- Validate the decoded UUID against a CSV file.
- Mark the UUID as used if it is valid.

## Requirements

This application requires the following Python packages:

- Streamlit
- OpenCV
- Pyzbar
- Pandas
- UUID
- Qrcode

## Setup Instructions



### 1. Clone the Repository

```bash
git clone https://github.com/SaoudAlawi/QR-invitation-checker.git
cd QR-invitation-checker
```
###  2. Create a Virtual Environment as you see fit

Then, install the dependencies using:

```bash
pip install -r requirements.txt
```
## Generating UUIDs and QR Codes


```bash
python generate_qr_db.py
```
Output: The script will create a CSV file named uuid.csv with the UUIDs and their usage status (set to False by default), and the QR code images will be stored at ./img.

## 5. How the Application Works
- Spreading the QR Codes: Once the UUIDs and QR codes are generated, you can distribute the QR codes to users or print them for access. Each QR code corresponds to a unique UUID.

- Uploading and Decoding: Users can upload an image containing a QR code through the Streamlit app. The app will decode the QR code using OpenCV and Pyzbar libraries.

- Validation: The decoded content (UUID) will be checked against the entries in the uuid.csv file. If the UUID is found and marked as unused, the app will update its status to "used" in the CSV file.

## Run the Application
To start the Streamlit application, use the following command:

```bash
streamlit run qr_code_validator_app.py --server.address <hostname> --server.port 8501
```
## Access the Application
After running the above command, Streamlit will provide a local URL (usually http://localhost:8501). Open this URL in your web browser to access the QR Code Reader and Validator application.

