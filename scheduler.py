import schedule
import time
import subprocess

def run_prediction():
    subprocess.run(["python", "/app/src/predict_penguin.py"])

# Schedule the task to run every day at specific times
schedule.every().day.at("07:30").do(run_prediction)

while True:
    schedule.run_pending()
    time.sleep(1)
