import streamlit as st
import math
from PIL import Image

# 1. إعدادات الصفحة
st.set_page_config(page_title="Khorshed SPM Tech", layout="centered")

# 2. تنسيق الـ Dark Mode
st.markdown("""
    <style>
    .stApp {background-color: #121212; color: #FFFFFF;}
    </style>
    """, unsafe_allow_html=True)

# 3. عرض اللوجو بحجم محكوم
try:
    logo = Image.open("logo.jpg")
    # تصغير العرض لـ 200 بكسل عشان يظهر فوق والزراير تكون واضحة
    st.image(logo, width=200) 
except:
    st.title("★ KHORSHED SPM TECH ★")

st.markdown("---") # خط فاصل

# 4. إدخال البيانات في أعمدة منظمة
col1, col2 = st.columns(2)
with col1:
    D = st.number_input("OD (mm)", value=2600.0)
    t = st.number_input("Thickness (mm)", value=14.0)
with col2:
    Ws = st.number_input("Width (mm)", value=2000.0)
    L = st.number_input("Length (m)", value=12.0)

# 5. إضافة مساحة بين الإدخال والزر
st.write("") 

# 6. الزر والمعادلات
if st.button("CALCULATE"):
    try:
        mod_D = D + (t * 2)
        circ = math.pi * mod_D
        alpha = math.degrees(math.acos(Ws / circ))
        weight = ((D - t) * t * 0.02466 * L) / 1000
        
        st.success(f"### 📐 Angle: {alpha:.2f}°")
        st.info(f"### ⚖️ Weight: {weight:.3f} Tons")
    except:
        st.error("خطأ في البيانات!")
