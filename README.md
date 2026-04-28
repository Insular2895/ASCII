<div align="center">

# ASCII Banner Kit

Store, generate, manage, and reuse ASCII banners for terminal tools, scripts, and CLI projects.

<p>
  <img src="https://img.shields.io/badge/Python-CLI%20Utility-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python CLI Utility">
  <img src="https://img.shields.io/badge/ASCII-Art-black?style=for-the-badge" alt="ASCII Art">
  <img src="https://img.shields.io/badge/Terminal-Friendly-111111?style=for-the-badge&logo=gnubash&logoColor=white" alt="Terminal Friendly">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
</p>

<p>
  Generate ASCII banners from images, keep a reusable banner library, and plug them into any terminal-based project.
</p>

</div>

---

## Preview

<img width="800" height="300" alt="image" src="https://github.com/user-attachments/assets/917289bd-fcfa-440a-9d31-7316c005a8e4" />

---


This repository helps you:

- convert images into ASCII `.txt` banners
- keep all banners in a reusable library
- choose one default active banner
- display banners when your terminal tool starts
- reuse the same system in Python or Node.js projects

---

## Project structure

```txt
ASCII/
├── ascii-assets/
│   └── img_here/
│       ├── logo.png
│       ├── image.jpeg
│       └── ...
├── banners/
│   ├── Goku.txt
│   ├── Diable.txt
│   ├── Robin.txt
│   └── ...
├── assets/
│   ├── banner.txt
│   └── preview.png
├── show_banner.py
└── README.md
```

---

## Core idea

There are two important folders:

```txt
banners/ = full ASCII banner library
assets/banner.txt = current default banner
```

### `banners/`

This folder contains all your saved ASCII banners.

Example:

```txt
banners/Goku.txt
banners/Diable.txt
banners/Robin.txt
```

You can display one by name:

```bash
python3 show_banner.py Goku
```

### `assets/banner.txt`

This file is the active default banner.

When you run:

```bash
python3 show_banner.py
```

the script displays:

```txt
assets/banner.txt
```

To make `Goku.txt` your default banner:

```bash
cp banners/Goku.txt assets/banner.txt
```

To make `Diable.txt` your default banner:

```bash
cp banners/Diable.txt assets/banner.txt
```

---

## Features

- Generate ASCII banners from `.jpg`, `.jpeg`, and `.png`
- Organize banners in a clean library
- Set one default banner for easy reuse
- Display a specific or random banner
- Reuse the same banner system across projects
- Simple integration for Python and Node.js

---

## Install dependencies

This project mainly uses `jp2a`, which works best with JPEG images.

### macOS

```bash
brew install jp2a
```

Check installation:

```bash
jp2a --version
```

---

## Generate ASCII banners from images

### Convert one JPEG image to ASCII

```bash
jp2a --width=100 ascii-assets/img_here/IMG_6770.jpeg > banners/IMG_6770.txt
```

Test it:

```bash
python3 show_banner.py IMG_6770
```

Make it the default banner:

```bash
cp banners/IMG_6770.txt assets/banner.txt
```

---

### Convert all JPEG images to ASCII

Put your source images in:

```txt
ascii-assets/img_here/
```

Then run:

```bash
for img in ascii-assets/img_here/*.jpeg; do
  name=$(basename "$img" .jpeg)
  jp2a --width=100 "$img" > "banners/$name.txt"
done
```

This creates:

```txt
banners/IMG_1174.txt
banners/IMG_6770.txt
banners/...
```

---

### Convert PNG to JPEG first

If your source image is a `.png`, convert it to `.jpg` first using macOS `sips`:

```bash
sips -s format jpeg ascii-assets/img_here/logo.png --out ascii-assets/img_here/logo.jpg
```

Then convert it to ASCII:

```bash
jp2a --width=100 ascii-assets/img_here/logo.jpg > banners/logo.txt
```

---

### Convert all PNG images to JPEG

```bash
for img in ascii-assets/img_here/*.png; do
  name=$(basename "$img" .png)
  sips -s format jpeg "$img" --out "ascii-assets/img_here/$name.jpg"
done
```

Then convert all `.jpg` files to ASCII:

```bash
for img in ascii-assets/img_here/*.jpg; do
  name=$(basename "$img" .jpg)
  jp2a --width=100 "$img" > "banners/$name.txt"
done
```

---

### Test different widths

If the output is not clean enough, try different widths:

```bash
jp2a --width=80 ascii-assets/img_here/logo.jpg > banners/logo_w80.txt
jp2a --width=120 ascii-assets/img_here/logo.jpg > banners/logo_w120.txt
jp2a --width=160 ascii-assets/img_here/logo.jpg > banners/logo_w160.txt
```

Preview one result:

```bash
cat banners/logo_w120.txt
```

---

### Invert rendering

Some dark images look better inverted:

```bash
jp2a --width=120 --invert ascii-assets/img_here/logo.jpg > banners/logo_invert.txt
```

---

### Recommended source image settings

For better results:

```txt
Use high-contrast images
Avoid complex backgrounds
Prefer logos, icons, faces, silhouettes
Use width between 80 and 120 for terminal display
Avoid giant ASCII outputs for README usage
```

---

## Commands

### List all banners

```bash
python3 show_banner.py --list
```

### Show the default banner

```bash
python3 show_banner.py
```

### Show a specific banner

```bash
python3 show_banner.py Goku
```

### Show a random banner

```bash
python3 show_banner.py --random
```

---

## Add a new banner

Put your ASCII `.txt` file inside `banners/`:

```txt
banners/my_banner.txt
```

Then test it:

```bash
python3 show_banner.py my_banner
```

To make it your default banner:

```bash
cp banners/my_banner.txt assets/banner.txt
```

---

## Use this in another Python project

Create this structure:

```txt
my-project/
├── assets/
│   └── banner.txt
├── main.py
└── README.md
```

Copy the banner you want:

```bash
mkdir -p assets
cp path/to/ASCII/banners/Goku.txt assets/banner.txt
```

Then add this to your Python code:

```python
from pathlib import Path

def show_banner():
    banner_path = Path(__file__).parent / "assets" / "banner.txt"

    if banner_path.exists():
        print(banner_path.read_text(encoding="utf-8"))
```

Call it when your program starts:

```python
def main():
    show_banner()
    print("Starting program...")

if __name__ == "__main__":
    main()
```

Now when someone runs:

```bash
python3 main.py
```

the banner appears in the terminal.

---

## Use this in another Node.js project

Create this structure:

```txt
my-project/
├── assets/
│   └── banner.txt
├── index.js
└── package.json
```

Copy a banner:

```bash
mkdir -p assets
cp path/to/ASCII/banners/Goku.txt assets/banner.txt
```

Then add this to your Node.js code:

```js
const fs = require("fs");
const path = require("path");

function showBanner() {
  const bannerPath = path.join(__dirname, "assets", "banner.txt");

  if (fs.existsSync(bannerPath)) {
    console.log(fs.readFileSync(bannerPath, "utf8"));
  }
}

showBanner();
console.log("Starting program...");
```

Run:

```bash
node index.js
```

---

## Important GitHub note

The banner does **not** appear during `git clone`.

When someone runs:

```bash
git clone https://github.com/username/project.git
```

GitHub only downloads the files. It does not execute your code.

The banner appears when the user runs the project, for example:

```bash
python3 main.py
```

or:

```bash
npm start
```

or:

```bash
./install.sh
```

This is normal and safer.

---

## Recommended workflow

```txt
1. Put source images in ascii-assets/img_here/
2. Convert images to ASCII .txt files
3. Store all generated banners in banners/
4. Choose one default banner
5. Copy it to assets/banner.txt
6. Call show_banner() at startup
7. Push the project to GitHub
```

---

## Best practices

```txt
Recommended width: 80 to 120 characters
Recommended height: under 40 lines
Format: .txt
Best use: terminal startup, CLI tools, install scripts
Avoid: huge photo-style ASCII blocks in README files
```

For GitHub visuals, prefer a real image like:

```md
![Preview](assets/preview.png)
```

Use ASCII mainly inside the terminal, and regular images for README presentation.

---

## License

MIT
