import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv("dashboard/all_data.csv")

# Mapping seasons and weather conditions
season_mapping = {1: "Winter", 2: "Spring", 3: "Summer", 4: "Fall"}
weather_mapping = {
    1: "Clear/Partly Cloudy",
    2: "Misty/Cloudy",
    3: "Light Rain/Snow",
    4: "Heavy Rain/Snow/Storm"
}

day_df["season_label"] = day_df["season"].map(season_mapping)
day_df["weather_label"] = day_df["weathersit"].map(weather_mapping)
day_df["year"] = day_df["yr"].map({0: 2011, 1: 2012})
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# Sidebar
st.sidebar.image("dashboard/img.png", use_container_width=True)
st.sidebar.title("Proyek Akhir Belajar Analisis Data dengan Python: Analisis Bike Sharing")
st.sidebar.write("**Nama:** Arief Setiawan")
st.sidebar.write("**Email:** [mc189d5y1641@student.devacademy.id](mailto:mc189d5y1641@student.devacademy.id)")
st.sidebar.write("**Id Dicoding:** MC189D5Y1641")

# Dashboard Title
st.title("Bike Sharing Analysis ")

# 1. Peminjaman Sepeda Berdasarkan Musim
st.header("1. Pola Peminjaman Sepeda Berdasarkan Musim")
seasonal_trend = day_df.groupby("season_label")["cnt"].mean().sort_values()
season_colors = {"Winter": "#1E90FF", "Spring": "#00FF7F", "Summer": "#FFD700", "Fall": "#FF4500"}

fig, ax = plt.subplots()
sns.barplot(x=seasonal_trend.index, y=seasonal_trend.values, palette=[season_colors[s] for s in seasonal_trend.index])
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.set_title("Pola Peminjaman Sepeda Berdasarkan Musim")
st.pyplot(fig)

st.write("Berdasarkan data, rata-rata jumlah peminjaman sepeda pada setiap musim adalah sebagai berikut:")
st.write("- Musim Dingin (Winter): Sekitar 5.500 peminjaman per hari")
st.write("- Musim Semi (Spring): Sekitar 7.000 peminjaman per hari")
st.write("- Musim Panas (Summer): Sekitar 8.500 peminjaman per hari")
st.write("- Musim Gugur (Fall): Sekitar 9.000 peminjaman per hari")
st.write("Dari angka-angka ini, terlihat bahwa peminjaman sepeda paling tinggi terjadi di musim gugur dan musim panas, sedangkan jumlah peminjaman terendah terjadi di musim dingin. Perbedaan ini kemungkinan besar dipengaruhi oleh faktor cuaca, di mana suhu hangat pada musim panas dan gugur lebih mendukung aktivitas bersepeda dibandingkan dengan musim dingin yang dingin dan mungkin bersalju.")

# 2. Pengaruh Cuaca terhadap Peminjaman Sepeda
st.header("2. Pengaruh Cuaca terhadap Peminjaman Sepeda")
weather_impact = day_df.groupby("weather_label")["cnt"].mean().sort_values()
weather_colors = {
    "Clear/Partly Cloudy": "#FFD700",
    "Misty/Cloudy": "#A9A9A9",
    "Light Rain/Snow": "#4682B4",
    "Heavy Rain/Snow/Storm": "#8B0000"
}

fig, ax = plt.subplots()
sns.barplot(x=weather_impact.index, y=weather_impact.values, palette=[weather_colors[w] for w in weather_impact.index])
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Peminjaman Sepeda")
ax.set_title("Pengaruh Cuaca terhadap Peminjaman Sepeda")
plt.xticks(rotation=15)
st.pyplot(fig)

st.write("Jika kita melihat jumlah rata-rata peminjaman berdasarkan kondisi cuaca:")
st.write("- Cerah/berawan sebagian (Clear/Partly Cloudy): Sekitar 8.400 peminjaman per hari")
st.write("- Berkabut atau berawan (Misty/Cloudy): Sekitar 6.600 peminjaman per hari")
st.write("- Hujan ringan/salju ringan (Light Rain/Snow): Sekitar 4.400 peminjaman per hari")
st.write("- Hujan lebat/salju lebat/badai (Heavy Rain/Snow/Storm): Sekitar 2.100 peminjaman per hari")
st.write("Dari data ini, terlihat bahwa peminjaman sepeda menurun hampir 75% pada kondisi cuaca ekstrem dibandingkan dengan cuaca cerah. Hal ini menunjukkan bahwa cuaca ekstrem sangat mempengaruhi keputusan pengguna untuk menyewa sepeda, kemungkinan karena alasan kenyamanan dan keamanan dalam berkendara.")

# 3. Tren Peminjaman Sepeda dari Tahun ke Tahun
st.header("3. Tren Peminjaman Sepeda dari Tahun ke Tahun")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=day_df["dteday"], y=day_df["cnt"], color="b")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman Sepeda")
ax.set_title("Tren Peminjaman Sepeda Harian (2011-2012)")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("Berdasarkan jumlah total peminjaman:")
st.write("- Tahun 2011: Sekitar 1.24 juta peminjaman")
st.write("- Tahun 2012: Sekitar 2.04 juta peminjaman")
st.write("Dari angka tersebut, terlihat adanya peningkatan sekitar 64% dalam jumlah total peminjaman sepeda dari tahun 2011 ke 2012. Ini menunjukkan bahwa layanan penyewaan sepeda semakin populer seiring waktu. Peningkatan ini bisa disebabkan oleh beberapa faktor, seperti semakin banyaknya pengguna yang beralih ke sepeda sebagai transportasi harian, peningkatan infrastruktur pendukung, atau promosi dari penyedia layanan.")

