import time
import streamlit as st
import phonenumbers
from phonenumbers import geocoder,carrier


st.header("📞Find Your Number")

num : str = st.text_input("Inter Your Number (+)")


if st.button("Find"):   # jab user click karry ga to ye chaly ga
    
    if num:    # agar num ky andar value hoye gi to ye chaly ga
       
        with st.spinner("⏳ Please wait..."):    # with 4 sec wait karry ga us ky baat hahat jaye ga
            time.sleep(4)    # Simulate waiting

        try:
            phone_num = phonenumbers.parse(num) 
            find_num = geocoder.description_for_number(phone_num, "en")

            service_pro = phonenumbers.parse(num)
            sav ="Service Provider:", carrier.name_for_number(service_pro, "en")

            if find_num:   # agar find_num ky andar sahe number hoye ga to ye cahly ga wana nhi
                st.markdown(f"<p>✔️ Successfully ! Find Your Number : <span style='color: red; font-size:20px; text-decoration: underline;'>{find_num}</span></p>", unsafe_allow_html=True) 
                st.success(f"{sav}") # is ky andar sim
            else :   # find_num ky andar sahe number nhi hoye ga to te cahly ga
               st.markdown("<p style='color: red; font-size: 18px;'> ❌ Invalid number!</p>", unsafe_allow_html=True)
               
        except phonenumbers.NumberParseException:    # agar user ny num ky andar text dia to ye cahly ga
            st.error("❌ Invalid phone number format! Please enter a valid number.")

    else :    # agar user ny num ky andar kuch bhi nhi dia to ye cahly ga
        st.warning("⚠️ Please enter a phone number before clicking Find.")


