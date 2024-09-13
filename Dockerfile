FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install "fastapi[standard]"

EXPOSE 80
COPY . .
CMD [ "fastapi", "run", "main.py", "--port", "80" ]