from locust import HttpUser, between, task
import json


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)
    
    @task
    def get_text_class(self):
        payload={"text":"I have a federal student loan"}
        header={'Content-Type':'application/json','Accept':'application/json'}
        self.client.post("/score",data=json.dumps(payload),headers=header, catch_response=False)