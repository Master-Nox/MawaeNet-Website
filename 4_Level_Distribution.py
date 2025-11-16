import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Alyra Level Distribution", layout="wide")

# Initialize session state for population
if "total_pop" not in st.session_state:
    st.session_state.total_pop = 300000

# Initialize session state for rarity settings
if "commoner_pct" not in st.session_state:
    st.session_state.commoner_pct = 80.0
if "profession_pct" not in st.session_state:
    st.session_state.profession_pct = 10.0
if "level1_pct" not in st.session_state:
    st.session_state.level1_pct = 10.0
if "rarity_divisor" not in st.session_state:
    st.session_state.rarity_divisor = 2.0
if "use_log_scale" not in st.session_state:
    st.session_state.use_log_scale = False

st.title("Alyra Population Level Distribution")
st.write(
    """
    This tool uses the Alyra level rarity rule:

    **Each level past 1st is half as common as the level before it.**

    Distribution:
    - 80% Commoners  
    - 10% Stat Block / Profession NPCs  
    - 10% Level 1  
    - Beyond that , each level is half as common as the previous level.
    """
)

# --- INPUT ---
col_input1, col_input2 = st.columns([3, 1])

with col_input1:
    st.session_state.total_pop = st.number_input(
        "Enter total population:", min_value=1, value=st.session_state.total_pop, step=1000, format="%i"
    )

# Population presets
with col_input2:
    st.write("**Presets:**")
    preset_col1, preset_col2, preset_col3 = st.columns(3)
    with preset_col1:
        if st.button("Village", use_container_width=True):
            st.session_state.total_pop = 300
            st.rerun()
        if st.button("Town", use_container_width=True):
            st.session_state.total_pop = 3000
            st.rerun()
    with preset_col2:
        if st.button("Small City", use_container_width=True):
            st.session_state.total_pop = 10000
            st.rerun()
        if st.button("Large City", use_container_width=True):
            st.session_state.total_pop = 50000
            st.rerun()
    with preset_col3:
        if st.button("Capital City", use_container_width=True):
            st.session_state.total_pop = 300000
            st.rerun()
        if st.button("Kingdom", use_container_width=True):
            st.session_state.total_pop = 1000000
            st.rerun()

total_pop = st.session_state.total_pop

# --- RARITY TUNING SLIDERS ---
with st.expander("⚙️ Rarity Configuration"):
    col_tuning1, col_tuning2, col_tuning3 = st.columns(3)

    with col_tuning1:
        st.session_state.commoner_pct = st.slider("Commoner %", min_value=0.0, max_value=100.0, value=st.session_state.commoner_pct, step=1.0)

    with col_tuning2:
        st.session_state.profession_pct = st.slider("Profession NPC %", min_value=0.0, max_value=100.0, value=st.session_state.profession_pct, step=1.0)

    with col_tuning3:
        st.session_state.level1_pct = st.slider("Level 1 %", min_value=0.0, max_value=100.0, value=st.session_state.level1_pct, step=1.0)

    st.session_state.rarity_divisor = st.slider("Rarity Divisor (how much each level reduces)", min_value=1.5, max_value=4.0, value=st.session_state.rarity_divisor, step=0.1)

commoner_pct = st.session_state.commoner_pct / 100.0
profession_pct = st.session_state.profession_pct / 100.0
level1_pct = st.session_state.level1_pct / 100.0
rarity_divisor = st.session_state.rarity_divisor

# --- LEVEL LABELS ---
levels = (
    ["Commoner (0)", "Profession (0)", "1"] +
    [str(i) for i in range(2, 21)]
)

# --- RARITY CURVE ---
percentages = [
    commoner_pct,      # Commoner
    profession_pct,    # Profession
    level1_pct,        # Level 1
]

# Levels 2–20
p = level1_pct / rarity_divisor  # Level 2 base percent
for _ in range(2, 21):
    percentages.append(p)
    p /= rarity_divisor

# --- CALCULATE COUNTS ---
counts = [int(total_pop * pct) for pct in percentages]

df = pd.DataFrame({
    "Level": levels,
    "Percent": [f"{pct*100:.6f}%" for pct in percentages],
    "Estimated Count": counts
})

# --- LAYOUT ---
col1, col2 = st.columns(2)
with col1:
    st.subheader("Level Distribution Table")
    st.dataframe(df, width='stretch', hide_index=True)
with col2:
    st.subheader("Class Level Chart")
    st.session_state.use_log_scale = st.checkbox("Use Log Scale", value=st.session_state.use_log_scale)
    use_log_scale = st.session_state.use_log_scale
    
    # Build numeric level column for sorting
    numeric_levels = list(range(1, 21))   # 1 through 20

    chart_df = pd.DataFrame({
        "Level": numeric_levels,     # levels 1–20
        "Count": counts[2:]
    })

    fig = px.bar(chart_df, x="Level", y="Count", text="Count")
    fig.update_traces(textposition="outside")
    fig.update_xaxes(tickmode="linear", tick0=1, dtick=1)
    if use_log_scale:
        fig.update_yaxes(type="log")
    st.plotly_chart(fig, use_container_width=True, )

# --- SUMMARY ---
st.subheader("Summary")

highest_level_with_people = max(i for i, c in enumerate(counts) if c > 0)
st.write(f"**Highest Level:** {levels[highest_level_with_people]}")

total_classed = sum(counts[2:])
st.write(f"**Total # of classed individuals:** {total_classed:,}")