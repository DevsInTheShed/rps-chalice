from locust import HttpUser, task
import random



# locust --headless --users 93 --spawn-rate 16 -H https://jo29imb6u1.execute-api.ap-southeast-2.amazonaws.com/api/
class DoStuff(HttpUser):
    @task
    def do_stuff(self):
        options = ['🪨', '📜', '✂️']
        chosen_option = random.choice(options)

        print("doing gets...")
        self.client.get("/")
        self.client.get("/index/")

        print("doing errors...")
        self.client.get("/error/")

        print("doing posts...")

        response = self.client.post("/result/", {"choice":chosen_option, })
        print("Response status code:", response.status_code)
        print("Response text:", response.text)
        response = self.client.get("/result/")