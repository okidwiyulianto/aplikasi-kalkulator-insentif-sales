import streamlit as st

def setup_page_config():
    """Configure the Streamlit page settings."""
    st.set_page_config(
        page_title="KISS - Versi 1.0.0",
        page_icon="💋",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

def show_header():
    """Display application header and disclaimer."""
    st.header("🧮 Kalkulator Insentif Sales Sederhana 🧮")
    st.subheader("Aplikasi web sederhana untuk menghitung insentif sales berdasarkan data portofolionya")
    
    st.markdown("---")
    st.markdown("""
    <div style="
        background-color: rgb(255, 183, 0);
        color: black;
        padding: 15px;
        border-radius: 5px;
        font-size: 1em;
    ">
    <strong>🚨DISCLAIMER:</strong> Aplikasi ini masih dalam <b><u>pengembangan</b></u>. 
    Hasil perhitungan bersifat <b><u>estimasi dan tidak dijamin akurat</b></u>. 
    Pengembang <b><u>tidak bertanggung jawab</b></u> atas kerugian akibat penggunaan data ini. 
    Gunakan hanya sebagai <b><u>referensi pendukung</b></u>, bukan pengganti analisis profesional.
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

def initialize_session_state():
    """Initialize session state variables if they don't exist."""
    # Sales data
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False
        
    if 'form_reset' not in st.session_state:
        st.session_state.form_reset = False

def reset_form_state():
    """Set the reset flag to trigger form reset."""
    st.session_state.form_reset = True
    st.session_state.form_submitted = False

def show_sales_data_input():
    """Display input fields for sales data."""
    st.subheader("Data Sales")
    
    # Default values based on reset state
    nip_value = "" if st.session_state.form_reset else st.session_state.get("nip", "")
    nama_value = "" if st.session_state.form_reset else st.session_state.get("nama", "")
    grading_index = None if st.session_state.form_reset else st.session_state.get("grading_index", None)
    
    nip = st.text_input("NIP", value=nip_value, placeholder="Masukkan NIP sales", key="nip")
    nama = st.text_input("Nama", value=nama_value, placeholder="Masukkan nama lengkap sales", key="nama")
    grading = st.selectbox(
        "Grading",
        ("Trainee", "Junior", "Senior", "Executive"),
        index=grading_index,
        placeholder="Pilih grading bulan lalu",
        key="grading"
    )
    
    if grading is not None:
        grading_options = ("Trainee", "Junior", "Senior", "Executive")
        st.session_state.grading_index = grading_options.index(grading)
    
    return nip, nama, grading

def show_baki_debet_input():
    """Display input fields for baki debet data."""
    st.subheader("Baki Debet")
    
    default_value = 0 if st.session_state.form_reset else None
    
    bade_blend_sebelumnya = st.number_input(
        "Bade Blend Bulan Sebelumnya",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("bade_blend_sebelumnya", 0),
        placeholder="Masukkan baki debet blend bulan sebelumnya",
        key="bade_blend_sebelumnya"
    )
    
    bade_kur = st.number_input(
        "Bade KUR",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("bade_kur", 0),
        placeholder="Masukkan baki debet KUR",
        key="bade_kur"
    )
    
    bade_kum = st.number_input(
        "Bade KUM",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("bade_kum", 0),
        placeholder="Masukkan baki debet KUM",
        key="bade_kum"
    )
    
    return bade_blend_sebelumnya, bade_kur, bade_kum

def show_debitur_trx_input():
    """Display input fields for debitur transaksi data."""
    st.subheader("Jumlah Debitur Transaksi")
    
    default_value = 0 if st.session_state.form_reset else None
    
    debitur_trx = st.number_input(
        "Debitur Transaksi Perdagangan / Usak Genuine LVM",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("debitur_trx", 0),
        placeholder="Masukkan jumlah debitur yang transaksi perdagangan / Usak genuine LVM",
        key="debitur_trx"
    )
    
    debitur_perdagangan = st.number_input(
        "Total Debitur Perdagangan",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("debitur_perdagangan", 0),
        placeholder="Masukkan total debitur perdagangan",
        key="debitur_perdagangan"
    )
    
    return debitur_trx, debitur_perdagangan

def show_kol_lancar_input():
    """Display input fields for KOL lancar data."""
    st.subheader("Bade Kol Lancar")
    
    default_value = 0 if st.session_state.form_reset else None
    
    bade_kol1 = st.number_input(
        "Bade Kol 1",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("bade_kol1", 0),
        placeholder="Masukkan total bade kol 1",
        key="bade_kol1"
    )
    
    bade_kol1_bulan_sebelumnya = st.number_input(
        "Bade Kol 1 Bulan Sebelumnya",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("bade_kol1_bulan_sebelumnya", 0),
        placeholder="Masukkan total bade kol 1 bulan sebelumnya",
        key="bade_kol1_bulan_sebelumnya"
    )
    
    return bade_kol1, bade_kol1_bulan_sebelumnya

def show_nett_booking_input():
    """Display input fields for nett booking data."""
    st.subheader("Nett Booking")
    
    default_value = 0 if st.session_state.form_reset else None
    
    nett_booking_kur = st.number_input(
        "Nett Booking KUR",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("nett_booking_kur", 0),
        placeholder="Masukkan total nett booking KUR",
        key="nett_booking_kur"
    )
    
    nett_booking_kum = st.number_input(
        "Nett Booking KUM",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("nett_booking_kum", 0),
        placeholder="Masukkan total nett booking KUM",
        key="nett_booking_kum"
    )
    
    return nett_booking_kur, nett_booking_kum

def show_leads_input():
    """Display input fields for leads data."""
    st.subheader("Leads")
    
    default_value = 0 if st.session_state.form_reset else None
    
    nett_booking_leads_kur = st.number_input(
        "Nett Booking Leads KUR",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("nett_booking_leads_kur", 0),
        placeholder="Masukkan total nett booking leads KUR",
        key="nett_booking_leads_kur"
    )
    
    nett_booking_leads_kum = st.number_input(
        "Nett Booking Leads KUM",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("nett_booking_leads_kum", 0),
        placeholder="Masukkan total nett booking leads KUM",
        key="nett_booking_leads_kum"
    )
    
    return nett_booking_leads_kur, nett_booking_leads_kum

def show_kecukupan_agf_input():
    """Display input fields for kecukupan AGF data."""
    st.subheader("Kecukupan AGF")
    
    default_value = 0 if st.session_state.form_reset else None
    
    agf_cukup_kol1 = st.number_input(
        "Debitur AGF Cukup Kol 1",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("agf_cukup_kol1", 0),
        placeholder="Masukkan total debitur AGF cukup kol 1",
        key="agf_cukup_kol1"
    )
    
    debitur_kol1 = st.number_input(
        "Total Debitur Kol 1",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("debitur_kol1", 0),
        placeholder="Masukkan total debitur kol 1",
        key="debitur_kol1"
    )
    
    return agf_cukup_kol1, debitur_kol1

def show_lvm_usak_input():
    """Display input fields for LVM USAK data."""
    st.subheader("LVM USAK Genuine & Agen")
    
    default_value = 0 if st.session_state.form_reset else None
    
    usak_bulan_ini = st.number_input(
        "USAK Genuine Bulan Ini",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("usak_bulan_ini", 0),
        placeholder="Masukkan total usak genuine bulan ini",
        key="usak_bulan_ini"
    )
    
    usak_bulan_sebelumnya = st.number_input(
        "USAK Genuine Bulan Sebelumnya",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("usak_bulan_sebelumnya", 0),
        placeholder="Masukkan total usak genuine bulan sebelumnya",
        key="usak_bulan_sebelumnya"
    )
    
    agen_ac = st.number_input(
        "Jumlah Agen AC",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("agen_ac", 0),
        placeholder="Masukkan total agen AC",
        key="agen_ac"
    )
    
    agen_kelolaan = st.number_input(
        "Jumlah Agen Kelolaan",
        step=1,
        value=default_value if default_value is not None else st.session_state.get("agen_kelolaan", 0),
        placeholder="Masukkan total agen kelolaan",
        key="agen_kelolaan"
    )
    
    return usak_bulan_ini, usak_bulan_sebelumnya, agen_ac, agen_kelolaan

def show_action_buttons():
    """Display calculate and reset buttons."""
    col1, col2 = st.columns(2)
    
    with col1:
        calculate_button = st.button("💰 Hitung Insentif", type="primary", use_container_width=True)
    
    with col2:
        reset_button = st.button("🔄 Reset Form", type="secondary", use_container_width=True, on_click=reset_form_state)
        
    return calculate_button, reset_button

def show_footer():
    """Display application footer."""
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
            <p><b>© 2025 OKI DWI YULIANTO | Made with ❤️ at Cluster Cilacap</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def calculate_incentive():
    """Calculate the incentive based on input data."""
    # Set form submitted flag
    st.session_state.form_submitted = True
    
    st.success("Perhitungan insentif berhasil!")
    
    # Example display (replace with actual calculation)
    st.write("### Hasil Perhitungan Insentif")
    st.write(f"NIP: {st.session_state.get('nip', '')}")
    st.write(f"Nama: {st.session_state.get('nama', '')}")
    st.write(f"Grading: {st.session_state.get('grading', '')}")
    
    # Add your actual calculation logic here
    st.info("Detail perhitungan akan ditampilkan di sini sesuai dengan formula insentif yang berlaku.")

def main():
    """Main application function."""
    setup_page_config()
    initialize_session_state()
    show_header()
    
    # Display all input sections
    show_sales_data_input()
    show_baki_debet_input()
    show_debitur_trx_input()
    show_kol_lancar_input()
    show_nett_booking_input()
    show_leads_input()
    show_kecukupan_agf_input()
    show_lvm_usak_input()
    
    st.divider()
    
    # Add action buttons
    calculate_button, reset_button = show_action_buttons()
    
    # Handle calculate button click
    if calculate_button:
        calculate_incentive()
    
    # Reset the form_reset flag after the form has been rendered
    if st.session_state.form_reset:
        st.session_state.form_reset = False
        st.rerun()
    
    show_footer()

if __name__ == "__main__":
    main()