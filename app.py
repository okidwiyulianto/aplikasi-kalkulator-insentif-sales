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
        page_title="KISS - Versi 1.0.1",
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
    <strong>🚨DISCLAIMER🚨:</strong><br> Rumus dan komponen perhitungan mengikuti <b><u>KALKULATOR INSENTIF VERSION 1.0.1</b></u>.<br> Pengembang <b><u>tidak bertanggung jawab</b></u> atas kerugian akibat penggunaan data ini.<br> Gunakan hanya sebagai <b><u>alat untuk mempermudah dan referensi pendukung.</b></u>
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
            <p><b>🔄️ Last updated: 14 Mei 2025</b></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def calculate_incentive():
    """Calculate the incentive based on input data."""
    try:
        # Set form submitted flag
        st.session_state.form_submitted = True
        
        # 1. Get data from session state
        # Basic sales data
        grading = st.session_state.get('grading', '')
        
        # Bade data
        bade_kur = float(st.session_state.get('bade_kur', 0))
        bade_kum = float(st.session_state.get('bade_kum', 0)) 
        bade_blend_sebelumnya = float(st.session_state.get('bade_blend_sebelumnya', 0))
        
        # Transaction data
        debitur_trx = float(st.session_state.get('debitur_trx', 0))
        debitur_perdagangan = float(st.session_state.get('debitur_perdagangan', 0))
        bade_kol1 = float(st.session_state.get('bade_kol1', 0))
        bade_kol1_bulan_sebelumnya = float(st.session_state.get('bade_kol1_bulan_sebelumnya', 0))
        
        # Booking data
        nett_booking_kur = float(st.session_state.get('nett_booking_kur', 0))
        nett_booking_kum = float(st.session_state.get('nett_booking_kum', 0))
        nett_booking_leads_kur = float(st.session_state.get('nett_booking_leads_kur', 0))
        nett_booking_leads_kum = float(st.session_state.get('nett_booking_leads_kum', 0))
        
        # Agent & USAK data
        usak_bulan_ini = float(st.session_state.get('usak_bulan_ini', 0))
        usak_bulan_sebelumnya = float(st.session_state.get('usak_bulan_sebelumnya', 0))
        agen_ac = float(st.session_state.get('agen_ac', 0))
        agen_kelolaan = float(st.session_state.get('agen_kelolaan', 0))
        
        # AGF data
        agf_cukup_kol1 = float(st.session_state.get('agf_cukup_kol1', 0))
        debitur_kol1 = float(st.session_state.get('debitur_kol1', 0))

        # 2. Basic calculations
        bade_blend = bade_kur + bade_kum
        
        # Target grading mapping
        target_grading_map = {
            "Trainee": 1,
            "Junior": 2_000_000_000,
            "Senior": 4_000_000_000,
            "Executive": 10_000_000_000
        }
        target_grading = target_grading_map.get(grading, 0)
        
        # Calculate transaction and KOL ratios
        trx_deb = debitur_trx / debitur_perdagangan if debitur_perdagangan != 0 else 0
        kol_lancar = bade_kol1 / bade_kol1_bulan_sebelumnya if bade_kol1_bulan_sebelumnya != 0 else 0
        
        # 3. Determine criteria
        kriteria_penentu = (
            (1 if bade_blend >= target_grading else 0) +
            (1 if trx_deb >= 0.1 or debitur_perdagangan == 0 else 0) +
            (1 if kol_lancar > 0 and kol_lancar >= 0.99 else 0)
        )
        
        # 4. Parameter multiplier based on grading and criteria
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
        parameter_pengali = parameter_pengali_map.get((grading, kriteria_penentu), 1.0)
        
        # 5. Booking target parameters
        parameter_target_booking = {
            "Trainee": 350_000_000,
            "Junior": 500_000_000,
            "Senior": 850_000_000,
            "Executive": 1_200_000_000
        }.get(grading, 0)
        
        # 6. Calculate net booking and percentages
        nett_booking_blend = nett_booking_kur + nett_booking_kum
        persentase_nett_booking_blend = (
            nett_booking_blend / parameter_target_booking if parameter_target_booking != 0 else 0
        )
        
        def determine_booking_multiplier():
            if persentase_nett_booking_blend >= 1.0:  # >= 100%
                return 1.0 if bade_blend >= bade_blend_sebelumnya else 0.7
            elif persentase_nett_booking_blend >= 0.8:  # >= 80%
                return 0.7
            return 0.3
        
        # 7. Calculate main incentive components
        pengali_main_booking = parameter_pengali * determine_booking_multiplier()
        main_insentif_booking = (nett_booking_blend / 10_000_000) * 10_000 * pengali_main_booking
        
        # 8. Calculate mix booking incentive
        persentase_nett_booking_kum = nett_booking_kum / nett_booking_blend if nett_booking_blend != 0 else 0
        pengali_main_booking_mix = (2 if persentase_nett_booking_kum >= 0.25 else 0) * determine_booking_multiplier()
        main_insentif_booking_mix = (nett_booking_blend / 10_000_000) * 10_000 * pengali_main_booking_mix
        
        # 9. Calculate leads incentive
        persentase_leads_kur = nett_booking_leads_kur / nett_booking_kur if nett_booking_kur != 0 else 0
        persentase_leads_kum = nett_booking_leads_kum / nett_booking_kum if nett_booking_kum != 0 else 0
        
        target_leads = {
            "kur": {"Trainee": 0.15, "Junior": 0.15, "Senior": 0.25, "Executive": 0.25},
            "kum": {"Trainee": 0.60, "Junior": 0.60, "Senior": 0.85, "Executive": 0.85}
        }
        
        pengali_main_leads = (
            1 if persentase_leads_kur >= target_leads["kur"].get(grading, 0) and 
            persentase_leads_kum >= target_leads["kum"].get(grading, 0) else 0
        ) * determine_booking_multiplier()
        
        main_insentif_leads = (nett_booking_blend / 10_000_000) * 10_000 * pengali_main_leads
        
        # 10. Calculate LVM & Agent incentive
        persentase_usak = usak_bulan_ini / usak_bulan_sebelumnya if usak_bulan_sebelumnya != 0 else 0
        persentase_kuadran_ac = agen_ac / agen_kelolaan if agen_kelolaan != 0 else 0
        
        boolean_agen = (
            (grading != "Executive" and persentase_kuadran_ac >= 0.2 and agen_kelolaan < 21) or
            (persentase_kuadran_ac >= 0.2 and persentase_kuadran_ac < 0.5 and agen_kelolaan < 21) or
            (grading == "Executive" and persentase_kuadran_ac >= 0.5 and agen_kelolaan < 31)
        )
        
        pengali_main_lvm_agen = (
            3 if persentase_usak > 1 and boolean_agen else
            1.5 if persentase_usak > 1 or boolean_agen else 0
        ) * determine_booking_multiplier()
        
        main_lvm_agen = (nett_booking_blend / 10_000_000) * 10_000 * pengali_main_lvm_agen
        
        # 11. Calculate AGF incentive
        persentase_agf_cukup_kol1 = agf_cukup_kol1 / debitur_kol1 if debitur_kol1 != 0 else 0
        pengali_main_kecukupan_agf = (2 if persentase_agf_cukup_kol1 >= 0.8 else 0) * determine_booking_multiplier()
        main_kecukupan_agf = (nett_booking_blend / 10_000_000) * 10_000 * pengali_main_kecukupan_agf
        
        # 12. Calculate total incentive
        total_insentif_sales = (
            main_insentif_booking +
            main_insentif_booking_mix +
            main_insentif_leads +
            main_lvm_agen +
            main_kecukupan_agf
        )
        
        # 13. Display results
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
            st.write(f"Total Insentif: {format_rupiah(total_insentif_sales)}")
        
        with st.expander("💡 Detail Komponen Perhitungan"):
            components = [
                ("Main Insentif Booking", main_insentif_booking, pengali_main_booking),
                ("Main Insentif Booking Mix", main_insentif_booking_mix, pengali_main_booking_mix),
                ("Main Insentif Leads", main_insentif_leads, pengali_main_leads),
                ("Main LVM & Agen", main_lvm_agen, pengali_main_lvm_agen),
                ("Main Kecukupan AGF", main_kecukupan_agf, pengali_main_kecukupan_agf)
            ]
            
            for idx, (name, value, multiplier) in enumerate(components, 1):
                st.write(f"\n#### {idx}️⃣ {name}")
                st.write(f"- Nilai: {format_rupiah(value)}")
                st.write(f"- Pengali: {multiplier:.2f}")
            
            st.write("\n#### 🎯 Rasio & Persentase")
            percentages = [
                ("Nett Booking Blend", persentase_nett_booking_blend),
                ("Mix KUM", persentase_nett_booking_kum),
                ("Leads KUR", persentase_leads_kur),
                ("Leads KUM", persentase_leads_kum),
                ("AGF Cukup", persentase_agf_cukup_kol1)
            ]
            
            for name, value in percentages:
                st.write(f"- {name}: {value:.2%}")
                
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