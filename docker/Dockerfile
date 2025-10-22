FROM python:3

WORKDIR /app

# installing audio dependencies: eye3D and audio tools
RUN apt-get update && apt-get install -y libmagic1 ffmpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint /entrypoint

ENTRYPOINT ["/bin/bash", "/entrypoint"]