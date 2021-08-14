from locust import HttpUser, task, between
import random



# locust --headless --users 93 --spawn-rate 16 -H https://858kop0oed.execute-api.ap-southeast-2.amazonaws.com/api
class DoStuff(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def do_gets(self):
        print("doing gets...")
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200:
                print("Get - Response status code:", response.status_code)
            else:
                print("Eep! Get - Response status code:", response.status_code)

    @task(1)
    def do_errors(self):
        print("doing errors...")
        with self.client.get("/error/", catch_response=True) as response:
            if response.status_code == 404:
                print("Get - Response status code:", response.status_code)
            else:
                print("Eep! Get - Response status code:", response.status_code)

    @task(3)
    def do_posts(self):
        print("doing posts...")
        options = ['🪨', '📜', '✂️']
        chosen_option = random.choice(options)
        response = self.client.post("/result/", {"choice":chosen_option})
        print("Post - Response status code:", response.status_code)