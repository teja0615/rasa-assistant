## search milk checkout yes path
* greet
  - utter_greet
* grocery_provider{"grocery_type":"milk"}
  - utter_varieties_milk
* inform_milk{"milk_type":"Organic"}
  - utter_checkout
* affirm
  - utter_quantity
* quantity{"milk_qty":2}
  - action_price
* goodbye
  - utter_goodbye

# search whole milk checkout yes path
* greet
  - utter_greet
* grocery_provider{"grocery_type":"milk"}
  - utter_varieties_milk
* inform_milk{"milk_type":"Whole"}
  - utter_checkout
* affirm
  - utter_quantity
* quantity{"milk_qty":2}
  - action_price
* goodbye
  - utter_goodbye


## search whole milk checkout yes path
* greet
  - utter_greet
* grocery_provider{"grocery_type":"milk"}
  - utter_varieties_milk
* inform_milk{"milk_type":"Fatfree"}
  - utter_checkout
* affirm
  - utter_quantity
* quantity{"milk_qty":2}
  - action_price
* goodbye
  - utter_goodbye

## search milk checkout no path
* greet
  - utter_greet
* grocery_provider{"grocery_type":"milk"}
  - utter_varieties_milk
* inform_milk{"milk_type": "Organic"}
  - utter_checkout
* deny
  - utter_goodbye

## search hospital happy path
* greet
  - utter_greet
* search_provider{"facility_type":"hospital","location":"San Francisco"}
  - action_facility_search
  - slot{"address":"100 Ave D, San Francisco"}
* goodbye
  - utter_goodbye


## search hospital + location
* greet
  - utter_greet
* search_provider{"facility_type":"hospital"}
  - utter_ask_location
* inform{"location":"San Francisco"}
  - action_facility_search
  - slot{"address":"100 Ave D, San Francisco"}
* goodbye
  - utter_goodbye


## bot challenge
* bot_challenge
  - utter_iamabot
