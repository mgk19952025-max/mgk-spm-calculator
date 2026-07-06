import streamlit as st
import math
from PIL import Image

# إعدادات الصفحة
st.set_page_config(page_title="Khorshed SPM Tech", layout="centered")

# تنسيق الـ Dark Mode وتنسيق الأزرار الذهبية
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
    }
    div.stButton > button:hover {
        background-color: #DAA520;
    }
    </style>
    """, unsafe_allow_html=True)

# عرض اللوجو بنفس عرض الأزرار
try:
    logo = Image.open("logo.jpg")
    # عرض اللوجو بحيث يأخذ مساحة كافية ومتناسقة
    st.image(logo, use_column_width=True)
except:
    st.title("KHORSHED SPM TECH")

st.markdown("---")

# المدخلات
col1, col2 = st.columns(2)
with col1:
    D = st.number_input("OD (mm)", value=2600.0)
    t = st.number_input("Thickness (mm)", value=14.0)
with col2:
    Ws = st.number_input("Width (mm)", value=2000.0)
    L = st.number_input("Length (m)", value=12.0)

st.write("") # مسافة إضافية

# الحسابات
if st.button("CALCULATE"):
    try:
        mod_D = D + (t * 2)
        circ = math.pi * mod_D
        alpha = math.degrees(math.acos(Ws / circ))
        weight = ((D - t) * t * 0.02466 * L) / 1000
        strip_per_m = 1 / (Ws / circ)
        
        # عرض النتائج
        st.subheader("Results:")
        res_cols = st.columns(2)
        res_cols[0].metric("Angle", f"{alpha:.2f}°")
        res_cols[1].metric("Weight", f"{weight:.3f} T")
        
        st.info(f"**Modified Circumference:** {circ:.2f} mm")
        st.info(f"**Strip per meter:** {strip_per_m:.4f} m")
        st.warning(f"**Weld Dimensions:** {t+4:.1f} mm (Width) / {t*0.8:.1f} mm (Height)")
        
    except Exception as e:
        st.error("تأكد من إدخال قيم صحيحة!")
