import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Global Med-Queue AI", layout="centered")

# Load dataset
df = pd.read_csv("HospitalsInIndia.csv")
df = df.dropna()

st.title("🏥 Global Med-Queue AI")
st.markdown("### Find hospitals and check estimated emergency wait time")

# City Input
city_input = st.text_input("🌍 Enter your City or Country")

if city_input:

    results = df[df["City"].str.lower() == city_input.lower()]

    if not results.empty:

        st.success(f"✅ Found {len(results)} hospitals in {city_input}")

        hospital_list = results["Hospital"].unique()

        selected_hospital = st.selectbox("🏨 Select a Hospital", hospital_list)

        if selected_hospital:

            # Simulated Live Data
            staff_count = random.randint(10, 50)
            available_seats = random.randint(0, 20)

            if available_seats > 10:
                emergency_level = "Low"
                color = "green"
            elif available_seats > 5:
                emergency_level = "Medium"
                color = "orange"
            else:
                emergency_level = "High"
                color = "red"

            estimated_wait = (50 - staff_count) + (20 - available_seats)

            st.markdown("---")
            st.subheader("📊 Live Hospital Status")

            col1, col2 = st.columns(2)

            col1.metric("👨‍⚕ Staff Count", staff_count)
            col2.metric("🪑 Available Seats", available_seats)

            st.markdown(f"### 🚨 Emergency Level: :{color}[{emergency_level}]")

            st.markdown(f"## ⏳ Estimated Wait Time: {estimated_wait} Minutes")

            st.markdown("---")
            st.subheader("🏥 Advice & Instructions")

            if emergency_level == "High":
                st.error("⚠ High emergency load. Visit only if urgent.")
            elif emergency_level == "Medium":
                st.warning("Moderate crowd. Expect some waiting time.")
            else:
                st.success("Low crowd. Faster service expected.")

            st.write("✔ Carry ID proof")
            st.write("✔ Bring previous medical reports")
            st.write("✔ Arrive 15 minutes early")

    else:
        st.error("❌ No hospitals found in this location. Try another city.")
