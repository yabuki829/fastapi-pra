FROM python:3.11-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
