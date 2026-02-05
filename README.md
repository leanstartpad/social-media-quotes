# Social Media Quote Generator

A Claude skill for generating branded social media quote images for LinkedIn and X (Twitter).

## Overview

This skill automatically generates 1000x1000px quote images with Jeff 'SKI' Kinsey branding, featuring:
- Purple background with geometric line pattern
- Rye decorative font for quote text
- Fixed branding elements (logo, name, tagline, #27Rhinos hashtag)
- High-quality JPEG output suitable for social media posting

## Installation

### For Claude Users

1. Download the latest `.skill` file from the [Releases](../../releases) page
2. In Claude, go to Settings > Skills
3. Click "Upload Skill" and select the downloaded file
4. The skill will be available in all future conversations

### For Developers

Clone this repository:

```bash
git clone https://github.com/yourusername/social-media-quotes-skill.git
cd social-media-quotes-skill
```

## Usage

Once installed in Claude, simply ask:

```
"Create a quote image with 'Your quote text here'"
```

Claude will automatically generate the branded image and provide it for download.

## Manual Usage

You can also run the script directly:

```bash
python scripts/generate_quote.py "Your quote text" output.jpg
```

### Requirements

- Python 3.x
- Pillow (PIL): `pip install Pillow`

## Structure

```
social-media-quotes-skill/
├── SKILL.md                      # Skill instructions for Claude
├── assets/
│   ├── background_template.jpg  # Branded background template
│   └── Rye-Regular.ttf          # Rye font file
└── scripts/
    └── generate_quote.py        # Quote generation script
```

## Assets

### Background Template
- Dimensions: 1000x1000px at 144dpi
- Style: Lavender with geometric line pattern
- Branding: Logo, name, tagline, and hashtag pre-positioned

### Typography
- Font: Rye (Google Fonts)
- Size: 72pt
- Style: Decorative Western-style slab serif
- Text wrapping: Automatic, centered, 85% of image width

## Customization

To modify the skill:

1. Edit the files in this repository
2. Test changes locally with the Python script
3. Package the skill using Claude's packaging tools
4. Upload the new `.skill` file to Claude

## License

The Rye font is licensed under the SIL Open Font License 1.1 (see assets/OFL.txt)

## Version History

### 1.0.0 (2026-02-05)
- Initial release
- Rye font integration
- Automatic quote text wrapping
- 1000x1000px output format
