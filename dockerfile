FROM python:3.11

WORKDIR /fastapiapp

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "fastapiapp.main:fastapiapp", "--host", "0.0.0.0", "--port", "8000"]