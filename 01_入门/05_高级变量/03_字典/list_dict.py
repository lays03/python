card_list = [{"name": "小明",
              "age": 18,
              "tele": "12345"},
             {"name": "小红",
              "age": 17,
              "tele": "999"}]

print(card_list[0])

temp_dict = {"gender": "male"}

card_list[0].update(temp_dict)

for card_dict in card_list:
    print(card_dict)
    

