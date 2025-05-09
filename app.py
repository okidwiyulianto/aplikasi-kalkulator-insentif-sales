import streamlit as st

# Judul Aplikasi
st.set_page_config(
    page_title="KIS - Versi 1.0.0",
    page_icon="💋",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Kalkulator Insentif Sales (KIS)")
st.subheader("Kalkulator untuk menghitung insentif sales berdasarkan data portofolio")
st.markdown(
    """
    Aplikasi ini dibuat untuk membantu pengguna dalam menghitung insentif SGP berdasarkan data portofolio yang dimiliki.\n
    Dengan menggunakan aplikasi ini, pengguna dapat dengan mudah mendapatkan informasi tentang insentif yang berhak diterima.\n
    Aplikasi ini juga dilengkapi dengan fitur untuk mengunduh hasil perhitungan dalam format PDF, sehingga memudahkan pengguna dalam menyimpan dan membagikan informasi tersebut.\n
    Aplikasi ini masih dalam tahap pengembangan dan akan terus diperbarui untuk meningkatkan fungsionalitas dan pengalaman pengguna.\n
    """
)

# Gambar Profile
st.image("okidwiyulianto.png", caption="Made with 💖 by Oki Dwi Yulianto", width=250)