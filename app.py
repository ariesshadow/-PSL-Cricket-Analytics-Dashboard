import pandas as pd
import streamlit as st
import plotly.express as px

# Team Colors
team_colors = {
    "Lahore Qalandars": "#00A86B",
    "Karachi Kings": "#003DA5",
    "Peshawar Zalmi": "#F7A800",
    "Quetta Gladiators": "#6A0DAD",
    "Islamabad United": "#EE1C25",
    "Multan Sultans": "#00A3E0",
    "Islamabad United ": "#EE1C25",  # handles trailing space in data
}

def get_team_color(team):
    return team_colors.get(team, "#888888")

# Load data
df = pd.read_csv("psl_data.csv.csv")

st.title("🏏 PSL Cricket Analytics Dashboard")
st.markdown("Explore ball-by-ball data from PSL 2017–2025")

# ── Sidebar Filters ──────────────────────────────────────
st.sidebar.header("🔍 Filters")
seasons = ["All"] + sorted(df["season"].unique().tolist())
selected_season = st.sidebar.selectbox("Select Season", seasons)

if selected_season != "All":
    df = df[df["season"] == selected_season]

# ── Summary Stats ─────────────────────────────────────────
st.subheader("📊 Quick Stats")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Matches", df["match_id"].nunique())
col2.metric("Total Runs", f"{df['batsman_runs'].sum():,}")
col3.metric("Total Wickets", df["is_wicket"].sum())
col4.metric("Total Sixes", df[df["batsman_runs"] == 6]["batsman_runs"].count())

st.divider()

# ── Top Run Scorers ───────────────────────────────────────
st.subheader("🏏 Top 10 Run Scorers")
top_batters = (
    df.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
top_batters.columns = ["Player", "Runs"]
fig1 = px.bar(top_batters, x="Runs", y="Player", orientation="h",
              color="Runs", color_continuous_scale="sunset",
              title="Top 10 Run Scorers")
fig1.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig1, use_container_width=True)

# ── Top Wicket Takers ─────────────────────────────────────
st.subheader("🎯 Top 10 Wicket Takers")
wickets = df[df["is_wicket"] == True]
top_bowlers = (
    wickets.groupby("bowler")["is_wicket"]
    .count()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
top_bowlers.columns = ["Bowler", "Wickets"]
fig2 = px.bar(top_bowlers, x="Wickets", y="Bowler", orientation="h",
              color="Wickets", color_continuous_scale="teal",
              title="Top 10 Wicket Takers")
fig2.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig2, use_container_width=True)

# ── Team Win Rates ────────────────────────────────────────
st.subheader("🏆 Team Win Rates")
wins = df.groupby("winner")["match_id"].nunique().reset_index()
wins.columns = ["Team", "Wins"]
wins = wins[wins["Team"] != "None"].sort_values("Wins", ascending=False)
wins["Color"] = wins["Team"].apply(get_team_color)

fig3 = px.bar(wins, x="Team", y="Wins",
              color="Team",
              color_discrete_map=team_colors,
              title="Total Wins by Team")
st.plotly_chart(fig3, use_container_width=True)

# ── Runs Per Season ───────────────────────────────────────
st.subheader("📈 Total Runs Per Season")
runs_per_season = df.groupby("season")["batsman_runs"].sum().reset_index()
runs_per_season.columns = ["Season", "Total Runs"]
fig4 = px.line(runs_per_season, x="Season", y="Total Runs",
               markers=True, title="Run Trends Across Seasons",
               color_discrete_sequence=["#00d4ff"])
st.plotly_chart(fig4, use_container_width=True)

# ── Six Hitters ───────────────────────────────────────────
st.subheader("💥 Top Six Hitters")
sixes = df[df["batsman_runs"] == 6]
top_six_hitters = (
    sixes.groupby("batter")["batsman_runs"]
    .count()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
top_six_hitters.columns = ["Player", "Sixes"]
fig5 = px.bar(top_six_hitters, x="Sixes", y="Player", orientation="h",
              color="Sixes", color_continuous_scale="plasma",
              title="Top 10 Six Hitters")
fig5.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig5, use_container_width=True)

# ── Best Powerplay Teams ──────────────────────────────────
st.subheader("⚡ Best Powerplay Teams (Overs 1-6)")
powerplay = df[df["over"] <= 6]
powerplay_runs = (
    powerplay.groupby("batting_team")["batsman_runs"]
    .sum()
    .reset_index()
)
powerplay_runs.columns = ["Team", "Powerplay Runs"]
powerplay_runs = powerplay_runs.sort_values("Powerplay Runs", ascending=False)
powerplay_runs["Color"] = powerplay_runs["Team"].apply(get_team_color)

fig6 = px.bar(powerplay_runs, x="Team", y="Powerplay Runs",
              color="Team",
              color_discrete_map=team_colors,
              title="Total Powerplay Runs by Team")
st.plotly_chart(fig6, use_container_width=True)

# ── Player Profile Card ───────────────────────────────────
st.subheader("🪪 Player Profile Card")

all_players = sorted(df["batter"].unique().tolist())
selected_player = st.selectbox("Select a Player", all_players)

player_df = df[df["batter"] == selected_player]

total_runs = player_df["batsman_runs"].sum()
total_balls = len(player_df)
strike_rate = round((total_runs / total_balls) * 100, 2) if total_balls > 0 else 0
fours = player_df[player_df["batsman_runs"] == 4].shape[0]
sixes = player_df[player_df["batsman_runs"] == 6].shape[0]
matches = player_df["match_id"].nunique()
seasons_played = sorted(player_df["season"].unique().tolist())

st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("🏏 Total Runs", f"{total_runs:,}")
col2.metric("🎯 Strike Rate", strike_rate)
col3.metric("📅 Matches", matches)

col4, col5, col6 = st.columns(3)
col4.metric("4️⃣ Fours", fours)
col5.metric("6️⃣ Sixes", sixes)
col6.metric("🗓️ Seasons", len(seasons_played))

st.markdown(f"**Seasons Played:** {', '.join(map(str, seasons_played))}")

# Runs per season graph for that player
st.markdown(f"#### {selected_player}'s Runs Per Season")
player_season = player_df.groupby("season")["batsman_runs"].sum().reset_index()
player_season.columns = ["Season", "Runs"]
fig7 = px.bar(player_season, x="Season", y="Runs",
              color_discrete_sequence=["#00d4ff"],
              title=f"{selected_player} - Season by Season Runs")
st.plotly_chart(fig7, use_container_width=True)

# ── Player Profile Card ───────────────────────────────────
st.subheader("🪪 Player Profile Card")

all_players = sorted(df["batter"].unique().tolist())
selected_player = st.selectbox("Select a Player", all_players, key="player_select")

player_df = df[df["batter"] == selected_player]

total_runs = player_df["batsman_runs"].sum()
total_balls = len(player_df)
strike_rate = round((total_runs / total_balls) * 100, 2) if total_balls > 0 else 0
fours = player_df[player_df["batsman_runs"] == 4].shape[0]
sixes = player_df[player_df["batsman_runs"] == 6].shape[0]
matches = player_df["match_id"].nunique()
seasons_played = sorted(player_df["season"].unique().tolist())

st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("🏏 Total Runs", f"{total_runs:,}")
col2.metric("🎯 Strike Rate", strike_rate)
col3.metric("📅 Matches", matches)

col4, col5, col6 = st.columns(3)
col4.metric("4️⃣ Fours", fours)
col5.metric("6️⃣ Sixes", sixes)
col6.metric("🗓️ Seasons", len(seasons_played))

st.markdown(f"**Seasons Played:** {', '.join(map(str, seasons_played))}")

# Runs per season graph for that player
st.markdown(f"#### {selected_player}'s Runs Per Season")
player_season = player_df.groupby("season")["batsman_runs"].sum().reset_index()
player_season.columns = ["Season", "Runs"]
fig7 = px.bar(player_season, x="Season", y="Runs",
              color_discrete_sequence=["#00d4ff"],
              title=f"{selected_player} - Season by Season Runs")
