import streamlit as st

# Inisialisasi data di Session State
def initialize_session():
    if "mobil_data" not in st.session_state:
        st.session_state["mobil_data"] = [
            {"ID_Mobil": 1, "Nama_Mobil": "Toyota Avanza", "Tipe_Mobil": "MPV", "Status_Mobil": "Tersewa", "Lokasi": "Jl. Thamrin No. 3, Jakarta Pusat", "Customer_ID": 101},
            {"ID_Mobil": 2, "Nama_Mobil": "Honda CR-V", "Tipe_Mobil": "SUV", "Status_Mobil": "Rusak", "Lokasi": "Jl. Raya Cawang No. 10, Jakarta Timur", "Customer_ID": 102},
            {"ID_Mobil": 3, "Nama_Mobil": "Suzuki Ertiga", "Tipe_Mobil": "MPV", "Status_Mobil": "Standby", "Lokasi": "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan", "Customer_ID": None},
            {"ID_Mobil": 4, "Nama_Mobil": "Honda Civic", "Tipe_Mobil": "Sedan", "Status_Mobil": "Standby", "Lokasi": "Jl. Raya Kebayoran Baru No. 5, Jakarta Selatan", "Customer_ID": None}
        ]

# Fungsi untuk menampilkan data mobil
def display_mobil():
    st.subheader("Data Mobil")
    st.table(st.session_state["mobil_data"])

# Fungsi untuk menambahkan data mobil
def input_mobil():
    st.subheader("Tambah Data Mobil")
    id_mobil = st.number_input("Masukkan ID Mobil:", min_value=1, step=1)
    nama_mobil = st.text_input("Masukkan Nama Mobil:")
    tipe_mobil = st.selectbox("Pilih Tipe Mobil:", ["MPV", "SUV", "Sedan"])
    status_mobil = st.selectbox("Pilih Status Mobil:", ["Standby", "Tersewa", "Rusak", "Sedang Mekanik"])
    lokasi = st.text_input("Masukkan Lokasi Mobil:")
    customer_id = st.text_input("Masukkan Customer ID (kosongkan jika tidak ada):")

    if st.button("Tambah Data"):
        customer_id = int(customer_id) if customer_id else None
        mobil_baru = {
            "ID_Mobil": id_mobil,
            "Nama_Mobil": nama_mobil,
            "Tipe_Mobil": tipe_mobil,
            "Status_Mobil": status_mobil,
            "Lokasi": lokasi,
            "Customer_ID": customer_id
        }
        st.session_state["mobil_data"].append(mobil_baru)
        st.success("Data mobil berhasil ditambahkan!")

# Fungsi untuk memperbarui data mobil
def update_mobil():
    st.subheader("Perbarui Data Mobil")
    id_mobil = st.number_input("Masukkan ID Mobil yang ingin diperbarui:", min_value=1, step=1)
    mobil = next((m for m in st.session_state["mobil_data"] if m["ID_Mobil"] == id_mobil), None)

    if mobil:
        st.write("Data Mobil Lama:")
        st.json(mobil)

        # Input untuk pembaruan data
        nama_mobil = st.text_input("Nama Mobil baru (kosongkan jika tidak ada):", value=mobil["Nama_Mobil"])
        tipe_mobil = st.selectbox("Tipe Mobil baru:", ["MPV", "SUV", "Sedan"], index=["MPV", "SUV", "Sedan"].index(mobil["Tipe_Mobil"]))
        status_mobil = st.selectbox("Status Mobil baru:", ["Standby", "Tersewa", "Rusak", "Sedang Mekanik"], index=["Standby", "Tersewa", "Rusak", "Sedang Mekanik"].index(mobil["Status_Mobil"]))
        lokasi = st.text_input("Lokasi Mobil baru (kosongkan jika tidak ada):", value=mobil["Lokasi"])
        customer_id = st.text_input("Customer ID baru (kosongkan jika tidak ada):", value=str(mobil["Customer_ID"]) if mobil["Customer_ID"] else "")

        if st.button("Perbarui Data"):
            mobil["Nama_Mobil"] = nama_mobil
            mobil["Tipe_Mobil"] = tipe_mobil
            mobil["Status_Mobil"] = status_mobil
            mobil["Lokasi"] = lokasi
            mobil["Customer_ID"] = int(customer_id) if customer_id else None
            st.success("Data mobil berhasil diperbarui!")
    else:
        st.error("Mobil dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menghapus data mobil
def delete_mobil():
    st.subheader("Hapus Data Mobil")
    id_mobil = st.number_input("Masukkan ID Mobil yang ingin dihapus:", min_value=1, step=1)

    if st.button("Hapus Data"):
        st.session_state["mobil_data"] = [mobil for mobil in st.session_state["mobil_data"] if mobil["ID_Mobil"] != id_mobil]
        st.success("Data mobil berhasil dihapus!")

# Menu utama
def main():
    initialize_session()
    st.title("Manajemen Data Mobil")
    menu = st.sidebar.selectbox("Menu:", ["Display Data", "Input Data", "Update Data", "Delete Data"])

    if menu == "Display Data":
        display_mobil()
    elif menu == "Input Data":
        input_mobil()
    elif menu == "Update Data":
        update_mobil()
    elif menu == "Delete Data":
        delete_mobil()

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
