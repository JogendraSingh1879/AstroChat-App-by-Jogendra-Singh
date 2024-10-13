import streamlit as st
from datetime import datetime
st.title("Astro Chat By Jogendra Singh(Experiment)")
st.image("astrochat banner.gif")
# Zodiac sign calculator based on date of birth
def get_zodiac_sign(day, month):
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    return astro_sign
    
# Placeholder for fetching horoscope (you can replace it with an API call)
def get_daily_horoscope(zodiac_sign):
    horoscopes = {
        "Aries": "Today is a great day to focus on new beginnings.",
        "Taurus": "Patience is key, stay grounded.",
        "Gemini": "Communication will lead to exciting opportunities.",
        "Cancer": "Focus on your emotional well-being.",
        "Leo": "Take charge and be confident in your decisions.",
        "Virgo": "Organization will help you achieve your goals.",
        "Libra": "Balance is crucial today, avoid conflicts.",
        "Scorpio": "Trust your intuition and embrace change.",
        "Sagittarius": "Adventure is calling, explore new possibilities.",
        "Capricorn": "Hard work will pay off, stay disciplined.",
        "Aquarius": "Innovation and creativity are your strengths today.",
        "Pisces": "Your compassion will create meaningful connections."
    }
    return horoscopes.get(zodiac_sign, "Zodiac sign not found.")

# Suggestions for life improvements (you can expand this with dynamic content)
def get_life_improvements(zodiac_sign):
    improvements = {
        "Aries": "Focus on setting clear goals and taking initiative.",
        "Taurus": "Practice mindfulness to stay present and reduce stress.",
        "Gemini": "Work on enhancing communication skills.",
        "Cancer": "Pay attention to your emotional health.",
        "Leo": "Focus on self-confidence and leadership skills.",
        "Virgo": "Improve organizational habits to stay productive.",
        "Libra": "Work on maintaining harmony in relationships.",
        "Scorpio": "Embrace flexibility and open-mindedness.",
        "Sagittarius": "Explore new hobbies and expand your knowledge.",
        "Capricorn": "Develop a long-term plan for success.",
        "Aquarius": "Engage in creative projects to boost innovation.",
        "Pisces": "Focus on empathy and understanding others."
    }
    return improvements.get(zodiac_sign, "No specific advice found.")

# Streamlit UI
st.title("Astrology & Daily Horoscope")

# Input for date of birth to find Zodiac Sign
st.header("Find Your Zodiac Sign")
dob = st.date_input("Enter your Date of Birth", datetime(2000, 1, 1))
zodiac_sign = get_zodiac_sign(dob.day, dob.month)

st.write(f"Your Zodiac Sign is: **{zodiac_sign}**")

# Select zodiac sign for daily horoscope
st.header("Daily Horoscope")
zodiac_options = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 
                  'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
user_zodiac = st.selectbox("Select your Zodiac Sign", zodiac_options)

if st.button("Get Horoscope"):
    horoscope = get_daily_horoscope(user_zodiac)
    st.subheader(f"Today's Horoscope for {user_zodiac}:")
    st.write(horoscope)

    improvements = get_life_improvements(user_zodiac)
    st.subheader("Life Improvement Tips:")
    st.write(improvements)

