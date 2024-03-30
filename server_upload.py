import requests
import os

def upload_picture(file_path, expiration, token, server_url):
    # Endpoint for uploading
    upload_endpoint = server_url + "/upload"
    
    # Prepare headers
    headers = {
        'token': token,
        'filename': os.path.basename(file_path),
        'expiration': str(expiration)
    }
    
    # Read image data
    if not os.path.exists(file_path):
        print("No such file or directory")
        return
    
    with open(file_path, 'rb') as file:
        image_data = file.read()
    
    # Make the POST request
    response = requests.post(upload_endpoint, headers=headers, data=image_data)
    
    # Check response status
    if response.status_code == 200:
        # Extract image token from response
        image_token = response.text
        # Construct the URL for accessing the uploaded image
        image_url = server_url + "/dip/" + image_token
        return image_url
    else:
        print("Failed to upload picture. Status code:", response.status_code)
        return None
