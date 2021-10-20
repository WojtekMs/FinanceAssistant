# FinanceAssistant

# Requirements
- tesseract-ocr
- tesseract-ocr-pol
- git lfs
- requirements.txt

# Quick Start
It is up to you whether you want to use python virtualenv. As it is a good practice, commands listed below assume you have created and activated your virtual environment in the project root directory.

Download tesseract-ocr library.
`sudo apt-get install tesseract-ocr`

Download polish language files.
`sudo apt-get install tesseract-ocr-pol`

Install git LFS
`sudo apt-get install git-lfs

In case this is the first time you are using git LFS you have to set it up
`git lfs install`

Pull binary files from git lfs
`git lfs pull`

Download packages from requirements.txt
`pip install -r requirements.txt`

Launch script
`python ./print.py data/test.png`
