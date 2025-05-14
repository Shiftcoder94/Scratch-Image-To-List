from PIL import Image

def rgb_to_scratch_color_integer(r, g, b):
    return r * 65536 + g * 256 + b

def crop_image_to_size(img, target_width, target_height):
    return img.resize((target_width, target_height))

def image_to_scratch_color_list(image_path, width, height):
    img = Image.open(image_path).convert('RGB')

    if img.size != (width, height):
        print(f"Image size {img.size} does not match expected {width}x{height}. Cropping...")
        img = crop_image_to_size(img, width, height)

    pixels = img.load()
    color_list = []

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            scratch_color_int = rgb_to_scratch_color_integer(r, g, b)
            color_list.append(scratch_color_int)

    return color_list

def save_color_list_to_txt(color_list, output_path):
    with open(output_path, 'w') as f:
        for color in color_list:
            f.write(str(color) + '\n')

# Example usage
if __name__ == "__main__":
    image_path = r"<your full absolute image path>"      # Replace with your image file
    output_txt = r"<your full absolute output list path>"  # Output file
    width = 480                         # Desired width
    height = 300                        # Desired height

    try:
        color_list = image_to_scratch_color_list(image_path, width, height)
        save_color_list_to_txt(color_list, output_txt)
        print(f"Color list saved to {output_txt}")
    except Exception as e:
        print("Error:", e)
