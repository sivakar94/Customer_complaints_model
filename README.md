# Customer_complaints_model
# new

Created Customer complaints Multi text classifier and served into a Scalable Flask application

• Processed the data, created a training pipeline using Tfidf vectorizer and Xgboost Algorithm

• Created a scalable Flask application using: Gunicorn and Ngnix

• Containerized the Application using Docker and Performed Load testing using Locust

# On your machine 
you can run the following command to run it:

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python Flask.py


Text the application with any input 
$ curl http://localhost:5000/score -d "{\"text\":\"I Have a federal student loan\"}" -H 'Content-Type: application/json'

# Now if you want to run on Docker


