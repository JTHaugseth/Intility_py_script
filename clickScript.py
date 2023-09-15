import requests
import time

while True:
    response = requests.get("https://intility-games.intility.com/scoreboard?_data=routes%2Fscoreboard")
    scoreboard = response.json()
    
    print("GET request posted")

    first_place_name = scoreboard[0]['name']
    first_place_score = scoreboard[0]['score']

    

    your_new_score = first_place_score + 1

    print("New score found, posting new highscore")
        
    payload = {
            'name': 'Julian Haugseth',  
            'number': '40087795',  
            'score': 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858369,
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
    
    time.sleep(500)