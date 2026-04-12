import streamlit as st
import pickle
import pandas as pd

# load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎧 Song Mood Classifier")
st.subheader("Predict song mood using audio features")

# inputs
song_name = st.text_input("🎵 Enter Song Name")
user_feeling = st.text_input("💭 How are you feeling? (love, sad, party)")

st.write("### Adjust song features:")

danceability = st.slider("Danceability", 0.0, 1.0, 0.5)
energy = st.slider("Energy", 0.0, 1.0, 0.5)
loudness = st.slider("Loudness", -60.0, 0.0, -10.0)
speechiness = st.slider("Speechiness", 0.0, 1.0, 0.05)
acousticness = st.slider("Acousticness", 0.0, 1.0, 0.5)
instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.0)
liveness = st.slider("Liveness", 0.0, 1.0, 0.1)
valence = st.slider("Valence", 0.0, 1.0, 0.5)
tempo = st.slider("Tempo", 50, 200, 120)

if st.button("Predict Mood"):

    if song_name == "":
        st.warning("⚠️ Please enter song name")

    else:
        # feeling detection
        if user_feeling:
            feeling = user_feeling.lower()

            if "love" in feeling:
                st.info("❤️ Detected Feeling: Romantic")
                valence = 0.7
                energy = 0.4

            elif "sad" in feeling:
                st.info("😢 Detected Feeling: Sad")
                valence = 0.2
                energy = 0.3

            elif "party" in feeling or "happy" in feeling:
                st.info("🥳 Detected Feeling: Energetic")
                valence = 0.8
                energy = 0.9

            else:
                st.info("🙂 Neutral Feeling")

        # create dataframe
        sample = pd.DataFrame([{
            "danceability": danceability,
            "energy": energy,
            "loudness": loudness,
            "speechiness": speechiness,
            "acousticness": acousticness,
            "instrumentalness": instrumentalness,
            "liveness": liveness,
            "valence": valence,
            "tempo": tempo
        }])

        result = model.predict(sample)

        st.success(f"🎵 Song: {song_name}")
        st.success(f"🎧 Predicted Mood: {result[0]}")