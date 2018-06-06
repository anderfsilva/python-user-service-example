FROM python:3.6-alpine

# Install MySQL Client
RUN apk add --no-cache mariadb-dev build-base

# Expose ports
EXPOSE 5000

# Set the default directory
WORKDIR /mnt/app

# Add application requirements file
ADD requirements.txt requirements.txt

# Get pip to install requirements
RUN pip install -r requirements.txt

# Add application source code
ADD . /mnt/app

# Set the default command to execute
CMD python app.py