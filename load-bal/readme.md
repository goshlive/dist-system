# Follow the instructions below to run:
1. Flask REST services handled by the load balancer will be available at:
```
http://localhost:9090
```
You may trigger the request by opening the browser and executing one of the following manually:
```
• http://localhost:9090/processImage
• http://localhost:9090/generateReport
```
Services are running on ports 7000, which are only accessible by internal services (service-to-service calls).

2. The load tester (Locust) will be available at:
```
http://localhost:8089
```
Generate multiple concurrent users and observe requests being distributed across Worker1, Worker2, and
Worker3.
