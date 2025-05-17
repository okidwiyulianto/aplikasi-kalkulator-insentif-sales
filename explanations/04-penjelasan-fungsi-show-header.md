# Penjelasan Fungsi `show_header()`

Mari kita bahas baris per baris dengan analogi yang mudah dipahami:

## 1. Definisi Fungsi dan Judul Utama
```python
def show_header():
    """Display application header and disclaimer."""
    st.header("Kalkulator Insentif Sales Sederhana")
```
**Analogi**: Seperti memasang papan nama besar di depan toko. Fungsi ini bertugas menata bagian atas aplikasi.

## 2. Subjudul
```python
st.subheader("Aplikasi web sederhana untuk menghitung insentif sales berdasarkan data portofolionya")
```
**Analogi**: Seperti menambahkan keterangan di bawah papan nama toko yang menjelaskan apa yang dijual di toko tersebut.

## 3. Garis Pemisah
```python
st.markdown("---")
```
**Analogi**: Seperti membuat garis di lantai yang memisahkan area pintu masuk dengan area display toko.

## 4. Kotak Peringatan
```python
st.markdown("""
<div style="
    background-color: rgb(255, 183, 0);
    color: black;
    padding: 15px;
    border-radius: 5px;
    font-size: 1em;
">
```
**Analogi**: Seperti membuat papan peringatan kuning mencolok yang menarik perhatian pengunjung.
- `background-color: rgb(255, 183, 0)` → Warna kuning seperti tanda peringatan
- `padding: 15px` → Memberikan ruang bernafas di sekitar teks
- `border-radius: 5px` → Membuat sudut kotak menjadi lebih lembut
- `font-size: 1em` → Mengatur ukuran teks agar mudah dibaca

## 5. Isi Peringatan
```python
<strong>🚨DISCLAIMER🚨:</strong><br> 
Rumus dan komponen perhitungan mengikuti <b><u>KALKULATOR INSENTIF VERSION 1.0.1</b></u>.<br> 
Pengembang <b><u>tidak bertanggung jawab</b></u> atas kerugian akibat penggunaan data ini.<br> 
Gunakan hanya sebagai <b><u>alat untuk mempermudah dan referensi pendukung.</b></u>
```
**Analogi**: Seperti menulis peringatan penting di papan pengumuman dengan:
- Emoji 🚨 sebagai lampu peringatan
- Teks tebal (`<b>`) untuk penekanan
- Garis bawah (`<u>`) untuk poin-poin penting
- `<br>` untuk membuat baris baru

## 6. Penutup Div dan Garis Akhir
```python
</div>
""", unsafe_allow_html=True)
st.divider()
```
**Analogi**: Menutup papan pengumuman dan membuat garis final pemisah.

## 🎨 Visualisasi Hasil
```
+----------------------------------------+
|     Kalkulator Insentif Sales          |  <- Header
|     Aplikasi web sederhana...          |  <- Subheader
|----------------------------------------|  <- Separator
|  🚨 DISCLAIMER 🚨                     |
|  +---------------------------------+   |
|  |                                 |   |  <- Warning Box
|  |  • Version 1.0.1                |   |
|  |  • Tidak bertanggung jawab      |   |
|  |  • Referensi pendukung          |   |
|  |                                 |   |
|  +---------------------------------+   |
|----------------------------------------|  <- Final Divider
```

Fungsi ini seperti seorang desainer interior yang menata bagian depan aplikasi agar terlihat profesional dan informatif, sambil memastikan pengguna memahami batasan penggunaan aplikasi! 🎨