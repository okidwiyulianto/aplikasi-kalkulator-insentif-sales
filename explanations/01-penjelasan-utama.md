# Penjelasan Kode Kalkulator Insentif Sales

## 1. Import dan Setup Awal
```python
import streamlit as st
import locale
```
- **Analogi**: Seperti membawa peralatan sebelum memulai memasak
- `streamlit`: Framework untuk membuat web app, seperti dapur tempat memasak
- `locale`: Modul untuk format angka/mata uang, seperti alat untuk menghias makanan

## 2. Format Rupiah
```python
def format_rupiah(value):
```
- **Analogi**: Seperti menghias angka agar terlihat seperti uang Rupiah
- **Contoh**: `1000000` → `Rp1.000.000,00`
- **Visualisasi**:
```
Input: 1000000
↓ (proses format)
Output: Rp1.000.000,00
```

## 3. Setup Halaman
```python
def setup_page_config():
```
- **Analogi**: Seperti menata ruangan sebelum tamu datang
- Mengatur judul, ikon, dan tata letak halaman
- **Visualisasi**:
```
Window Title: "KISS - Versi 1.0.1" 💋
Layout: Centered
Sidebar: Collapsed
```

## 4. Header dan Disclaimer
```python
def show_header():
```
- **Analogi**: Seperti papan nama dan peringatan di pintu masuk
- Menampilkan judul aplikasi dan disclaimer penting
- **Visualisasi**:
```
=========================
Kalkulator Insentif Sales
=========================
⚠️ DISCLAIMER ⚠️
[kotak kuning dengan peringatan]
-------------------------
```

## 5. State Management
```python
def initialize_session_state():
```
- **Analogi**: Seperti buku catatan untuk mengingat data
- Menyimpan status form dan input pengguna
- **Visualisasi**:
```
📒 Session State
- form_submitted: False
- form_reset: False
```

## 6. Form Input
Beberapa fungsi input seperti:
```python
def show_sales_data_input()
def show_baki_debet_input()
# dst...
```
- **Analogi**: Seperti formulir yang harus diisi
- Setiap bagian meminta data spesifik
- **Visualisasi**:
```
📝 Data Sales
┌─────────────────┐
│ NIP: [______] │
│ Nama: [______] │
│ Grading: [▼] │
└─────────────────┘
```

## 7. Perhitungan Insentif
```python
def calculate_incentive():
```
- **Analogi**: Seperti koki yang mengolah bahan menjadi hidangan
- Memproses semua input menjadi hasil insentif
- **Visualisasi**:
```
Input Data → Proses Perhitungan → Hasil Insentif
   📊        →       🔄         →     💰
```

## 8. Main Function
```python
def main():
```
- **Analogi**: Seperti resep utama yang mengatur urutan memasak
- Menjalankan semua fungsi dalam urutan yang tepat
- **Visualisasi**:
```
Setup → Header → Input Forms → Calculate → Display
  🔧  →   📋   →     📝      →    🔄    →    📊
```

## Fitur Utama
1. **Input Data**:
   - Data Sales (NIP, Nama, Grading)
   - Baki Debet (KUR, KUM)
   - Debitur Transaksi
   - Dan lainnya

2. **Perhitungan**:
   - Insentif Booking
   - Insentif Mix
   - Insentif Leads
   - LVM & Agen
   - Kecukupan AGF

3. **Output**:
   - Total Insentif
   - Detail Komponen
   - Rasio & Persentase

## Cara Kerja
1. User mengisi form
2. Data disimpan di session state
3. Saat tombol hitung ditekan:
   - Data diambil dari session state
   - Dihitung sesuai rumus
   - Hasil ditampilkan dengan format Rupiah

## Keamanan
- Penanganan error untuk pembagian nol
- Validasi input
- Format mata uang yang konsisten

Aplikasi ini seperti kalkulator khusus yang membantu sales menghitung insentif mereka secara otomatis dan akurat.