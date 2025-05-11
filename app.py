import streamlit as st

# Header & Judul Aplikasi
st.set_page_config(
    page_title="KISS - Versi 1.0.0",
    page_icon="💋",
    layout="centered",
    initial_sidebar_state="collapsed",
)
st.header("Kalkulator Insentif Sales Sederhana")
st.subheader("Aplikasi web sederhana untuk menghitung insentif sales berdasarkan data portofolionya")

# Disclaimer
st.markdown("---")
st.markdown("""
<div style="
    background-color: rgb(255, 183, 0);
    color: black;
    padding: 15px;
    border-radius: 5px;
    font-size: 1em;
">
<strong>🚨DISCLAIMER:</strong> Aplikasi ini masih dalam <b><u>pengembangan</b></u>. Hasil perhitungan bersifat <b><u>estimasi dan tidak dijamin akurat</b></u>. Pengembang <b><u>tidak bertanggung jawab</b></u> atas kerugian akibat penggunaan data ini. Gunakan hanya sebagai <b><u>referensi pendukung</b></u>, bukan pengganti analisis profesional.
</div>
""", unsafe_allow_html=True)

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

st.subheader("Baki Debet")

bade_blend_sebelumnya = st.number_input(
    "Bade Blend Bulan Sebelumnya",
    step=1,
    value=0,
    placeholder="Masukkan baki debet blend bulan sebelumnya",
)

bade_kur = st.number_input(
    "Bade KUR",
    step=1,
    value=0,
    placeholder="Masukkan baki debet KUR",
)

bade_kum = st.number_input(
    "Bade KUM",
    step=1,
    value=0,
    placeholder="Masukkan baki debet KUM",
)

st.subheader("Jumlah Debitur Transaksi")

debitur_trx = st.number_input(
    "Debitur Transaksi Perdagangan / Usak Genuine LVM",
    step=1,
    value=0,
    placeholder="Masukkan jumlah debitur yang transaksi perdagangan / Usak genuine LVM",
)

debitur_perdagangan = st.number_input(
    "Total Debitur Perdagangan",
    step=1,
    value=0,
    placeholder="Masukkan total debitur perdagangan",
)

st.subheader("% Stay Kol Lancar")

bade_kol1 = st.number_input(
    "Bade Kol 1",
    step=1,
    value=0,
    placeholder="Masukkan total bade kol 1",
)

bade_kol1_bulan_sebelumnya = st.number_input(
    "Bade Kol 1 Bulan Sebelumnya",
    step=1,
    value=0,
    placeholder="Masukkan total bade kol 1 bulan sebelumnya",
)

st.subheader("Nett Booking")

nett_booking_kur = st.number_input(
    "Nett Booking KUR",
    step=1,
    value=0,
    placeholder="Masukkan total nett booking KUR",
)

nett_booking_kum = st.number_input(
    "Nett Booking KUM",
    step=1,
    value=0,
    placeholder="Masukkan total nett booking KUM",
)

st.subheader("Leads")

nett_booking_leads_kur = st.number_input(
    "Nett Booking Leads KUR",
    step=1,
    value=0,
    placeholder="Masukkan total nett booking leads KUR",
)

nett_booking_leads_kum = st.number_input(
    "Nett Booking Leads KUM",
    step=1,
    value=0,
    placeholder="Masukkan total nett booking leads KUM",
)

st.subheader("Kecukupan AGF")

agf_cukup_kol1 = st.number_input(
    "Debitur AGF Cukup Kol 1",
    step=1,
    value=0,
    placeholder="Masukkan total debitur AGF cukup kol 1",
)

debitur_kol1 = st.number_input(
    "Total Debitur Kol 1",
    step=1,
    value=0,
    placeholder="Masukkan total debitur kol 1",
)

st.subheader("LVM USAK Genuine & Agen")

usak_bulan_ini = st.number_input(
    "USAK Genuine Bulan Ini",
    step=1,
    value=0,
    placeholder="Masukkan total usak genuine bulan ini",
)

usak_bulan_sebelumnya = st.number_input(
    "USAK Genuine Bulan Sebelumnya",
    step=1,
    value=0,
    placeholder="Masukkan total usak genuine bulan sebelumnya",
)

agen_ac = st.number_input(
    "Jumlah Agen AC",
    step=1,
    value=0,
    placeholder="Masukkan total agen AC",
)

agen_kelolaan = st.number_input(
    "Jumlah Agen Kelolaan",
    step=1,
    value=0,
    placeholder="Masukkan total agen kelolaan",
)

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
        background-color: rgb(0, 61, 121);
        color: #fff;
        text-align: center;
        padding: 10px;
        font-size: 1em;
    }
    </style>
    <div class="footer">
        <p><b>© 2025 OKI DWI YULIANTO | Made with ❤️ di Cluster Cilacap</b></p>
    </div>
    """,
    unsafe_allow_html=True
)