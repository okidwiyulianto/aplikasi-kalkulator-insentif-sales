import streamlit as st

# Header & Judul Aplikasi
st.set_page_config(
    page_title="KIS - Versi 1.0.0",
    page_icon="💋",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.header("Kalkulator Insentif Sales (KIS) 💋")
st.subheader("Aplikasi sederhana untuk menghitung insentif sales berdasarkan data portofolionya")

st.divider()

# Input Data
st.subheader("Data Sales")

nip = st.text_input("NIP", placeholder="Masukkan NIP sales")
nama = st.text_input("Nama", placeholder="Masukkan nama lengkap sales")
grading = st.selectbox(
    "Grading",
    ("Trainee", "Junior", "Senior", "Executive"),
    index=None,
    placeholder="Pilih grading bulan lalu",
)

st.write("Grading yang kamu picklist adalah ", grading)

st.subheader("Baki Debet")

bade_blend_sebelumnya = st.number_input(
    "Bade Blend Bulan Sebelumnya",
    step=1,
    value=0,
    placeholder="Masukkan baki debet blend bulan sebelumnya",
    )
st.write("Bade blend bulan sebelumnya yang kamu input adalah ", int(bade_blend_sebelumnya))

bade_kur = st.number_input(
    "Bade KUR",
    step=1,
    value=0,
    placeholder="Masukkan baki debet KUR",
    )
st.write("Bade KUR yang kamu input adalah ", int(bade_kur))

bade_kum = st.number_input(
    "Bade KUM",
    step=1,
    value=0,
    placeholder="Masukkan baki debet KUM",
    )
st.write("Bade KUM yang kamu input adalah ", int(bade_kum))

st.subheader("Jumlah Debitur Transaksi")

debitur_trx = st.number_input(
    "Debitur Transaksi Perdagangan / Usak Genuine LVM",
    step=1,
    value=0,
    placeholder="Masukkan jumlah debitur yang transaksi perdagangan / Usak genuine LVM",
    )
st.write("Total debitur transaksi yang kamu input adalah ", int(debitur_trx))

debitur_perdagangan = st.number_input(
    "Total Debitur Perdagangan",
    step=1,
    value=0,
    placeholder="Masukkan total debitur perdagangan",
    )
st.write("Total debitur perdagangan yang kamu input adalah ", int(debitur_perdagangan))

st.divider()

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #000;
        text-align: center;
        padding: 10px;
        font-size: 0.9em;
    }
    </style>
    <div class="footer">
        <p><b>© 2025 OKI DWI YULIANTO | Made with ❤️</b></p>
    </div>
    """,
    unsafe_allow_html=True
)