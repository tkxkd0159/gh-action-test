FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cahce-dir -r requirements.txt

COPY . .
CMD [ "python", "./main.py"]