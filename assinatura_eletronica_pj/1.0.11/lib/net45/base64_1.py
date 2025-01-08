import sys
import base64
import io
import zipfile
import os
import json

read_file_path = sys.argv[1]
file_path = sys.argv[2]

def decode_base64_to_pdf(decoded_data, pdf_file_path):
    with open(pdf_file_path, 'wb') as pdf_file:
        pdf_file.write(decoded_data)

def convert_base64_to_pdf(json_file_path, output_pdf_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        if 'DocumentBase64' in json_data:
            base64_string = json_data['DocumentBase64']
            decoded_data = base64.b64decode(base64_string)
            decode_base64_to_pdf(decoded_data, output_pdf_path)

def extract_zip(zip_path, extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

def find_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.json'):
                json_files.append(os.path.join(root, filename))
    return json_files

def convert_base64_zip_to_pdf_files(read_file_path, file_path):
    try:
        with open(read_file_path, 'r') as file:
            base64_string = file.read()
     # Decode the base64 string
        decoded_data = base64.b64decode(base64_string)

       # Write the decoded data to the ZIP file
        with open(file_path, 'wb') as zip_file:
            zip_file.write(decoded_data)

       # Extract the contents of the ZIP file
        extract_dir = os.path.splitext(file_path)[0]  # Create a directory with the same name as the ZIP file
        extract_zip(file_path, extract_dir)

       # Traverse the extracted directory and find .json files to convert to PDF
        evidencias_dir = os.path.join(extract_dir, 'Evidências')
        json_files = find_json_files(evidencias_dir)
        for json_file_path in json_files:
            pdf_file_path = os.path.splitext(json_file_path)[0] + '.pdf'
            convert_base64_to_pdf(json_file_path, pdf_file_path)

        print(f'Successfully extracted and converted JSON files to PDFs in {evidencias_dir}')
    except Exception as e:
        print(f'Error occurred: {e}')

convert_base64_zip_to_pdf_files(read_file_path, file_path)