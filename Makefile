setup:
    pip install -r requirements.txt

run:
    python app.py

docker-build:
    docker build -t i200677 .

docker-run:
    docker run -p 4000:80 i200677

