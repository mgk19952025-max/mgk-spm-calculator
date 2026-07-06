import streamlit as st
import math
from PIL import Image

# إعدادات الصفحة
st.set_page_config(page_title="Khorshed SPM Tech", layout="centered")

# تنسيق الـ Dark Mode وتوضيح نصوص الإدخال
st.markdown("""
    <style>
    .stApp {background-color: #121212; color: #FFFFFF;}
    /* توضيح نصوص الإدخال */
    label {color: #FFFFFF !important; font-weight: bold !important;}
    h1 {color: #FFD700 !important; text-align: center;}
    div.stButton > button {width: 100%; background-color: #FFD700; color: #000000; font-weight: bold; border: none; padding: 10px;}
    </style>
    """, unsafe_allow_html=True)

# عرض اللوجو
try:
    logo = Image.open("logo.jpg")
    st.image(logo, use_column_width=True)
except:
    st.title("★ KHORSHED SPM TECH ★")

st.markdown("---")

# المدخلات
col1, col2 = st.columns(2)
with col1:
    D = st.number_input("OD (mm)", value=2600.0)
    t = st.number_input("Thickness (mm)", value=14.0)
    L = st.number_input("Length (m)", value=12.0)
with col2:
    Ws = st.number_input("Width (mm)", value=2000.0)
    V = st.number_input("Speed (m/min)", value=1.3)
    # إضافة خانة زمن القطع
    cut_time = st.number_input("Cut Time (sec)", value=10.0)

# الحسابات
if st.button("CALCULATE"):
    try:
        mod_D = D + (t * 2)
        circ = math.pi * mod_D
        cos_a = Ws / circ
        alpha = math.degrees(math.acos(cos_a))
        weight = ((D - t) * t * 0.02466 * L) / 1000
        
        strip_len = (1 / cos_a) * L
        strip_per_meter = 1 / cos_a
        weld_width = t + 4
        cap_height = t * 0.8
        
        # عرض النتائج
        st.subheader("Results:")
        r1, r2 = st.columns(2)
        r1.metric("Angle", f"{alpha:.2f}°")
        r2.metric("Weight", f"{weight:.3f} T")
        
        st.info(f"**Cut Time:** {cut_time} sec")
        st.info(f"**Modified Circumference:** {circ:.2f} mm")
        st.info(f"**Strip per meter:** {strip_per_meter:.4f} m")
        st.warning(f"**Weld Dimensions:** {weld_width:.1f} mm / {cap_height:.1f} mm")
        
    except:
        st.error("Check Inputs!")
