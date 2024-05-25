# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=dispatcher.tracker.get_slot("full_name")

        if not name:
            dispatcher.utter_message("Thank you, GoodCalo specialises in meal plans (weekly and monthly).")
        else:
            dispatcher.utter_message(f"Thank you {name}, GoodCalo specialises in meal plans (weekly and monthly).")


        return []
