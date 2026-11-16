import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
Discount_% = st.number_input("กรอกส่วนสินค้า (%):", max_value=100.0 , value=0.0)
Discount_price = price*(Discount_%/100)
vat = Discount_price * 0.07
net_price = Discount_price - vat
st.header(f"• ส่วนลดลดได้: {Discount_price:.2f} บาท")
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")

st.write("นายธีรภัทร มุลิลา 42 ม.4/5")
