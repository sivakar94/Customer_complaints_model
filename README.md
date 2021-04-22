# Customer Complaints Prediction

Created Customer complaints Multi text classifier which given a complaint will output the right complaint category:
- Debt collection
- Mortgage
- Credit card
- Bank account or service
- Student loan

![Application](images/Consumer.png)

1) Processed the data, created a training pipeline using Tfidf vectorizer and Xgboost Algorithm

![Traning_pipeline](images/Training_pipeline.png)

2) Created a scalable Flask application using: Gunicorn and Ngnix

![Flask_Application](images/FLASK.png)

3) Containerized the Application using Docker and Performed Load testing using Locust

![Locust1](images/Locust1.png)
![Locust1](images/Locust2.png)
![Locust1](images/Locust3.png)
![Locust1](images/Locust4.png)


# Running on your local machine 
Clone the repository 
you can run the following command to run it:

### Create your environment
$ python -m venv .venv

### Activate your environment
$ source .venv/bin/activate

### Installing dependecies
$ pip install -r requirements.txt

### Run the Flask application
$ python Flask.py

### Text the application with any input 
$ curl http://localhost:5000/score -d "{\"text\":\"I Have a federal student loan\"}" -H 'Content-Type: application/json'

### Now let's Load test it with locust with the following command
$ locust -f loadtest.py

#### Try to Simulate it with a different number of users and see how the latency is affected 







