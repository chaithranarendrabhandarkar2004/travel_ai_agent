# ✈️ Vagabond – AI Travel Planner

An AI-powered travel planning application built with Python and Streamlit. Vagabond helps users generate personalized travel itineraries by selecting their source city, destination city, and trip duration.

## 🌟 Features

- Select a source city and destination city.
- Choose your trip duration (1–10 days).
- Generate a personalized travel itinerary.
- Interactive and user-friendly Streamlit interface.
- Custom-designed interface with a modern gradient theme.
- Loads flight information from JSON data.

## 🛠️ Technologies Used

- **Python** – Main programming language
- **Streamlit** – Web application interface
- **JSON** – Flight data handling
- **Agent-based architecture** – Travel itinerary generation

## 📁 Project Structure

```text
travel_ai_agent/
│
├── agent/          # Agent-related modules
├── assets/         # Project assets
├── data/           # Data files
├── tools/          # Supporting tools
├── utils/          # Utility modules
│
├── app.py          # Main Streamlit application
├── pyproject.toml  # Project configuration
├── uv.lock         # Dependency lock file
└── README.md       # Project documentation
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/chaithranarendrabhandarkar2004/travel_ai_agent.git
```

### 2. Open the project folder

```bash
cd travel_ai_agent
```

### 3. Install dependencies

If the project dependencies are configured in `pyproject.toml`, install them using:

```bash
uv sync
```

### 4. Run the application

```bash
uv run streamlit run app.py
```

## 🖥️ How It Works

1. Open the Vagabond application.
2. Select your departure city.
3. Select your destination city.
4. Choose the number of travel days.
5. Click **Generate Bespoke Itinerary**.
6. View your generated travel itinerary.

## 🎯 Project Goal

The goal of Vagabond is to explore how Python, AI agents, and interactive web applications can make travel planning easier and more convenient.

---

**Developed with Python and Streamlit.**
