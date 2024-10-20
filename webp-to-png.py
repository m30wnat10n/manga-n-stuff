import os
from PIL import Image

def convert_webp_to_png():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Loop through all files in the script's folder
    for filename in os.listdir(script_dir):
        if filename.endswith(".webp"):
            # Open the .webp image
            img_path = os.path.join(script_dir, filename)
            img = Image.open(img_path)

            # Define the output path for the .png image
            png_filename = f"{os.path.splitext(filename)[0]}.png"
            output_path = os.path.join(script_dir, png_filename)

            # Save the image as .png
            img.save(output_path, "PNG")
            print(f"Converted: {img_path} to {output_path}")

# Run the function
convert_webp_to_png()
