# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

'''
class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # a tracker keeps track of slots that are set at each dialogue stage.
        # values of slots can be returned by get slot method and providing the name of slot we would like to get
        facility= tracker.get_slot("facility_type")
        address=" 100 Ave D, San Francisco"
        dispatcher.utter_message("Here is the address of the {}:{}".format(facility,address))

        return [SlotSet("address",address)]
        # these events have to be reflected in training stories
        # For ex, if action_facility_search sets slot address, added line 6 in stories

'''
class ActionPrice(Action):
    def name(self) -> Text:
        return "action_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # a tracker keeps track of slots that are set at each dialogue stage.
        # values of slots can be returned by get slot method and providing the name of slot we would like to get
        
        #milk= tracker.get_slot("milk_type")
        #testvar="two dollars"
        #dispatcher.utter_message("Here is the price of {}:{}".format(milk,testvar))

        milk= tracker.get_slot("milk_type")
        quantvar=tracker.get_slot("milk_qty")
        price=0
        if(milk=="Organic"):
            price=2*int(quantvar)
        elif(milk=="Fatfree"):
            price=3*int(quantvar)
        else:
            price=4*int(quantvar)
        
        testvar="yo"
        

        
        dispatcher.utter_message("Total price: {}".format(price))
        return [SlotSet("testvar",testvar)]

        # these events have to be reflected in training stories
        # For ex, if action_facility_search sets slot address, added line 6 in stories
