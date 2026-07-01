FROM python:3.13
WORKDIR /usr/local/app

RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
rm -rf /var/lib/apt/lists/* 

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copy in the source code
COPY . .
EXPOSE 5000


CMD ["python", "app.py"]
