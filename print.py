#!/usr/bin/env python

import argparse
import pytesseract
from PIL import Image

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="image to read text from")
    args = parser.parse_args()
    text = pytesseract.image_to_string(Image.open(args.image), lang="pol")
    print(text)


if __name__ == "__main__":
    main()
