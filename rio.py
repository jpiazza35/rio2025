import streamlit as st
from datetime import datetime
import time

st.set_page_config(
    page_title="🏖️ Contador Río 2025",
    page_icon="🇧🇷",
    layout="centered"
)

def calculate_time_remaining():
    vacation_date = datetime(2025, 10, 9, 9, 30, 0)
    now = datetime.now()
    
    if now >= vacation_date:
        return None, "¡YA ESTAMOS EN RÍO! 🏖️🇧🇷"
    
    time_diff = vacation_date - now
    days = time_diff.days
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds % 3600) // 60
    seconds = time_diff.seconds % 60
    
    return time_diff, days, hours, minutes, seconds

def show_progress_bar(days_remaining, total_days=365):
    progress = max(0, (total_days - days_remaining) / total_days)
    return progress

# Interfaz principal
st.title("🏖️ CONTADOR VACACIONES RÍO 2025 🇧🇷")
st.markdown("---")

# Placeholder para actualización automática
placeholder = st.empty()

# Auto-refresh cada segundo
while True:
    with placeholder.container():
        result = calculate_time_remaining()
        
        if result[0] is None:
            st.success(result[1])
            st.balloons()
            break
        
        time_diff, days, hours, minutes, seconds = result
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Días", days)
        with col2:
            st.metric("Horas", hours)
        with col3:
            st.metric("Minutos", minutes)
        with col4:
            st.metric("Segundos", seconds)
        
        st.markdown(f"### ✈️ Vuelo: 9 de Octubre 2025 - 9:30 AM")
        st.markdown(f"🕐 *Ahora:* {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Barra de progreso
        progress = show_progress_bar(days)
        st.progress(progress)
        st.markdown(f"📊 Progreso hacia Río: {progress*100:.1f}%")
        
        # Mensajes motivacionales
        if days <= 1:
            st.error("🚨 ¡MAÑANA ES EL GRAN DÍA!")
        elif days <= 7:
            st.warning("🔥 ¡ÚLTIMA SEMANA!")
        elif days <= 30:
            st.info("🌟 ¡MENOS DE UN MES!")
        else:
            st.success("🏖️ Paciencia... ¡Río te está esperando!")
    
    time.sleep(1)
    st.rerun()