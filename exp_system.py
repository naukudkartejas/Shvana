import collections
import collections.abc
collections.Mapping = collections.abc.Mapping  # Python 3.10+ fix

from experta import *
import json

# Define input structure
class DogVitals(Fact):
    """Dog health indicators"""
    pass

# Expert System
class DogHealthExpert(KnowledgeEngine):
    @Rule(DogVitals(temperature=P(lambda t: t > 39.5)))
    def fever(self):
        print("Detected: High Temperature (Fever)")

    @Rule(DogVitals(heart_rate=P(lambda hr: hr > 160)))
    def tachycardia(self):
        print("Detected: Elevated Heart Rate (Tachycardia)")

    @Rule(DogVitals(activity_level='low'))
    def low_activity(self):
        print("Detected: Low Activity Level")

    @Rule(DogVitals(voice='whining'))
    def whining_sound(self):
        print("Detected: Whining - Possible Distress")

    @Rule(DogVitals(motion='irregular'))
    def irregular_movement(self):
        print("Detected: Irregular Movement - Check for Injury or Anxiety")

    @Rule(DogVitals(gps_accuracy=P(lambda g: g < 5)))
    def gps_issue(self):
        print("Detected: GPS signal too weak (< 5m accuracy)")

# Load JSON and run
if __name__ == '__main__':
   
    with open(r'd:\shvana\expert system\test_dog_vitals.json') as file:

        input_data = json.load(file)

    
    engine = DogHealthExpert()
    engine.reset()
    engine.declare(DogVitals(**input_data))
    engine.run()
