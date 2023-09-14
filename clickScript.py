import requests
import time

while True:
    response = requests.get("https://intility-games.intility.com/scoreboard?_data=routes%2Fscoreboard")
    scoreboard = response.json()
    
    print("GET request posted")

    first_place_name = scoreboard[0]['name']
    first_place_score = scoreboard[0]['score']

    if first_place_name != "Julian Haugseth":

        your_new_score = first_place_score + 1

        print("New score found, posting new highscore")
        
        payload = {
            'name': 'Julian Haugseth',  
            'number': '40087795',  
            'score': your_new_score,
            'school': 'HØyskolen Kristiania'  
        }

        response = requests.post(
            "https://intility-games.intility.com/?index=&_data=routes%2Findex",
            data=payload,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            }
        )

        print(response.status_code)
    
    time.sleep(120)