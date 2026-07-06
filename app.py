import streamlit as st
import math
from PIL import Image

# إعدادات الصفحة
st.set_page_config(page_title="MGK SPM Calculator", layout="centered")

# التنسيق المظلم (Dark Mode) مع زر ذهبي
st.markdown("""
    <style>
    .stApp {background-color: #121212; color: #FFFFFF;}
    h1 {color: #FFD700 !important; text-align: center;}
    div.stButton > button {width: 100%; background-color: #FFD700; color: #000000; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# عرض اللوجو
try:
    logo = Image.open("logo.jpg")
    st.image(logo, use_column_width=True)
except:
    st.title("MGK SPM CALCULATOR")

# المدخلات (مقسمة لصفين عشان الموبايل)
col1, col2 = st.columns(2)
with col1:
    D = st.number_input("OD (mm)", value=2600.0)
    t = st.number_input("Thickness (mm)", value=14.0)
with col2:
    Ws = st.number_input("Width (mm)", value=2000.0)
    L = st.number_input("Length (m)", value=12.0)

# زر الحساب
if st.button("CALCULATE"):
    try:
        # المعادلات
        mod_circ = (D + (2 * t)) * math.pi
        alpha = math.degrees(math.acos(Ws / mod_circ))
        weight = ((D - t) * t * 0.02466 * L) / 1000
        strip_per_m = 1 / (Ws / mod_circ)
        
        # عرض النتائج في أعمدة
        st.subheader("Results:")
        r1, r2 = st.columns(2)
        r1.metric("Angle", f"{alpha:.2f}°")
        r2.metric("Weight", f"{weight:.3f} T")
        
        # معلومات إضافية (بشكل أوضح)
        st.write("---")
        st.markdown(f"**Modified Circumference:** `{mod_circ:.2f} mm`")
        st.markdown(f"**Strip per meter:** `{strip_per_m:.4f} m`")
        st.markdown(f"**Weld Dimensions:** `{t+4:.1f} mm (Width) / {t*0.8:.1f} mm (Height)`")
        
    except Exception:
        st.error("خطأ في الحساب! تأكد من أن Width أصغر من Circumference.")
