# GitHub Repository Setup Instructions

## Step 1: Create a New Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `social-media-quotes-skill`
3. Description: "Claude skill for generating branded social media quote images"
4. Choose Public or Private (your preference)
5. Do NOT initialize with README (we already have one)
6. Click "Create repository"

## Step 2: Push Your Local Repository

After creating the repository on GitHub, run these commands in your terminal:

```bash
cd /path/to/social-media-quotes-repo

# Add the GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/social-media-quotes-skill.git

# Push to GitHub
git push -u origin master
```

If you prefer using SSH:

```bash
git remote add origin git@github.com:YOUR_USERNAME/social-media-quotes-skill.git
git push -u origin master
```

## Step 3: Create a Release (Optional)

To make it easy for others to download the .skill file:

1. Go to your repository on GitHub
2. Click "Releases" (right sidebar)
3. Click "Create a new release"
4. Tag version: `v1.0.0`
5. Release title: `Initial Release`
6. Upload the `social-media-quotes.skill` file
7. Click "Publish release"

## Repository URL

After setup, your repository will be at:
```
https://github.com/YOUR_USERNAME/social-media-quotes-skill
```

## Future Updates

When you make changes:

```bash
cd /path/to/social-media-quotes-repo
git add .
git commit -m "Description of changes"
git push
```

## Using Claude Code

If you want to work with this using Claude Code:

```bash
# Navigate to the repository
cd /path/to/social-media-quotes-repo

# Open in Claude Code
code .
```

Then you can ask Claude Code to help you modify the skill, test changes, and commit updates.
