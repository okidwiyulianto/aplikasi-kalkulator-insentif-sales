import streamlit as st
import locale # Impor modul locale

def format_rupiah(value):
    """Formats a number into Indonesian Rupiah currency format (RpX.XXX.XXX,XX)."""
    try:
        # Coba atur locale ke Indonesian, abaikan jika gagal (misal, locale tidak terinstall)
        try:
            locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
        except locale.Error:
            # Jika locale id_ID tidak tersedia, gunakan cara manual fallback
            # Format dengan pemisah standar (koma ribuan, titik desimal)
            formatted_string = f"{float(value):,.2f}" # Contoh: 3,000,000.00
            # Tukar pemisah secara manual
            int_part, dec_part = formatted_string.split('.')
            int_part_id = int_part.replace(',', '.') # Ganti koma ribuan -> titik ribuan
            return f"Rp{int_part_id},{dec_part}"

        # Jika locale id_ID berhasil diatur, gunakan format locale
        # '%.2f' untuk dua desimal, grouping=True untuk pemisah ribuan
        return locale.format_string("Rp%.2f", float(value), grouping=True)

    except (ValueError, TypeError):
        # Jika input bukan angka, kembalikan nilai default/error
        return "Rp0,00"
    finally:
        # Selalu kembalikan locale ke default sistem setelah selesai
        # untuk menghindari efek samping pada bagian lain aplikasi.
        # Kosongkan argumen kedua untuk kembali ke default.
        try:
            locale.setlocale(locale.LC_ALL, '')
        except locale.Error:
            pass # Abaikan jika gagal mengembalikan locale

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
    st.header("Kalkulator Insentif Sales Sederhana")
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
            padding: 5px;
            font-size: 0.9em;
        }
        </style>
        <div class="footer">
            <p><b>©️ 2025 | 👨‍💻 OKI DWI YULIANTO</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def calculate_incentive():
    """Calculate the incentive based on input data."""
    try:
        # Set form submitted flag
        st.session_state.form_submitted = True
        
        # 1. Mengambil data dari session state
        grading = st.session_state.get('grading', '')
        bade_kur = float(st.session_state.get('bade_kur', 0))
        bade_kum = float(st.session_state.get('bade_kum', 0))
        bade_blend_sebelumnya = float(st.session_state.get('bade_blend_sebelumnya', 0))
        debitur_trx = float(st.session_state.get('debitur_trx', 0))
        debitur_perdagangan = float(st.session_state.get('debitur_perdagangan', 0))
        bade_kol1 = float(st.session_state.get('bade_kol1', 0))
        bade_kol1_bulan_sebelumnya = float(st.session_state.get('bade_kol1_bulan_sebelumnya', 0))
        nett_booking_kur = float(st.session_state.get('nett_booking_kur', 0))
        nett_booking_kum = float(st.session_state.get('nett_booking_kum', 0))

        # 2. Perhitungan Komponen Dasar
        bade_blend = bade_kur + bade_kum
        
        # Target berdasarkan grading
        target_grading_map = {
            "Trainee": 1,
            "Junior": 2_000_000_000,
            "Senior": 4_000_000_000,
            "Executive": 10_000_000_000
        }
        target_grading = target_grading_map.get(grading, 0)
        
        # Rasio transaksi debitur
        trx_deb = debitur_trx / debitur_perdagangan if debitur_perdagangan != 0 else 0
        
        # Rasio KOL lancar
        kol_lancar = bade_kol1 / bade_kol1_bulan_sebelumnya if bade_kol1_bulan_sebelumnya != 0 else 0
        
        # 3. Perhitungan Kriteria Penentu
        kriteria_penentu = (
            (1 if bade_blend >= target_grading else 0) +
            (1 if trx_deb >= 0.1 or debitur_perdagangan == 0 else 0) +
            (1 if abs(kol_lancar - 0.99) < 0.0001 else 0)
        )
        
        # 4. Parameter Pengali
        parameter_pengali_map = {
            ("Executive", 3): 2.0,
            ("Senior", 3): 1.5,
            ("Junior", 3): 1.25,
            ("Trainee", 3): 1.0,
            ("Executive", 2): 1.0,
            ("Senior", 2): 1.0,
            ("Junior", 2): 0.75,
            ("Trainee", 2): 0.75
        }
        parameter_pengali = parameter_pengali_map.get((grading, kriteria_penentu), 0.5)
        
        # 5. Parameter Target Booking
        parameter_target_booking_map = {
            "Trainee": 350_000_000,
            "Junior": 500_000_000,
            "Senior": 850_000_000,
            "Executive": 1_200_000_000
        }
        parameter_target_booking = parameter_target_booking_map.get(grading, 0)
        
        # 6. Perhitungan Nett Booking
        nett_booking_blend = nett_booking_kur + nett_booking_kum
        persentase_nett_booking_blend = (
            nett_booking_blend / parameter_target_booking if parameter_target_booking != 0 else 0
        )
        
        persentase_nett_booking_kum = (
            nett_booking_kum / nett_booking_blend if nett_booking_blend != 0 else 0
        )
        
        persentase_nett_booking_kur = (
            nett_booking_kur / nett_booking_blend if nett_booking_blend != 0 else 0
        )
        
        # 7. Pengali Main Booking
        def determine_booking_multiplier():
            if persentase_nett_booking_blend >= 1.0:  # >= 100%
                if bade_blend >= bade_blend_sebelumnya:
                    return 1.0
                return 0.7
            elif persentase_nett_booking_blend >= 0.8:  # >= 80%
                if bade_blend >= bade_blend_sebelumnya:
                    return 0.7
                return 0.7
            else:  # < 80%
                return 0.3
        
        pengali_main_booking = parameter_pengali * determine_booking_multiplier()
        
        # 8. Main Insentif Booking
        main_insentif_booking = (nett_booking_blend / 10_000_000) * 10_000 * pengali_main_booking
        
        # 9. Menampilkan Hasil
        st.success("💰 Perhitungan insentif berhasil!")
        
        st.write("### 📊 Hasil Perhitungan Insentif")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Data Sales:**")
            st.write(f"NIP: {st.session_state.get('nip', '')}")
            st.write(f"Nama: {st.session_state.get('nama', '')}")
            st.write(f"Grading: {grading}")
        
        with col2:
            st.write("**Hasil Akhir:**")
            st.write(f"Main Insentif Booking: {format_rupiah(main_insentif_booking)}")
        
        with st.expander("💡 Detail Komponen Perhitungan"):
            st.write("#### 1️⃣ Komponen Dasar")
            st.write(f"- Bade Blend: {format_rupiah(bade_blend)}")
            st.write(f"- Target Grading: {format_rupiah(target_grading)}")
            st.write(f"- Rasio Transaksi Debitur: {trx_deb:.2%}")
            st.write(f"- Rasio KOL Lancar: {kol_lancar:.2%}")
            
            st.write("\n#### 2️⃣ Komponen Pengali")
            st.write(f"- Kriteria Penentu: {kriteria_penentu}")
            st.write(f"- Parameter Pengali: {parameter_pengali:.2f}")
            
            st.write("\n#### 3️⃣ Komponen Booking")
            st.write(f"- Target Booking: {format_rupiah(parameter_target_booking)}")
            st.write(f"- Nett Booking Blend: {format_rupiah(nett_booking_blend)}")
            st.write(f"- Persentase Nett Booking Blend: {persentase_nett_booking_blend:.2%}")
            st.write(f"- Persentase Nett Booking KUM: {persentase_nett_booking_kum:.2%}")
            st.write(f"- Persentase Nett Booking KUR: {persentase_nett_booking_kur:.2%}")
            st.write(f"- Pengali Main Booking: {pengali_main_booking:.2f}")
        
    except ZeroDivisionError:
        st.error("❌ Error: Terdapat pembagian dengan nol dalam perhitungan")
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan dalam perhitungan: {str(e)}")

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