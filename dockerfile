# Download ubuntu from docker hub
FROM python:3-alpine

# Declaring working directory in our container
WORKDIR /opt/apps/playlistmanager

# Copy all relevant files to our working dir /opt/apps/playlistmanager
COPY requirements.txt .

# Install all requrements for our app
RUN pip3 install -r requirements.txt

# Copy source files to $WORKDIR
COPY . . 

# Expose container port to outside host
EXPOSE 6969

# Run the application
CMD [ "python3", "-u", "/opt/apps/playlistmanager/main.py" ]