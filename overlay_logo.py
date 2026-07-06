from PIL import Image

def add_logo():
    # Paths
    base_img_path = r"f:\website3\img\0101_1.jpg"
    logo_img_path = r"f:\website3\img\logo.png"

    # Open images
    base = Image.open(base_img_path).convert("RGBA")
    logo = Image.open(logo_img_path).convert("RGBA")

    # Determine new size for logo (e.g. 30% of the base image width)
    base_w, base_h = base.size
    logo_w, logo_h = logo.size

    target_logo_w = int(base_w * 0.25)
    target_logo_h = int(logo_h * (target_logo_w / logo_w))

    logo = logo.resize((target_logo_w, target_logo_h), Image.Resampling.LANCZOS)

    # Padding
    padding_x = 40
    padding_y = 40

    # Position: top left
    pos_x = padding_x
    pos_y = padding_y

    # Paste the logo
    base.paste(logo, (pos_x, pos_y), logo)

    # Save
    result = base.convert("RGB")
    result.save(base_img_path, format="JPEG", quality=95)
    print("Logo overlaid successfully.")

if __name__ == "__main__":
    add_logo()
