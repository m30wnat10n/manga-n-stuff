import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse, parse_qs

# Function to download images
def download_image(url, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Parse the URL and extract the path without the query parameters
    parsed_url = urlparse(url)
    base_filename = os.path.basename(parsed_url.path)  # Extract the filename from the URL
    
    filename = os.path.join(folder_name, base_filename)  # Create the full file path
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f'Successfully downloaded {filename}')
    else:
        print(f'Failed to download {url}')

# Function to extract image URLs and download them
def scrape_images(url, folder_name='downloaded_images'):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image elements or links pointing to the images (You can adjust the filter depending on the website structure)
        img_tags = soup.find_all('img')
        
        # Extract image URLs
        for img in img_tags:
            img_url = img.get('src')  # Extract src attribute of the img tag
            if img_url:
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url  # Fix protocol-less URLs
                elif img_url.startswith('/'):
                    img_url = url + img_url  # Relative URLs
            
                # Download the image
                download_image(img_url, folder_name)
    else:
        print(f'Failed to access {url}')


# URL of the website you want to scrape (you might need to change it)
page_url = 'https://jcomic.net/page/%E6%88%91%E4%BA%B2%E7%88%B1%E7%9A%84%E6%9D%80%E4%BA%BA%E9%AC%BC%20%E5%83%95%E3%81%AE%E6%84%9B%E3%81%97%E3%81%AE%E6%AE%BA%E4%BA%BA%E9%AC%BC[%E4%B8%AD%E5%9B%BD%E7%BF%BB%E8%A8%B3]'

# Scrape and download all images from the page
scrape_images(page_url)
