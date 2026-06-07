from locust import HttpUser, task
import random

class DemoUser(HttpUser):

    @task
    def random_request(self):

        endpoint = random.choice([
            "/processImage",
            "/generateReport"
        ])

        self.client.get(endpoint)

