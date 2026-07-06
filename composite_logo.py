from PIL import Image

# Load the base image
base_img_path = r"C:\Users\user102\.gemini\antigravity-ide\brain\f79a10d8-0c59-45eb-9840-54bc1c1ff0c0\foreign_engineers_1783310378092.png"
base_img = Image.open(base_img_path).convert("RGBA")

# Load the logo image
logo_img_path = r"f:\website3\img\logo.png"
logo_img = Image.open(logo_img_path).convert("RGBA")

# Resize logo to fit nicely. The base image is usually 1024x1024 or similar.
# Let's make the logo width around 300px.
target_width = 250
wpercent = (target_width / float(logo_img.size[0]))
hsize = int((float(logo_img.size[1]) * float(wpercent)))
logo_img = logo_img.resize((target_width, hsize), Image.Resampling.LANCZOS)

# Create a composite
# We want it in the top-left corner with some padding (e.g., 30px)
padding = 40
base_img.paste(logo_img, (padding, padding), logo_img)

# Save the final result as JPG (drop alpha channel)
final_img = base_img.convert("RGB")
final_img.save(r"f:\website3\img\0101_1.jpg", "JPEG", quality=95)
print("Image composited and saved successfully.")
