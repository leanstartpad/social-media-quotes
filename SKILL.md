---
name: social-media-quotes
description: Generate branded social media quote images for LinkedIn and X (Twitter) with Jeff 'SKI' Kinsey branding. Use when the user requests quote graphics, social media posts, or wants to create shareable quote images with the established brand template (lavender background with geometric lines, logo, name, tagline, and #27Rhinos hashtag). Trigger on requests like 'create a quote image', 'make a social media post', 'generate a quote graphic', or any request to overlay text on the branded template.
---

# Social Media Quote Generator

Generate 1000x1000px quote images with Jeff 'SKI' Kinsey branding for LinkedIn and X.

## Quick Start

```bash
cd /home/claude
python /path/to/skill/scripts/generate_quote.py "Your quote text here" output.jpg
```

The script automatically:
- Uses the branded background template (lavender with geometric lines)
- Centers the quote text with quotation marks
- Preserves the fixed branding elements (logo, name, tagline, hashtag)
- Outputs a 1000x1000px image at 144dpi

## Template Assets

**Background template:** `assets/background_template.jpg`
- Pre-branded with logo (bottom left)
- Jeff 'SKI' Kinsey, Jonah / The Marketing Mad Man™ (bottom left)
- #27Rhinos hashtag (bottom right)
- Lavender background with geometric line pattern

## Script Usage

```bash
python scripts/generate_quote.py <quote_text> <output_path> [template_path]
```

**Arguments:**
- `quote_text`: The quote to display (quotation marks added automatically)
- `output_path`: Where to save the generated image
- `template_path`: Optional, defaults to `assets/background_template.jpg`

**Example:**
```bash
python scripts/generate_quote.py "You don't hire to fill a seat; you hire to remove a constraint." /mnt/user-data/outputs/quote.jpg
```

## Typography

The script uses the Rye font (a decorative Western-style slab serif from Google Fonts) stored in `assets/Rye-Regular.ttf`. Font size is 72pt with automatic text wrapping to fit within 85% of image width.

## Output

Images are saved as high-quality JPEGs (quality=95) at 1000x1000px, suitable for both LinkedIn and X posts.
