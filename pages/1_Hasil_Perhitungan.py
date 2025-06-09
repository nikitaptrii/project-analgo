import streamlit as st
from karatsuba import karatsuba

st.set_page_config(page_title="Hasil Karatsuba", layout="wide")

# Ambil nilai dari session_state
A = st.session_state.get("A", "")
B = st.session_state.get("B", "")
base = st.session_state.get("base", 10)

if not A or not B:
    st.warning("Kembali ke halaman utama untuk memasukkan bilangan.")
    st.page_link("Masukan_Angka.py", label="⬅️ Kembali ke Halaman Utama")
    st.stop()

st.markdown("<h1 style='text-align: center;'>📄 Hasil Perhitungan</h1>", unsafe_allow_html=True)
st.divider()

steps = []
result = karatsuba(A, B, base, steps)

st.success("✅ Perkalian berhasil dihitung!")
st.code(f"{A} × {B} = {result}", language="python")

if base == 2:
    st.info(f"💡 Dalam desimal: {int(A, 2)} × {int(B, 2)} = {int(result, 2)}")

st.markdown("---")
with st.expander("📋 Langkah-langkah Karatsuba (Penjabaran Detail)"):
    for step in steps:
        st.markdown(f"- {step}")

st.page_link("Masukan_Angka.py", label="🔄 Hitung ulang", icon="🔁")
