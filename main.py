from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button

class WellnessApp(App):
    def build(self):
        return BoxLayout()

    def calculate_score(self):
        mood = self.root.ids.mood_slider.value
        stress = self.root.ids.stress_slider.value
        sleep = self.root.ids.sleep_slider.value

        score = (mood + (10 - stress) + sleep) / 3
        recommendation = self.generate_recommendation(score)

        result_text = f"📊 Wellness Assessment Results:\n- 😊 Mood: {mood}/10\n- 😓 Stress: {stress}/10\n- 😴 Sleep Quality: {sleep}/10\n\n🏆 Overall Wellness Score: {score:.1f}/10\n\n📝 Personalized Recommendations:\n{recommendation}"
        self.root.ids.result_label.text = result_text

    def generate_recommendation(self, score):
        if score > 7:
            return ("🌟 Great job! Maintain your positive habits:\n"
                    "- Practice daily mindfulness\n"
                    "- Keep a gratitude journal\n"
                    "- Maintain consistent sleep patterns")
        elif score >= 4:
            return ("💆‍♂️ Moderate stress detected:\n"
                    "- Try guided meditation\n"
                    "- Practice box breathing\n"
                    "- Take regular movement breaks")
        else:
            return ("🚨 High stress levels detected:\n"
                    "- Contact a mental health professional\n"
                    "- Reach out to a trusted friend\n"
                    "- Try grounding techniques")

if __name__ == '__main__':
    WellnessApp().run()