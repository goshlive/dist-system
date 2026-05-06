# Please follow the instructions below to run:
1. Make sure you have Docker and RabbitMQ running on your system.<br>
   Docker Desktop can be downloaded from [here](https://www.docker.com/get-started/).<br>
   RabbitMQ can be downloaded from [here](https://www.rabbitmq.com/). Alternatively, for Windows, use rabbitmq-server-4.3.0.exe from [here](https://github.com/rabbitmq/rabbitmq-server/releases)
3. Execute services: RabbitMQ + worker + result:
   ```
   root-dir> docker compose up -d --build rabbitmq
   root-dir> docker compose up -d --build worker
   root-dir> docker compose up -d --build result
   ```
   OR, if you want to use three (more) workers:
   ```
   root-dir> docker compose up -d --build --scale rabbitmq
   root-dir> docker compose up -d --build --scale worker=3 worker
   root-dir> docker compose up -d --build --scale result
4. Send “payment request”:
   ```
   docker compose run --rm producer python producer.py
   docker compose run --rm producer python producer.py 120000 VA_MANDIRI
   docker compose run --rm producer python producer.py 50000 QRIS
6. Check the worker outpur
   ```
   docker compose logs -f worker
8. To remove all services:
   ```
   docker compose down
10. Check the RabbitMQ Management at: http://localhost:15672
    ```
    user: guest/guest
