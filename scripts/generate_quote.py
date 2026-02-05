#!/usr/bin/env python3
"""
Generate social media quote images with Jeff 'SKI' Kinsey branding.
Overlays quote text on the branded background template.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_quote_image(quote_text, output_path, template_path):
    """
    Generate a quote image using the branded template.
    
    Args:
        quote_text: The quote to display (without quotation marks, they'll be added)
        output_path: Where to save the output image
        template_path: Path to the background template image
    """
    # Load the template
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    
    # Image dimensions
    width, height = img.size
    
    # Text positioning - centered in upper-middle area
    text_x = width // 2
    text_y = height // 3  # Upper third of image
    max_width = int(width * 0.85)  # 85% of image width for text
    
    # Use the Rye font
    font_size = 72
    script_dir = Path(__file__).parent
    rye_font_path = script_dir.parent / "assets" / "Rye-Regular.ttf"
    
    try:
        font = ImageFont.truetype(str(rye_font_path), font_size)
    except:
        # Fall back to default if Rye font is not found
        font = ImageFont.load_default()
    
    # Add quotation marks
    formatted_quote = f'"{quote_text}"'
    
    # Wrap text to fit within max_width
    # Estimate characters per line based on font size and max width
    avg_char_width = font_size * 0.6  # Rough estimate
    chars_per_line = int(max_width / avg_char_width)
    
    wrapped_lines = textwrap.wrap(formatted_quote, width=chars_per_line)
    
    # Calculate total text height
    line_height = font_size + 10
    total_text_height = len(wrapped_lines) * line_height
    
    # Adjust starting y to center the text block
    start_y = text_y - (total_text_height // 2)
    
    # Draw each line centered
    for i, line in enumerate(wrapped_lines):
        # Get the bounding box of the text
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        
        # Center the line
        line_x = text_x - (text_width // 2)
        line_y = start_y + (i * line_height)
        
        # Draw text in black
        draw.text((line_x, line_y), line, fill='black', font=font)
    
    # Save the output
    img.save(output_path, quality=95)
    print(f"Quote image saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_quote.py <quote_text> <output_path> [template_path]")
        print('Example: python generate_quote.py "Your quote here" output.jpg')
        sys.exit(1)
    
    quote = sys.argv[1]
    output = sys.argv[2]
    
    # Default template path (relative to script location)
    script_dir = Path(__file__).parent
    default_template = script_dir.parent / "assets" / "background_template.jpg"
    
    template = sys.argv[3] if len(sys.argv) > 3 else str(default_template)
    
    generate_quote_image(quote, output, template)
