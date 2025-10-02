# Image-Resizer-Tool
A simple, efficient Python script to resize and convert images in batch using the Pillow library. Perfect for automating image processing tasks across folders.

📌 Features

✅ Resize all images in a folder to a custom size
✅ Convert images to a target format (e.g., JPEG, PNG)
✅ Supports multiple image types: .jpg, .png, .jpeg, .webp, .bmp, .tiff
✅ Handles batch processing automatically
✅ Saves resized images to a separate output folder

🚀 Getting Started
1. Clone the Repository or Download the Script
````
git clone https://github.com/yourusername/image-resizer-tool.git
cd image-resizer-tool
```` 

Or simply download the image_resizer.py file.

2. Install Requirements

Ensure you have Python 3 installed.
Install the required Pillow library:
````
pip install pillow
````
3. Prepare Your Folders

Place your original images in the input_images/ folder.
The script will save the resized and converted images to the output_images/ folder.

4. Run the Script
````
python image_resizer.py
````
⚙️ Configuration

You can customize the following settings directly in the script:
````
input_folder = "input_images"
output_folder = "output_images"
new_size = (800, 600)  # Resize dimensions (width, height)
output_format = "JPEG"  # Output format: "PNG", "JPEG", "WEBP", etc.
````
🧠 How It Works

Reads all image files in the input folder using the os module.
Uses the PIL.Image module from Pillow to:
Resize images
Convert them to the target format
Save them to the output folder
Automatically skips non-image files or unsupported formats.

📂 Folder Structure
image_resizer/
│
├── input_images/       # Your original images
├── output_images/      # Resized and converted images
├── image_resizer.py    # Main script
└── README.md           # Project documentation

🧩 Example Output

Original:

photo1.png (1920x1080)

logo.webp (1024x1024)

After processing:

photo1.jpeg (800x600)

logo.jpeg (800x600)
