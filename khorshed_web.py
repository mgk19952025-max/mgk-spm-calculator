import streamlit as st
import math
from PIL import Image

# 1. إعدادات الصفحة
st.set_page_config(page_title="Khorshed SPM Tech", layout="centered")

# 2. تطبيق الـ Dark Mode (CSS)
st.markdown("""
    <style>
    .stApp {background-color: #121212; color: #FFFFFF;}
    [data-testid="stSidebar"] {background-color: #1a1a1a;}
    h1 {color: #FFD700 !important; text-align: center;}
    .stButton>button {background-color: #FFD700; color: #000000; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# 3. عرض اللوجو
try:
    logo = Image.open("logo.jpg")
    st.image(logo, use_column_width=True)
except:
    st.title("★ KHORSHED SPM TECH ★")

st.markdown("---")

# 4. إدخال البيانات
col1, col2 = st.columns(2)
with col1:
    D = st.number_input("OD (mm)", value=2600.0)
    t = st.number_input("Thickness (mm)", value=14.0)
    L = st.number_input("Length (m)", value=12.0)
with col2:
    Ws = st.number_input("Width (mm)", value=2000.0)
    V = st.number_input("Speed (m/min)", value=1.3)

# 5. زر الحساب والمعادلات
if st.button("CALCULATE"):
    try:
        # المعادلات
        mod_D = D + (t * 2)
        circ = math.pi * mod_D
        alpha = math.degrees(math.acos(Ws / circ))
        weight = ((D - t) * t * 0.02466 * L) / 1000

        # النتائج
        st.success(f"### 📐 Angle: {alpha:.2f}°")
        st.info(f"### ⚖️ Weight: {weight:.3f} Tons")
        st.warning(f"### 📏 Strip/m: {1 / (Ws / circ):.3f} m")
    except:
        st.error("خطأ في البيانات! تأكد من الأرقام.")