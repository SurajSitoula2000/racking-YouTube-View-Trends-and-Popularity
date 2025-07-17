# Tracking-YouTube-View-Trends-and-Popularity
#  Overview
This project is a data analytics tool that uses the YouTube Data API v3 to fetch real-time video data (views, likes, comments) based on a search query and visualizes engagement trends. It helps in understanding video performance, viewer behavior, and content strategy insights using Python, Pandas, and Streamlit.

# Features
1. Fetch video data (views, likes, comments, published date) via keyword/topic
2. Sort and visualize top-performing content
3. Analyze views vs likes correlation
4. Generate weekly view trends using time-series plots
5. Live dashboard with Streamlit

# Tech Stack
| Category        | Tools/Libraries                |
| ----------------| ------------------------------ |
| API             | YouTube Data API v3            |
| Language        | Python                         |
| Data Handling   | Pandas                         |
| Visualization   | Matplotlib, Seaborn, Streamlit |
| Others          | Google API Client, dotenv      |

# Installation Steps
git clone https://github.com/yourusername/youtube-trend-analyzer.git
cd youtube-trend-analyzer
pip install -r requirements.txt

Create a .env file and add:
YOUTUBE_API_KEY=your_actual_api_key_here

Run the App
streamlit run streamlit_app.py

# Use Cases
1. Content creators analyzing their niche.
2. Marketing teams monitoring viral trends.
3. Data analysts exploring engagement patterns.

# Learnings & Takeaways
1. Worked with a live API (YouTube Data API)
2. Applied data wrangling, cleaning, and formatting with Pandas
3. Developed meaningful visualizations from real-time data
4. Deployed an interactive dashboard with Streamlit

# Future Improvements
1. Add support for channel-based tracking
2. Integrate sentiment analysis from comments
3. Deploy live via Streamlit Cloud or Hugging Face Spaces

