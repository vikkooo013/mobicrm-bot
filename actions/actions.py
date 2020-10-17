# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionCrm(Action):

    def name(self) -> Text:
        return "action_crm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
            choice = tracker.latest_message.get('text')
            requirement = choice
            response = """Oh good! We have the ideal {} tucked in serene and landscape setting for you.""".format (requirement)
            dispatcher.utter_message(response)
            return [SlotSet('inform', requirement)]
# class crmAction(Action):

#     def name(self):
#         return 'action_crm'

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         choice = tracker.get_slot('inform')
        
#         requirement = choice
#         response = """Oh good! We have the ideal {} tucked in serene and landscape setting for you.""".format (requirement)
       
#         dispatcher.utter_message(response)
#         return [SlotSet('inform', requirement)]


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[D - rule: Say goodbye anytime the user says goodbye
#     steps:
#       - intent: goodbye
#       - action: utter_goodbye

#   ict[Text, Any]]:
# #
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
