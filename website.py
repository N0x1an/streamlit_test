import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import base64

# Page config - must be first
st.set_page_config(
    page_title="LCT StreamLit Demo Dash",
    page_icon="💾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to completely transform the appearance
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Remove padding */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    
    /* Custom background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Custom header */
    .custom-header {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    /* Glass morphism cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: transform 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
    }
    
    /* Custom metrics */
    .custom-metric {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 10px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .custom-metric:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(0,0,0,0.4);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    /* Custom buttons */
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    /* Custom sidebar */
    .css-1d391kg {
        background: rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(10px);
    }
    
    /* Custom dataframe */
    .stDataFrame {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        overflow: hidden;
    }
    
    /* Custom text styling */
    .custom-title {
        font-size: 3rem;
        font-weight: bold;
        color: white;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 10px;
    }
    
    .custom-subtitle {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.8);
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Animated elements */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    
    /* Custom progress bars */
    .custom-progress {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        overflow: hidden;
        height: 20px;
        margin: 10px 0;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    /* Custom tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 5px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        margin: 0 5px;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(255, 255, 255, 0.2);
        color: white;
    }
    
    /* Custom form styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        padding: 10px;
    }
    
    .stSelectbox > div > div > div {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 10px;
    }
    
    /* Hide Streamlit branding */
    .css-1rs6os {
        display: none;
    }
    
    .css-17ziqus {
        display: none;
    }
    
    /* Custom notification styles */
    .success-box {
        background: linear-gradient(45deg, #56ab2f, #a8e6cf);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .warning-box {
        background: linear-gradient(45deg, #f093fb, #f5576c);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Custom chart containers */
    .chart-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Custom JavaScript for advanced interactions
st.markdown("""
<script>
    // Custom JavaScript functionality
    function updateProgress(elementId, value) {
        document.getElementById(elementId).style.width = value + '%';
    }
    
    // Add click effects
    document.addEventListener('DOMContentLoaded', function() {
        // Add ripple effect to cards
        const cards = document.querySelectorAll('.glass-card');
        cards.forEach(card => {
            card.addEventListener('click', function(e) {
                const ripple = document.createElement('span');
                const rect = card.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;
                
                ripple.style.cssText = `
                    position: absolute;
                    width: ${size}px;
                    height: ${size}px;
                    background: rgba(255,255,255,0.3);
                    border-radius: 50%;
                    transform: translate(${x}px, ${y}px) scale(0);
                    animation: ripple 0.6s ease-out;
                    pointer-events: none;
                `;
                
                card.appendChild(ripple);
                setTimeout(() => ripple.remove(), 600);
            });
        });
    });
</script>
""", unsafe_allow_html=True)

# Custom header with animation
st.markdown("""
<div class="custom-header">
    <div class="custom-title floating">💾 LCT Dashboard</div>
    <div class="custom-subtitle">Streamlit demo for LCT python webapp</div>
</div>
""", unsafe_allow_html=True)

# Create custom navigation
navigation = st.container()
with navigation:
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; justify-content: center; gap: 20px;">
            <div style="color: #2c3e50; font-weight: bold; cursor: pointer; padding: 10px 20px; background: #e9ecef; border-radius: 20px;">📊 Analytics</div>
            <div style="color: #6c757d; font-weight: bold; cursor: pointer; padding: 10px 20px; background: #f8f9fa; border-radius: 20px;">📈 Reports</div>
            <div style="color: #6c757d; font-weight: bold; cursor: pointer; padding: 10px 20px; background: #f8f9fa; border-radius: 20px;">⚙️ Settings</div>
            <div style="color: #6c757d; font-weight: bold; cursor: pointer; padding: 10px 20px; background: #f8f9fa; border-radius: 20px;">👤 Profile</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Custom metrics row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="custom-metric">
        <div class="metric-label">Total Sales</div>
        <div class="metric-value">$125,430</div>
        <div style="font-size: 0.9rem;">↗️ +12.5%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="custom-metric">
        <div class="metric-label">Active Users</div>
        <div class="metric-value">8,742</div>
        <div style="font-size: 0.9rem;">↗️ +5.2%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="custom-metric">
        <div class="metric-label">Conversion Rate</div>
        <div class="metric-value">3.47%</div>
        <div style="font-size: 0.9rem;">↘️ -0.8%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="custom-metric">
        <div class="metric-label">Revenue Growth</div>
        <div class="metric-value">24.8%</div>
        <div style="font-size: 0.9rem;">↗️ +3.1%</div>
    </div>
    """, unsafe_allow_html=True)

# Custom progress indicators using Streamlit components
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #2c3e50; margin-bottom: 20px;">📊 Progress Indicators</h3>', unsafe_allow_html=True)

# Sales Target
st.markdown('<div style="color: #495057; margin-bottom: 5px; font-weight: 500;">Sales Target</div>', unsafe_allow_html=True)
st.progress(0.75)
st.markdown('<div style="color: #6c757d; font-size: 0.9rem; margin-bottom: 15px;">75% Complete</div>', unsafe_allow_html=True)

# Project Completion  
st.markdown('<div style="color: #495057; margin-bottom: 5px; font-weight: 500;">Project Completion</div>', unsafe_allow_html=True)
st.progress(0.45)
st.markdown('<div style="color: #6c757d; font-size: 0.9rem; margin-bottom: 15px;">45% Complete</div>', unsafe_allow_html=True)

# Team Performance
st.markdown('<div style="color: #495057; margin-bottom: 5px; font-weight: 500;">Team Performance</div>', unsafe_allow_html=True)
st.progress(0.90)
st.markdown('<div style="color: #6c757d; font-size: 0.9rem; margin-bottom: 15px;">90% Complete</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Custom interactive form in glass morphism style
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #2c3e50; margin-bottom: 20px;">🔧 Control Panel</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        user_name = st.text_input("👤 User Name", placeholder="Enter your name...")
        department = st.selectbox("🏢 Department", ["Sales", "Marketing", "Engineering", "HR"])
        
    with col2:
        priority = st.slider("⚡ Priority Level", 1, 10, 5)
        enable_notifications = st.checkbox("🔔 Enable Notifications", value=True)
    
    if st.button("🚀 Execute Action", type="primary"):
        st.markdown("""
        <div class="success-box">
            ✅ Action executed successfully! Settings updated for user: {user_name}
        </div>
        """.format(user_name=user_name), unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Custom charts with styling
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h4 style="color: #2c3e50; margin-bottom: 15px;">📈 Revenue Trends</h4>', unsafe_allow_html=True)
    
    # Generate sample data
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    revenue_data = pd.DataFrame({
        'Date': dates,
        'Revenue': np.random.randint(1000, 5000, 30) + np.arange(30) * 50
    })
    
    fig = px.line(revenue_data, x='Date', y='Revenue', 
                  title="",
                  color_discrete_sequence=['#4ECDC4'])
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#2c3e50',
        showlegend=False
    )
    fig.update_xaxes(gridcolor='#e9ecef')
    fig.update_yaxes(gridcolor='#e9ecef')
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h4 style="color: #2c3e50; margin-bottom: 15px;">🥧 Category Distribution</h4>', unsafe_allow_html=True)
    
    # Generate pie chart data
    categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Sports']
    values = [23, 17, 35, 12, 13]
    
    fig_pie = px.pie(values=values, names=categories,
                     color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
    fig_pie.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#2c3e50',
        showlegend=True
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Custom data table with advanced styling
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<h3 style="color: #2c3e50; margin-bottom: 20px;">📋 Advanced Data Table</h3>', unsafe_allow_html=True)

# Generate sample data
sample_data = pd.DataFrame({
    'ID': range(1, 11),
    'Product': [f'Product {i}' for i in range(1, 11)],
    'Category': np.random.choice(['Electronics', 'Clothing', 'Food'], 10),
    'Price': np.random.uniform(10, 500, 10).round(2),
    'Stock': np.random.randint(0, 100, 10),
    'Status': np.random.choice(['✅ Active', '⚠️ Low Stock', '❌ Out of Stock'], 10)
})

# Apply custom styling to dataframe
def highlight_rows(row):
    if '❌' in str(row['Status']):
        return ['background-color: rgba(255, 107, 107, 0.3)'] * len(row)
    elif '⚠️' in str(row['Status']):
        return ['background-color: rgba(255, 193, 7, 0.3)'] * len(row)
    else:
        return ['background-color: rgba(78, 205, 196, 0.3)'] * len(row)

styled_df = sample_data.style.apply(highlight_rows, axis=1)
st.dataframe(styled_df, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Custom tabs with advanced content
tab1, tab2, tab3 = st.tabs(["📊 Analytics", "⚙️ Settings", "🔔 Notifications"])

with tab1:
    st.markdown("""
    <div class="glass-card">
        <h4 style="color: #2c3e50;">Advanced Analytics Dashboard</h4>
        <p style="color: #6c757d;">Real-time data visualization and insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom heatmap data
    heatmap_data = np.random.rand(10, 10)
    fig_heatmap = px.imshow(heatmap_data, 
                           color_continuous_scale='Viridis',
                           title="Performance Heatmap")
    fig_heatmap.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#2c3e50'
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

with tab2:
    st.markdown("""
    <div class="glass-card">
        <h4 style="color: #2c3e50;">System Configuration</h4>
        <p style="color: #6c757d;">Customize your dashboard experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Theme", ["Dark", "Light", "Auto"], key="theme")
        st.slider("Refresh Rate (seconds)", 1, 60, 5, key="refresh")
    with col2:
        st.multiselect("Active Modules", ["Sales", "Inventory", "Reports", "Analytics"])
        st.checkbox("Auto-save", value=True)

with tab3:
    st.markdown("""
    <div class="glass-card">
        <h4 style="color: #2c3e50;">Notification Center</h4>
        <p style="color: #6c757d;">Stay updated with real-time alerts</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Custom notification cards
    notifications = [
        ("🎉", "New sale recorded", "2 minutes ago", "success"),
        ("⚠️", "Low stock alert", "15 minutes ago", "warning"),
        ("📈", "Monthly target achieved", "1 hour ago", "success"),
        ("🔔", "System update available", "3 hours ago", "info")
    ]
    
    for icon, title, time, type_class in notifications:
        color = "#4ECDC4" if type_class == "success" else "#FF6B6B" if type_class == "warning" else "#45B7D1"
        st.markdown(f"""
        <div style="
            background: #ffffff;
            border-left: 4px solid {color};
            padding: 15px;
            margin: 10px 0;
            border-radius: 0 10px 10px 0;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border: 1px solid #e9ecef;
        ">
            <div style="color: #2c3e50; font-weight: bold;">{icon} {title}</div>
            <div style="color: #6c757d; font-size: 0.9rem;">{time}</div>
        </div>
        """, unsafe_allow_html=True)

# Custom footer
st.markdown("""
<div class="glass-card" style="margin-top: 50px; text-align: center;">
    <div style="color: #2c3e50; font-size: 1.1rem; margin-bottom: 10px;">
        LCT TEST DASH
    </div>
</div>
""", unsafe_allow_html=True)