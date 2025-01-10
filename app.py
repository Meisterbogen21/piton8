import csv
from datetime import datetime
import os
import streamlit as st

# Nama file dataset
data_file = 'data_sewa_mobil.csv'

# Fungsi untuk memastikan file dataset tersedia
def cek_dataset():
    if not os.path.exists(data_file):
        with open(data_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nama Penyewa", "Nomor KTP", "Nomor Telepon", "Jenis Mobil", "Tanggal Sewa", "Tanggal Kembali"])

# Fungsi untuk menambahkan data sewa mobil
def tambah_data_sewa(nama_penyewa, nomor_ktp, nomor_telepon, jenis_mobil, tanggal_sewa, tanggal_kembali):
    try:
        datetime.strptime(tanggal_sewa, '%Y-%m-%d')
        datetime.strptime(tanggal_kembali, '%Y-%m-%d')
    except ValueError:
        st.error("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
        return False

    data = [nama_penyewa, nomor_ktp, nomor_telepon, jenis_mobil, tanggal_sewa, tanggal_kembali]

    with open(data_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

    st.success("Data sewa berhasil ditambahkan!")
    return True

# Fungsi untuk menampilkan semua data sewa
def tampilkan_data_sewa():
    try:
        with open(data_file, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
            if len(data) > 1:
                st.write("### Data Sewa Mobil")
                st.table(pd.DataFrame(data[0:], columns = ["Penyewa", "No. KTP", "No. Telp", "Jenis Mobil",  "Tanggal Sewa", "Tanggal Kembali"]))  # Menampilkan data tanpa header
            else:
                st.info("Tidak ada data sewa.")
    except FileNotFoundError:
        st.warning("Data sewa belum tersedia.")

# Fungsi untuk mencari data berdasarkan nama penyewa
def cari_data_sewa(nama_penyewa):
    try:
        with open(data_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            hasil = []
            for row in reader:
                if nama_penyewa.lower() in row[0].lower():
                    hasil.append(row)
            if hasil:
                st.write("### Hasil Pencarian")
                st.table(hasil)
            else:
                st.info("Data tidak ditemukan.")
    except FileNotFoundError:
        st.warning("Data sewa belum tersedia.")

# Fungsi untuk menghapus data berdasarkan nama penyewa
def hapus_data_sewa(nama_penyewa):
    try:
        with open(data_file, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)

        header = data[0]
        data_baru = [row for row in data if nama_penyewa.lower() not in row[0].lower()]

        if len(data_baru) == len(data):
            st.info("Data tidak ditemukan atau tidak ada perubahan.")
            return

        with open(data_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data_baru)

        st.success("Data berhasil dihapus!")
    except FileNotFoundError:
        st.warning("Data sewa belum tersedia.")

# Aplikasi Streamlit
def main():
    cek_dataset()
    st.title("Aplikasi Pendataan Sewa Mobil")

    menu = st.sidebar.selectbox("Menu", ["Tambah Data", "Tampilkan Data", "Cari Data", "Hapus Data"])

    if menu == "Tambah Data":
        st.header("Tambah Data Sewa")
        with st.form("form_tambah_data"):
            nama_penyewa = st.text_input("Nama Penyewa")
            nomor_ktp = st.text_input("Nomor KTP")
            nomor_telepon = st.text_input("Nomor Telepon")
            jenis_mobil = st.text_input("Jenis Mobil")
            tanggal_sewa = st.date_input("Tanggal Sewa")
            tanggal_kembali = st.date_input("Tanggal Kembali")
            submitted = st.form_submit_button("Tambah")

            if submitted:
                tambah_data_sewa(nama_penyewa, nomor_ktp, nomor_telepon, jenis_mobil, str(tanggal_sewa), str(tanggal_kembali))

    elif menu == "Tampilkan Data":
        st.header("Tampilkan Data Sewa")
        tampilkan_data_sewa()

    elif menu == "Cari Data":
        st.header("Cari Data Sewa")
        nama_penyewa = st.text_input("Masukkan Nama Penyewa")
        if st.button("Cari"):
            cari_data_sewa(nama_penyewa)

    elif menu == "Hapus Data":
        st.header("Hapus Data Sewa")
        nama_penyewa = st.text_input("Masukkan Nama Penyewa untuk Dihapus")
        if st.button("Hapus"):
            hapus_data_sewa(nama_penyewa)

if __name__ == "__main__":
    main()
