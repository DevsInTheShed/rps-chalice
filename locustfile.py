from locust import HttpUser, task

# locust --headless --users 93 --spawn-rate 16 -H https://jo29imb6u1.execute-api.ap-southeast-2.amazonaws.com/api/
class DoStuff(HttpUser):
    @task
    def do_stuff(self):
        self.client.get("/")
        self.client.get("/index/")
        response = self.client.post("/result/", {"choice":"%F0%9F%93%9C", })
        print("Response status code:", response.status_code)
        print("Response text:", response.text)
        response = self.client.get("/result/")