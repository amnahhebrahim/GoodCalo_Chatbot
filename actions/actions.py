# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher


ALLOWED_PERIODS = ["monthly", "weekly"]
ALLOWED_MEALPLANS = ["one", "two", "three", "1", "2", "3"]

#
class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot("full_name")

        if not name:
            dispatcher.utter_message("Thank you, GoodCalo specialises in meal plans (weekly and monthly).")
        else:
            dispatcher.utter_message(f"Thank you {name}, GoodCalo specialises in meal plans (weekly and monthly).")


        return []

class validate_registration_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_registration_form"
    
    def validate_type_plan(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """validate type_plan Value"""

        if slot_value.lower() not in ALLOWED_PERIODS:
            dispatcher.utter_message(text=f"We only accept weekly or monthly subscriptions")
            return {"type_plan": None}
        dispatcher.utter_message(text=f"Ok, I've registered you as a {slot_value} user")
        return {"type_plan": slot_value}


    def validate_quantity_meals(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """validate Quantity Meals Value"""

        if slot_value not in ALLOWED_MEALPLANS:
            dispatcher.utter_message(text=f"We only accept one, two, or three meal plan subscriptions")
            return {"quantity_meals": None}
        dispatcher.utter_message(text=f"Ok, You have been registered for a  {slot_value} meal plan")
        return {"quantity_meals": slot_value}