import streamlit as st

class ParadoxQuest:
    def __init__(self):
        self.score = 0
        self.scenarios = [
            {
                "situation": "Your company is at a crossroads: launch an unfinished product now to gain market share, or delay for a perfect release?",
                "options": {
                    "A": "Launch now and iterate based on customer feedback (Paradox Mindset)",
                    "B": "Delay and perfect before release (Traditional Approach)",
                    "C": "Beta launch with limited users while refining (Balanced Approach)"
                },
                "correct": "C",
                "explanation": "A balanced approach maximizes learning while managing risk."
            },
            {
                "situation": "Your top team is burning out due to intense work culture. Do you…",
                "options": {
                    "A": "Push harder—this is a make-or-break moment (High Pressure)",
                    "B": "Encourage breaks but maintain deadlines (Manage Discomfort)",
                    "C": "Redesign work schedules for sustainable productivity (Long-Term Thinking)"
                },
                "correct": "C",
                "explanation": "Long-term sustainable work culture fosters retention and performance."
            }
        ]

    def play(self):
        st.title("🧩 Paradox Quest - Leadership Challenge")
        st.write("Navigate key leadership challenges wisely!")

        for scenario in self.scenarios:
            st.subheader(scenario["situation"])
            choice = st.radio("Choose an option:", list(scenario["options"].values()))

            if choice == scenario["options"][scenario["correct"]]:
                st.success("✅ Correct! " + scenario["explanation"])
                self.score += 1
            else:
                st.error("❌ Not quite! " + scenario["explanation"])

        st.write(f"### Your final score: {self.score}/{len(self.scenarios)}")
        if self.score == len(self.scenarios):
            st.success("🎉 Excellent leadership! You mastered paradox management.")
        elif self.score >= len(self.scenarios) // 2:
            st.info("👍 Good job! Some decisions were strong, but there's room for growth.")
        else:
            st.warning("⚠️ Leadership is tough! Consider refining your paradox mindset.")

if __name__ == "__main__":
    game = ParadoxQuest()
    game.play()
