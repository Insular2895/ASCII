# ASCII Banner Kit

A small utility to store, generate, manage, and reuse ASCII banners inside terminal tools, scripts, and CLI projects.

This project lets you keep a library of ASCII banners and quickly display one when a program starts.

---

## Folder structure

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
│   └── banner.txt
├── show_banner.py
└── README.md
```

---

## How it works

There are two important folders:

```txt
banners/ = your full ASCII banner library
assets/banner.txt = the default active banner
```

### `banners/`

This folder stores all your available banners.

Example:

```txt
banners/Goku.txt
banners/Diable.txt
banners/Robin.txt
```

You can display one of them by name:

```bash
python3 show_banner.py Goku
```

### `assets/banner.txt`

This is the default banner.

When you run:

```bash
python3 show_banner.py
```

the script displays:

```txt
assets/banner.txt
```

So if you want `Goku.txt` to be the default banner, run:

```bash
cp banners/Goku.txt assets/banner.txt
```

If you want `Diable.txt` to be the default banner, run:

```bash
cp banners/Diable.txt assets/banner.txt
```

---

## Generate ASCII banners from images

You can create ASCII banners from `.jpg`, `.jpeg`, or `.png` images.

This project mainly uses `jp2a`, which works best with JPEG images.

---

### Install jp2a

On macOS:

```bash
brew install jp2a
```

Check installation:

```bash
jp2a --version
```

---

### Convert one JPEG image to ASCII

Example:

```bash
jp2a --width=100 ascii-assets/img_here/IMG_6770.jpeg > banners/IMG_6770.txt
```

Then test it:

```bash
python3 show_banner.py IMG_6770
```

To make it the default banner:

```bash
cp banners/IMG_6770.txt assets/banner.txt
```

---

### Convert all JPEG images to ASCII

Put your images in:

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

Then convert the JPEG to ASCII:

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

Then convert all `.jpg` images to ASCII:

```bash
for img in ascii-assets/img_here/*.jpg; do
  name=$(basename "$img" .jpg)
  jp2a --width=100 "$img" > "banners/$name.txt"
done
```

---

### Test different widths

If the result is not clean, try different widths:

```bash
jp2a --width=80 ascii-assets/img_here/logo.jpg > banners/logo_w80.txt
jp2a --width=120 ascii-assets/img_here/logo.jpg > banners/logo_w120.txt
jp2a --width=160 ascii-assets/img_here/logo.jpg > banners/logo_w160.txt
```

Then preview:

```bash
cat banners/logo_w120.txt
```

---

### Invert the rendering

Some dark images look better with inverted rendering:

```bash
jp2a --width=120 --invert ascii-assets/img_here/logo.jpg > banners/logo_invert.txt
```

---

### Recommended image settings

For better results:

```txt
Use high-contrast images
Avoid complex backgrounds
Prefer logos, faces, icons, silhouettes
Use width between 80 and 120 for terminal display
Avoid huge ASCII outputs for README files
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

Put your ASCII file inside `banners/`:

```txt
banners/my_banner.txt
```

Then test it:

```bash
python3 show_banner.py my_banner
```

To make it the default banner:

```bash
cp banners/my_banner.txt assets/banner.txt
```

---

## Use this inside another Python project

In your other project, create this structure:

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

## Use this inside another Node.js project

In your Node.js project, create:

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

## Important note about GitHub

The banner does not appear during `git clone`.

When someone runs:

```bash
git clone https://github.com/username/project.git
```

GitHub only downloads the files. It does not execute your code.

The banner appears when the user runs your tool, for example:

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
3. Store generated banners in banners/
4. Choose one default banner
5. Copy it to assets/banner.txt
6. Call show_banner() at the start of your project
7. Push the project to GitHub
```

---

## Best practices

Keep banners readable:

```txt
Recommended width: 80 to 120 characters
Recommended height: less than 40 lines
Format: .txt
Best use: terminal startup, CLI tools, install scripts
Avoid: huge photo-style ASCII blocks in README files
```

For GitHub README visuals, use a real image instead:

```md
![Project Banner](assets/banner.png)
```

Use ASCII mainly inside terminals.

---

## License

MIT
