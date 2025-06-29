import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def radar_batting(df, player):
    pdf = df[df['player'] == player].copy()
    if pdf.empty:
        st.warning("No data for selected player.")
        return

    avg = pdf['runs_scored'].sum() / max(pdf['times_out'].sum(),1)
    sr = pdf['runs_scored'].sum() / max(pdf['balls_faced'].sum(),1) * 100
    balls = pdf['balls_faced'].sum()
    thirties = (pdf['runs_scored'] >= 30).sum()
    fifties = (pdf['runs_scored'] >= 50).sum()

    categories = ['Average', 'Strike Rate', '30s', '50s', 'Balls Faced']
    values = [avg, sr, thirties, fifties, balls]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=player
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, showticklabels=True, ticks='')),
        showlegend=False,
        title=f"{player} Batting Radar"
    )
    st.plotly_chart(fig, use_container_width=True)

def batting_performance_bar(df, player):
    pdf = df[df['player'] == player].copy().sort_values('date')
    if pdf.empty:
        st.warning("No data for selected player.")
        return

    pdf['cum_runs'] = pdf['runs_scored'].cumsum()
    pdf['cum_outs'] = pdf['times_out'].cumsum()
    pdf['cum_avg'] = pdf['cum_runs'] / pdf['cum_outs'].replace(0, 1)

    x_vals = pd.to_datetime(pdf['date']) if 'date' in pdf else range(len(pdf))
    runs = pdf['runs_scored']
    cum_avg = pdf['cum_avg']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=x_vals,
        y=runs,
        name="Runs per Innings",
        marker_color='blue'
    ))
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=cum_avg,
        name="Cumulative Average",
        marker_color='orange',
        yaxis='y2'
    ))

    fig.update_layout(
        title=f"{player} Batting Performance Over Time",
        xaxis_title="Innings (by date)",
        yaxis=dict(title="Runs per innings", side='left'),
        yaxis2=dict(title="Cumulative Batting Average", side='right', overlaying='y'),
        legend=dict(orientation="h", y=1.1)
    )
    st.plotly_chart(fig, use_container_width=True)