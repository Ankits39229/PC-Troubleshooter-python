#!/usr/bin/env python3
"""
Create a simple icon for the PC Troubleshooter application
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    # Create a 256x256 icon
    size = (256, 256)
    
    # Create a new image with transparent background
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Define colors
    bg_color = (30, 30, 30, 255)  # Dark background
    primary_color = (0, 120, 255, 255)  # Blue
    secondary_color = (255, 255, 255, 255)  # White
    accent_color = (0, 255, 120, 255)  # Green
    
    # Draw background circle
    margin = 20
    draw.ellipse([margin, margin, size[0]-margin, size[1]-margin], 
                 fill=bg_color, outline=primary_color, width=4)
    
    # Draw computer monitor shape
    monitor_margin = 60
    monitor_top = 70
    monitor_bottom = 160
    monitor_left = 60
    monitor_right = 196
    
    # Monitor screen
    draw.rectangle([monitor_left, monitor_top, monitor_right, monitor_bottom], 
                   fill=primary_color, outline=secondary_color, width=2)
    
    # Monitor stand
    stand_width = 40
    stand_height = 20
    stand_left = (size[0] - stand_width) // 2
    stand_top = monitor_bottom + 5
    draw.rectangle([stand_left, stand_top, stand_left + stand_width, stand_top + stand_height], 
                   fill=secondary_color)
    
    # Monitor base
    base_width = 80
    base_height = 8
    base_left = (size[0] - base_width) // 2
    base_top = stand_top + stand_height
    draw.rectangle([base_left, base_top, base_left + base_width, base_top + base_height], 
                   fill=secondary_color)
    
    # Draw tools icon on screen
    tool_size = 15
    
    # Wrench
    wrench_x = monitor_left + 20
    wrench_y = monitor_top + 20
    draw.rectangle([wrench_x, wrench_y, wrench_x + tool_size, wrench_y + tool_size*2], 
                   fill=accent_color)
    
    # Screwdriver
    screwdriver_x = wrench_x + 25
    screwdriver_y = wrench_y + 5
    draw.rectangle([screwdriver_x, screwdriver_y, screwdriver_x + tool_size, screwdriver_y + tool_size*2], 
                   fill=accent_color)
    
    # Gear
    gear_x = wrench_x + 50
    gear_y = wrench_y
    draw.ellipse([gear_x, gear_y, gear_x + tool_size*1.5, gear_y + tool_size*1.5], 
                 fill=accent_color)
    
    # Add text "PC" in the bottom part of the screen
    try:
        # Try to use a system font
        font_size = 24
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    text = "PC"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = monitor_left + (monitor_right - monitor_left - text_width) // 2
    text_y = monitor_bottom - text_height - 10
    
    draw.text((text_x, text_y), text, fill=secondary_color, font=font)
    
    return img

def main():
    print("🎨 Creating PC Troubleshooter icon...")
    
    # Ensure assets directory exists
    assets_dir = "assets"
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    
    # Create the icon
    icon = create_icon()
    
    # Save as PNG
    png_path = os.path.join(assets_dir, "icon.png")
    icon.save(png_path, "PNG")
    print(f"   ✅ PNG icon saved: {png_path}")
    
    # Save as ICO with multiple sizes
    ico_path = os.path.join(assets_dir, "icon.ico")
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    icon.save(ico_path, format='ICO', sizes=sizes)
    print(f"   ✅ ICO icon saved: {ico_path}")
    
    print("   🎉 Icon creation completed!")

if __name__ == "__main__":
    main()
