# ✈️ Travel Booking Multi-Agent

An AI-powered multi-agent system that helps you search for flights, gather travel information, and plan trips — all through a simple Streamlit interface.

## Features

- 🔍 **Flight Search** — Query real-time flight data (airline, departure/arrival airports, status) based on your search input.
- 🌍 **Travel Info Search** — Uses the Tavily search API to pull up-to-date travel-related information (destinations, tips, local info, etc.).
- 🤖 **Multi-Agent Architecture** — Specialized tools/agents work together to plan a trip based on your query.
- 💻 **Streamlit Frontend** — Simple, interactive web UI to interact with the agents.

## Project Structure

```
travel_booking/
├── tools/
│   ├── __init__.py
│   ├── flight_tool.py       # Flight search tool
│   └── tavily_tool.py       # Tavily-based travel search tool
├── travel_plans/             # Generated/stored travel plans
├── frontend.py                # Streamlit frontend entry point
├── main.py                    # Core agent logic
├── requirement.txt            # Python dependencies
└── .env                        # API keys (not committed)
```

## Getting Started

### Prerequisites

- Python 3.9+
- API keys for the flight data provider and [Tavily](https://tavily.com/)

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/RISHIKESH-kumaar/travelling-multiagent
   cd travelling-multiagent
   ```

2. Create a virtual environment

   ```bash
   python -m venv venv
   venv\Scripts\activate       # Windows
   source venv/bin/activate    # macOS/Linux
   ```

3. Install dependencies

   ```bash
   pip install -r requirement.txt
   ```

4. Set up environment variables

   Create a `.env` file in the root directory:

   ```
   API_KEY=your_flight_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

### Running the App

```bash
streamlit run frontend.py
```

This will launch the app in your browser, where you can enter a travel query and get flight results and trip suggestions.

## How It Works

1. You enter a travel query through the Streamlit UI.
2. The system routes the query to the relevant tool(s):
   - `flight_tool.py` fetches flight options matching your query.
   - `tavily_tool.py` searches the web for relevant travel information.
3. Results are combined and presented back to you as a trip overview.

## Tech Stack

- Python
- Streamlit
- Tavily Search API
- Flight data API

## Roadmap

- [ ] Hotel search integration
- [ ] End-to-end booking support
- [ ] Multi-city trip planning
- [ ] Improved agent memory/context across sessions

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
