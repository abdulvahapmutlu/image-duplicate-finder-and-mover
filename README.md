# Image Duplicate Finder and Mover

This Python script helps in identifying and moving duplicate images within a specified directory to a designated duplicates folder. Utilizing perceptual hashing (phash) from the `imagehash` library, the script ensures that visually similar images are detected even if they have different filenames or slight variations.

## Features:
- Duplicate Detection: Identifies duplicate images using perceptual hashing.
- Automatic Moving: Moves detected duplicates to a specified folder.
- Supported Formats: Handles .png, .jpg, .jpeg, .bmp, and .gif files.

## Requirements:
- Python 3.x
- `Pillow` library
- `imagehash` library

## Installation:
```
pip install pillow imagehash

```

## Usage:
1. Set the path to the directory containing your images.
2. Define the path to the folder where duplicates should be moved.
3. Run the script to find and move duplicate images.

## License:
This project is licensed under the MIT License. 

Feel free to contribute or report issues on the GitHub repository!
