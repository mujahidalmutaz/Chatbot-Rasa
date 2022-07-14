from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from resi import Resi


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_resi_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        no_resi = tracker.get_slot("rc")
        text = Resi(no_resi)
        dispatcher.utter_message(text=f"{text}") 
        return []