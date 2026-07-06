import streamlit as st
import math
from PIL import Image

# 1. إعدادات الصفحة
st.set_page_config(page_title="Khorshed SPM Tech", layout="centered")

# 2. تنسيق الـ Dark Mode والألوان الذهبية
st.markdown("""
    <style>
    .stApp {background-color: #121212; color: #FFFFFF;}
    h1 {color: #FFD700 !important; text-align: center;}
    /* زر الحساب ذهبي */
    div.stButton > button:first-child {
        width: 100%;
        background-color: #FFD700;
        color: #000000;
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    div.stButton > button:hover {
        background-color: #DAA520;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض اللوجو
try:
    logo = Image.open("logo.jpg")
    st.image(logo, use_column_width=True)
except:
    st.title("KHORSHED SPM TECH")

st.markdown("---")

# 4. المدخلات
col1, col2 = st.columns(2)
with col1:
    D = st.number_input("Required Diameter (mm)", value=2600.0)
    t = st.number_input("Thickness (mm)", value=14.0)
with col2:
    Ws = st.number_input("Strip Width (mm)", value=2000.0)
    L = st.number_input("Pipe Length (m)", value=12.0)
    V = st.number_input("Speed (m/min)", value=1.3)

st.write("")

# 5. الحسابات والمعادلات المحدثة
if st.button("CALCULATE"):
    try:
        # المعادلة المصححة للمحيط المعدل (القطر + 2*السمك * pi)
        mod_circ = (D + (2 * t)) * math.pi
        
        # الزاوية
        alpha = math.degrees(math.acos(Ws / mod_circ))
        
        # الوزن (0.02466 هو المعامل المعتاد)
        weight = ((D - t) * t * 0.02466 * L) / 1000
        
        # الشريط لكل متر (1 مقسوم على (عرض الشريط / المحيط))
        strip_per_m = 1 / (Ws / mod_circ)
        
        # عرض النتائج
        st.subheader("Results:")
        
        res_cols1, res_cols2 = st.columns(2)
        res_cols1.metric("Angle", f"{alpha:.2f}°")
        res_cols2.metric("Weight", f"{weight:.3f} T")
        
        st.info(f"**Modified Circumference:** {mod_circ:.2f} mm")
        st.info(f"**Strip per meter:** {strip_per_m:.4f} m")
        st.warning(f"**Weld Dimensions:** {t+4:.1f} mm (Width) / {t*0.8:.1f} mm (Height)")
        
    except Exception as e:
        st.error("Error: Check your input values (Ensure Width < Circumference).")
