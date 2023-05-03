# Overview

This is a Python script that uses AWS S3 and Rekognition services to generate alternative tags for images in a specified S3 bucket. It prints the image file name and the corresponding alternative tags.

# Prerequisites

- AWS credentials set up with necessary permissions to access S3 and Rekognition services

# Setup

- Clone this repository
- Install the necessary packages by running `pipenv install`
- Activate the virtual environment by running `pipenv shell`
- Update the `bucket_name` variable in the script `generate_alt_tags.py` to the name of your S3 bucket
```python
bucket_name = '>>YOUR.S3.BUCKET.NAME.HERE<<'
```

# Usage
- Run the script with the command `python generate_alt_tags.py`

