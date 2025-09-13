import streamlit as st
from datetime import datetime
import time
import random

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

funny_phrases = [
    # Tata
    "Tata, deja de buscar 'chicas malas' y empieza a buscar tu pasaporte. 🕶️",
    "Tata, no te pierdas antes del viaje... ¡te necesitamos en Río! 🍷",
    "Tata, controla la mandíbula, que en Río hay mucho para disfrutar. 😂",
    
    # Lucho
    "Lucho, ¡prepárate para renegar! En Río no te vamos a dejar ser tan cómodo. 😅",
    
    # Virche
    "Virche, endereza ese chasis antes de pisar la playa. 🚗",
    "Virche, en Río no hay tiempo para torceduras... ¡ponete las pilas! 👀",
    "Virche, deja el chupe ahora, que en Río hay mucho más para disfrutar. 🍺",
    
    # Farina
    "Farina, el petiso sin cogote, ya debe estar soñando con las playas de Río. 🏖️",
    "Farina, no te pongas temático con Talleres en Río... ¡relajate un poco! ⚽",
    "Farina, en Río no hay excusas para ser insoportable... ¡a disfrutar! 🌞",
    
    # Filo
    "Filo, si no llegás en forma, no importa... ¡pero llegá! 💪",
    "Filo, Río te espera, aunque el gimnasio no te haya visto mucho. 🏋️",
    "Filo, no te preocupes por ponerte en forma... no te dan los timepos ya 😄",
    
    # Martín
    "Martín, en Río hay buen comer... pero deja algo para los demás. 🍖",
    "Martín, las chicas malas te esperan en Río...  😏"
]
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

        # Mostrar frase aleatoria
        random_phrase = random.choice(funny_phrases)
        st.markdown(f"<h2 style='text-align: center; color: #FF5733;'>💬 {random_phrase}</h2>", unsafe_allow_html=True)
    
    time.sleep(1)
    st.rerun()