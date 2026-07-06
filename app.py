import streamlit as st
import math
from PIL import Image

# --- الثوابت ---
GRADES = {"S235JR": 0.02466, "API X42/52": 0.02467, "API X60/70": 0.02468}
STDS = {"API 5L": (13.0, 1.6, 5.0), "EN 10219": (10.0, 2.0, 6.0), "DIN 2458": (10.0, 2.0, 6.0)}

# --- إعداد الصفحة ---
st.set_page_config(page_title="Khorshed SPM Tech", layout="centered")

# --- تنسيق Dark Mode ---
st.markdown("""
    <style>
    .stApp {background-color: #2e2e2e; color: #FFFFFF;}
    .stButton>button {width: 100%; background-color: #007acc; color: white; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# --- عرض اللوجو مكان العنوان الزخرفي ---
try:
    logo = Image.open("logo.jpg") # تأكد أن اسم ملف الصورة في GitHub هو logo.jpg
    st.image(logo, use_column_width=True)
except:
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>★ KHORSHED SPM TECH ★</h1>", unsafe_allow_html=True)

# --- المدخلات ---
col1, col2 = st.columns(2)
with col1:
    D = st.number_input("OD (mm)", value=2600.0)
    t = st.number_input("Thickness", value=14.0)
    L = st.number_input("Length (m)", value=12.0)
with col2:
    Ws = st.number_input("Width (mm)", value=2000.0)
    V = st.number_input("Speed (m/min)", value=1.3)

c1 = st.selectbox("Grade", list(GRADES.keys()))
c2 = st.selectbox("Standard", list(STDS.keys()))

# --- منطق الحساب ---
if st.button("CALCULATE"):
    try:
        factor = GRADES[c1]
        d_tol, end_tol, end_c_tol = STDS[c2]
        
        mod_D = D + (t * 2)
        circ = math.pi * mod_D
        cos_a = Ws / circ
        alpha = math.degrees(math.acos(cos_a))
        weight = ((D - t) * t * factor * L) / 1000
        
        strip_len = (1 / cos_a) * L
        strip_per_meter = 1 / cos_a
        weld_width = t + 4
        cap_height = t * 0.8
        
        # عرض النتائج بنفس ترتيبك
        res = f"""
        **Angle:** {alpha:.2f} Degrees  
        **Weight:** {weight:.3f} Tons  
        **Strip/m:** {strip_per_meter:.3f} m  
        **Total Strip:** {strip_len:.2f} m  
        **Weld Width:** {weld_width:.1f} mm  
        **Cap Height:** {cap_height:.1f} mm  
        
        --- **QUALITY LIMITS** ---  
        **Body OD:** {D-d_tol:.1f} to {D+d_tol:.1f}  
        **End OD:** {D-end_tol:.1f} to {D+end_tol:.1f}  
        **End Circ:** {circ-end_c_tol:.1f} to {circ+end_c_tol:.1f}
        """
        st.info(res)
    except:
        st.error("Check Inputs!")
