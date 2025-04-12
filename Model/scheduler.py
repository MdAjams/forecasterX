# scheduler.py

import schedule
import time
import os

# Define task functions
def run_feature_engineering():
    os.system("Feature Engineering.ipynb")

def run_model_training():
    os.system("Weather model training.ipynb")

# Schedule tasks
schedule.every().day.at("06:00").do(run_feature_engineering)
schedule.every().day.at("06:10").do(run_model_training)

print("Scheduler started. Running daily tasks...")

# Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(60)
