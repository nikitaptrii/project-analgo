import streamlit as st
from karatsuba import karatsuba

st.set_page_config(page_title="Karatsuba Multiplier", layout="wide")

# Fungsi validasi input
def is_valid_input(value: str, base: int) -> bool:
    if base == 2:
        return value != "" and all(c in "01" for c in value)
    elif base == 10:
        return value.isdigit()
    return False


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

    A = st.text_input(f"Bilangan pertama ({tipe})", placeholder="Masukan Angka Disini")
    B = st.text_input(f"Bilangan kedua ({tipe})", placeholder="Masukan Angka Disini")

    tombol = st.button("🚀 Hitung Sekarang")

    if tombol:
        A_clean = A.strip()
        B_clean = B.strip()

        # Cek validitas A dan B
        valid_A = is_valid_input(A_clean, base)
        valid_B = is_valid_input(B_clean, base)

    # Tampilkan semua error yang ada
        
        # Handle jika kosong
        if not A_clean or not B_clean:
            st.error("Input tidak boleh kosong.")
        # Handle jika negatif
        elif A_clean.startswith('-') or B_clean.startswith('-'):
            st.error("Algoritma Karatsuba hanya mendukung bilangan non-negatif.")
        # Handle jika dua-duanya salah format
        elif not valid_A and not valid_B:
            st.error(f"Bilangan pertama **dan** kedua bukan {'biner (hanya 0 dan 1)' if base == 2 else 'desimal (hanya angka 0–9)'}!")
        # Handle jika salah satu salah
        elif not valid_A:
            st.error(f"Bilangan pertama bukan {'biner (hanya 0 dan 1)' if base == 2 else 'desimal (hanya angka 0–9)'}!")
        elif not valid_B:
            st.error(f"Bilangan kedua bukan {'biner (hanya 0 dan 1)' if base == 2 else 'desimal (hanya angka 0–9)'}!")
        # Jika semua valid
        else:
            st.session_state["A"] = A_clean
            st.session_state["B"] = B_clean
            st.session_state["base"] = base
            st.switch_page("pages/1_Hasil_Perhitungan.py")


