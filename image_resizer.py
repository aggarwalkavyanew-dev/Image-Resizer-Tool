import os
from PIL import Image

# Configuration
input_folder = "input_images"
output_folder = "output_images"
new_size = (800, 600)  # Width x Height
output_format = "JPEG"  # Can be "PNG", "WEBP", etc.

def resize_and_convert_images():
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff')):
            input_path = os.path.join(input_folder, filename)
            output_name = os.path.splitext(filename)[0] + '.' + output_format.lower()
            output_path = os.path.join(output_folder, output_name)

            try:
                with Image.open(input_path) as img:
                    img = img.resize(new_size)
                    img = img.convert("RGB")  # Ensures compatibility with JPEG
                    img.save(output_path, output_format)
                    print(f"Processed: {filename} -> {output_name}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    resize_and_convert_images()
    print("✅ All images processed.")
