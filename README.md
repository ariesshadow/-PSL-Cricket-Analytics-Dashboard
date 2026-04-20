🏏PSL-Cricket-Analytics-Dashboard
An interactive data analytics dashboard built with Python and Streamlit, analyzing ball-by-ball data from the Pakistan Super League (PSL) seasons 2017–2025.

🚀 Live Demo
> https://v74p63d6qjaffj7if9gxd5.streamlit.app/

📊 Features

- **Top 10 Run Scorers** — All-time and per season
- **Top 10 Wicket Takers** — Best bowlers across PSL history
- **Team Win Rates** — Which franchise dominates?
- **Run Trends Per Season** — How has scoring evolved over the years?
- **Top Six Hitters** — Who hits the most sixes?
- **Season Filter** — Filter every chart by a specific PSL season
- **Best Powerplay Teams** — Which team dominates overs 1-6?
- **Team Color Themes** — Each franchise represented in their official colors
- **Player Profile Cards** — Search any player for their complete PSL stats

🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Pandas | Data cleaning and analysis |
| Streamlit | Interactive web dashboard |
| Plotly | Data visualizations |

📁 Dataset

- **Source:** Kaggle — PSL Complete Dataset (2016–2025)
- **Size:** 73,000+ rows of ball-by-ball delivery data
- **Columns:** match_id, date, season, venue, batting_team, bowling_team, batter, bowler, runs, wickets, and more

⚙️ How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/psl-dashboard.git
cd psl-dashboard
```

2. **Install dependencies**
```bash
pip install pandas streamlit plotly seaborn matplotlib
```

3. **Add the dataset**
- Download the PSL dataset from Kaggle
- Place it in the project folder as `psl_data.csv`

4. **Run the app**
```bash
streamlit run app.py
```

5. Open your browser at `http://localhost:8501`

📸 Some Screenshots

<img width="904" height="570" alt="image" src="https://github.com/user-attachments/assets/4a0e9879-7380-4e72-bac1-c536ace04976" />
<img width="848" height="573" alt="image" src="https://github.com/user-attachments/assets/0cfbc58a-2588-4446-afb0-a5ebe85f12f6" />

🙋‍♀️ Author

**Om e Kalsoom**
📧 ummekalsoom0085daum@gmail.com
💼 [LinkedIn](https://www.linkedin.com/in/om-e-kalsoom-5a7405347)
🎓 BS Computer Science | University of the Punjab

📌 Future Improvements

- Player vs Player comparison
- Toss impact analysis
- Venue-wise batting/bowling stats
- Economy rate leaderboard for bowlers

⭐ If you found this useful, give it a star on GitHub!
