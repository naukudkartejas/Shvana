import collections
import collections.abc
collections.Mapping = collections.abc.Mapping  

from experta import *
import json
import pygame
import time

# Initialize Pygame Mixer for audio playback
pygame.mixer.init()

def play_alarm():
    try:
        pygame.mixer.music.load(r'alarm.mp3')
        pygame.mixer.music.play()
        print("🚨 CRITICAL HEALTH ALERT: Immediate Attention Needed!")
    except Exception as e:
        print(f"⚠️ Alarm failed to play: {e}")

# Define input structure
class DogVitals(Fact):
    """Dog health indicators"""
    pass

# Expert System
class DogHealthExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.critical_alert = False

    @Rule(DogVitals(temperature=P(lambda t: t > 39.5)))
    def fever(self):
        print("Detected: High Temperature (Fever)")
        self.critical_alert = True

    @Rule(DogVitals(heart_rate=P(lambda hr: hr > 160)))
    def tachycardia(self):
        print("Detected: Elevated Heart Rate (Tachycardia)")
        self.critical_alert = True

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
    with open(r'test_dog_vitals.json') as file:
        test_cases = json.load(file)

    for index, data in enumerate(test_cases, start=1):
        print(f"\n--- Test Case #{index} ---")
        engine = DogHealthExpert()
        engine.reset()
        engine.declare(DogVitals(**data))
        engine.run()

        if engine.critical_alert:
            play_alarm()

        
        time.sleep(5)
