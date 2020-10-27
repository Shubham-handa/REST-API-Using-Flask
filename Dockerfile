# Step 1 select default OS image
FROM alpine

# Step 2 Setting up environment
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

# Step 3 Configure a software
WORKDIR /greendeck

# Installing dependencies
COPY /requirements.txt /greendeck

RUN pip3 install -r requirements.txt

# Copying project files.
COPY ["MongoDB Greendecktask1.py", "/greendeck"]

# Exposing an internal port
EXPOSE 8005

# Step 4 set default commands
ENTRYPOINT [ "python3" ]

# These commands will be replaced if user provides any command by himself
CMD ["MongoDB Greendecktask1.py"]
