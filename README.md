# T20 Cricket Player Chatbot

A modern, interactive Streamlit app for exploring T20 cricket player stats and chatting with an AI analyst about strengths, style, and areas for improvement.

## Features

- **Player Sidebar**: Select from a list of simulated T20 stars.
- **Player Profile**: See key stats and a cricket-themed profile image.
- **Chatbot Interface**: Ask questions about the selected player; responses follow a two-paragraph, analytical format.
- **Simulated Data**: The repository includes sample stats for 10 well-known T20 players.

## Getting Started

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Run the app**
   ```
   streamlit run app.py
   ```

3. **OpenAI API Key**
   - Add your OpenAI API key to `.streamlit/secrets.toml`:
     ```
     OPENAI_API_KEY = "sk-..."
     ```
   - Or set it as the `OPENAI_API_KEY` environment variable.
   - If not set, simulated responses will be shown.

4. **Custom Data**
   - Replace `t20_player_stats.csv` with your own player stats for real analysis.

## Project Structure

- `app.py` - Main Streamlit app.
- `t20_player_stats.csv` - Simulated T20 player stats.
- `requirements.txt` - Dependencies.
- `README.md` - This file.

## Notes

- All AI responses are formatted as two paragraphs, each with 3–4 sentences, analyzing strengths and areas for improvement.
- Player images are generic cricket icons for demonstration.