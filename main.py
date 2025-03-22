from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Load the .kv file
# Builder.load_file('main.kv')

class WellnessApp(App):
    def calculate_score(self):
        # Access the sliders and label using their IDs
        mood = self.root.ids.mood_slider.value
        stress = self.root.ids.stress_slider.value
        sleep = self.root.ids.sleep_slider.value

        # Calculate the wellness score
        score = (mood + (10 - stress) + sleep) / 3

        # Generate recommendations
        recommendation = self.generate_recommendation(score)

        # Update the result label
        result_text = (
            f"📊 Wellness Assessment Results:\n"
            f"- 😊 Mood: {mood}/10\n"
            f"- 😓 Stress: {stress}/10\n"
            f"- 😴 Sleep Quality: {sleep}/10\n\n"
            f"🏆 Overall Wellness Score: {score:.1f}/10\n\n"
            f"📝 Personalized Recommendations:\n{recommendation}"
        )
        self.root.ids.result_label.text = result_text

    def generate_recommendation(self, score):
        if score > 7:
            return (
                "🌟 Great job! Maintain your positive habits:\n"
                "- Practice daily mindfulness\n"
                "- Keep a gratitude journal\n"
                "- Maintain consistent sleep patterns"
            )
        elif score >= 4:
            return (
                "💆‍♂️ Moderate stress detected:\n"
                "- Try guided meditation\n"
                "- Practice box breathing\n"
                "- Take regular movement breaks"
            )
        else:
            return (
                "🚨 High stress levels detected:\n"
                "- Contact a mental health professional\n"
                "- Reach out to a trusted friend\n"
                "- Try grounding techniques"
            )

if __name__ == '__main__':
    WellnessApp().run()