FROM python:3.10.6-slim
RUN useradd --create-home --shell /bin/bash fetch_user
WORKDIR /home/fetch_user
COPY requirements.txt ./
USER fetch_user
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT [ "python", "fetch.py" ]