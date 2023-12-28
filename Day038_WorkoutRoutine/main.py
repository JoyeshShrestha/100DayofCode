import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

NUTRITION_API = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Tell me what exercise did you do?: ")

nutrition_parameters = {
    "query" : exercise
}
headers = {
    "x-app-id":os.environ["NUTRITION_APP_ID"],
    "x-app-key":os.environ["NUTRITION_APPLICATION_KEY"]
}
response = requests.post(url=NUTRITION_API,json=nutrition_parameters,headers=headers)

response.raise_for_status()

data = response.json()

exercises_names = []

today = datetime.now()


google_sheet_url = "https://api.sheety.co/c3d7f3385565659f15f302b3f8c6e736/myWorkouts/workouts"

workout_response = requests.get(google_sheet_url)

actual_date = today.strftime(f"%Y/%m/%d")

actual_time = today.strftime(f"%X")

exercise_list = []

for exercise in data["exercises"]:
    try:
        name= exercise['name']
    except:
        name = "NONE"
    try:
        duration = exercise["duration_min"]
    except:
        duration = "NONE"


    try:
        calories = exercise["nf_calories"]
    except:
        calories="NONE"
    exercise_dict = {
        "workout":{
        "date":actual_date,
        "time":actual_time,
        "exercise":name,
        "duration":duration,
        "calories":calories,

    }
    }
    exercise_list.append(exercise_dict)

auth=(
      os.environ["SHEETY_USERNAME"], 
      os.environ["SHEETY_PASSWORD"],
  )
header_sheety = {
    "Authorization":os.environ["Authorization_sheety"]
}
for every in exercise_list:
    post_workout_response = requests.post(url=google_sheet_url,json=every,auth=auth)

# post_workout_response.raise_for_status()

    print(post_workout_response.json())

