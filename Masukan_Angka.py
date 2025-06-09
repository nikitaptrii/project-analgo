import streamlit as st
from karatsuba import karatsuba

st.set_page_config(page_title="Karatsuba Multiplier", layout="wide")

# Header
st.markdown("<h1 style='text-align: center;'>Karatsuba Multiplier 🧮</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Perkalian bilangan besar dengan algoritma Karatsuba (Fast Multiplication)</p>", unsafe_allow_html=True)
st.divider()

# Buat kolom dummy kiri-kanan aar isi konten rata tengah
left_spacer, center_col, right_spacer = st.columns([1, 2, 1])

with center_col:
    st.subheader("🔢 Masukkan Angka")

    tipe = st.radio("Pilih tipe bilangan:", ["Decimal", "Binary"], horizontal=True)
    base = 2 if tipe.lower() == "binary" else 10

    A = st.text_input(f"Bilangan pertama ({tipe})", placeholder="Contoh: 1234")
    B = st.text_input(f"Bilangan kedua ({tipe})", placeholder="Contoh: 5678")

    tombol = st.button("🚀 Hitung Sekarang")

    if tombol:
        st.session_state["A"] = A.strip()
        st.session_state["B"] = B.strip()
        st.session_state["base"] = base
        st.switch_page("pages/1_Hasil_Perhitungan.py")
