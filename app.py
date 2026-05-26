import streamlit as st
import json
from agent.travel_agent import generate_trip

# Set page config
st.set_page_config(
    page_title="Vagabond - AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Premium Styling
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

    /* Global Typography & Background Override */
    .stApp {
        background: linear-gradient(135deg, #0b132b 0%, #1c2541 50%, #3a506b 100%);
        color: #ffffff;
        font-family: 'Outfit', sans-serif;
    }

    /* Main Container Padding */
    .main-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 2rem;
    }

    /* Glassmorphic Header Card */
    .header-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 3rem 2rem;
        text-align: center;
        backdrop-filter: blur(12px);
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        background-image: radial-gradient(circle at 10% 20%, rgba(98, 0, 234, 0.15) 0%, transparent 40%),
                          radial-gradient(circle at 90% 80%, rgba(0, 229, 255, 0.15) 0%, transparent 40%);
    }

    .header-card h1 {
        font-family: 'Outfit', sans-serif;
        font-weight: 800;
        font-size: 3.5rem;
        margin: 0;
        background: linear-gradient(90deg, #00E5FF, #7209B7, #FF007F);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
    }

    .header-card p {
        font-family: 'Outfit', sans-serif;
        font-weight: 300;
        font-size: 1.25rem;
        color: #B0C4DE;
        margin-top: 0.5rem;
        margin-bottom: 0;
    }

    /* Glassmorphic Input Card */
    .input-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 2rem;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        margin-bottom: 2rem;
    }

    /* Output Section Card */
    .output-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 2.5rem;
        backdrop-filter: blur(16px);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
        margin-top: 2rem;
        font-family: 'Outfit', sans-serif;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    .output-card h2, .output-card h3 {
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        color: #00E5FF;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 0.5rem;
        margin-top: 1.5rem;
    }

    .output-card strong {
        color: #FF007F;
    }

    /* Custom Streamlit Button Styling */
    div.stButton > button {
        background: linear-gradient(90deg, #7209B7 0%, #3F37C9 50%, #4CC9F0 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2.5rem;
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(114, 9, 183, 0.4);
        width: 100%;
        margin-top: 1rem;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(76, 201, 240, 0.6);
        background: linear-gradient(90deg, #FF007F 0%, #7209B7 50%, #00E5FF 100%);
        color: white;
    }

    div.stButton > button:active {
        transform: translateY(1px);
    }

    /* Styling Selectboxes and Numbers Inputs */
    label {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 500 !important;
        color: #B0C4DE !important;
        font-size: 0.95rem !important;
    }

    /* Subdued Success Notification */
    .stAlert {
        border-radius: 12px !important;
        background-color: rgba(0, 229, 255, 0.1) !important;
        color: #00E5FF !important;
        border: 1px solid rgba(0, 229, 255, 0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# Load list of cities dynamically from JSON
try:
    with open("data/flights.json", "r") as f:
        flights_data = json.load(f)
    sources = sorted(list(set(flight["source"] for flight in flights_data)))
    destinations = sorted(list(set(flight["destination"] for flight in flights_data)))
except Exception:
    # Fallback to robust lists if read fails
    sources = ["Bangalore", "Chennai", "Delhi", "Kolkata", "Mumbai"]
    destinations = ["Goa", "Jaipur", "Kerala", "Manali", "Srinagar"]

# App Container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Premium Header
st.markdown("""
<div class="header-card">
    <h1>VAGABOND</h1>
    <p>Premium Agentic AI Travel Planner</p>
</div>
""", unsafe_allow_html=True)

# Glassmorphic Input Form
st.markdown('<div class="input-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    source = st.selectbox(
        "🛫 Source City",
        options=sources,
        index=0
    )

with col2:
    destination = st.selectbox(
        "🛬 Destination City",
        options=destinations,
        index=0
    )

with col3:
    days = st.number_input(
        "📅 Days",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )

st.markdown('</div>', unsafe_allow_html=True)

# Action Trigger
if st.button("Generate Bespoke Itinerary"):
    if source and destination:
        if source == destination:
            st.error("Source and destination cities cannot be the same. Please pick a different destination.")
        else:
            with st.spinner("✨ Curating your perfect travel experience..."):
                try:
                    result = generate_trip(
                        source,
                        destination,
                        days
                    )
                    
                    st.success("🎉 Your Personalized Itinerary is Ready!")
                    
                    # Beautifully display the markdown result in the custom styled container
                    st.markdown('<div class="output-card">', unsafe_allow_html=True)
                    st.markdown(result)
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Failed to generate trip itinerary: {str(e)}")
    else:
        st.warning("Please specify both source and destination cities.")

st.markdown('</div>', unsafe_allow_html=True)