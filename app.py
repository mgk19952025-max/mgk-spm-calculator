import streamlit as st
import math
from PIL import Image

# ... (نفس الثوابت وإعداد الصفحة) ...

if st.button("CALCULATE"):
    try:
        factor = GRADES[c1]
        d_tol, end_tol, end_c_tol = STDS[c2]
        
        mod_D = D + (t * 2)
        circ = math.pi * mod_D
        cos_a = Ws / circ
        alpha = math.degrees(math.acos(cos_a))
        weight = ((D - t) * t * factor * L) / 1000
        
        # المعادلات المحدثة
        strip_per_meter = 1 / cos_a
        total_strip = strip_per_meter * L
        cut_time = total_strip / V # المعادلة اللي أنت طلبتها
        
        weld_width = t + 4
        cap_height = t * 0.8
        
        # النتائج
        res = f"""
        **Angle:** {alpha:.2f} Degrees  
        **Weight:** {weight:.3f} Tons  
        **Strip/m:** {strip_per_meter:.3f} m  
        **Total Strip:** {total_strip:.2f} m  
        **Weld Width:** {weld_width:.1f} mm  
        **Cap Height:** {cap_height:.1f} mm  
        **Cutting Time:** {cut_time:.2f} min  
        """
        st.markdown("### Results")
        st.info(res)
        # ... (باقي النتائج)
    except:
        st.error("Check Inputs!")
