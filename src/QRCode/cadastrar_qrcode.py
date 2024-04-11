import qrcode
import json

# Load the JSON data from the file
with open('drug_info_pitch.json', 'r') as json_file:
    drug_data_list = json.load(json_file)

# Function to generate and save QR codes
def generate_qr_codes(drug_data_list):
    for drug_info in drug_data_list:
        # Serialize the drug information to a JSON string
        drug_info_json = json.dumps(drug_info)
        
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(drug_info_json)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code as an image file
        img.save(f"{drug_info['Nome']}.png")

# Call the function to generate QR codes
generate_qr_codes(drug_data_list)
