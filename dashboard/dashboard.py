import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set style Seaborn
sns.set_style("whitegrid")

data = pd.read_csv("dashboard/all_data.csv")

# Sidebar
st.sidebar.image("dashboard/img.png", use_container_width=True)
st.sidebar.title("Analisis Bike Sharing")
st.sidebar.write("**Nama:** Arief Setiawan")
st.sidebar.write(
    "**Email:** [mc189d5y1641@student.devacademy.id](mailto:mc189d5y1641@student.devacademy.id)")
st.sidebar.write("**Id Dicoding:** MC189D5Y1641")

# Opsi pemilihan kondisi cuaca di sidebar
weather_options = {
    1: "Cerah",
    2: "Mendung",
    3: "Hujan"
}
selected_weather = st.sidebar.selectbox("Pola Penyewaan Sepeda dengan Kondisi Cuaca:", options=list(
    weather_options.keys()), format_func=lambda x: weather_options[x])

# Dashboard Title
st.title("Bike Sharing Analysis")

# 1. Pola perubahan jumlah penyewaan sepeda dalam sehari
st.subheader("Pola Penyewaan Sepeda dalam Sehari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=data.groupby("hr")[
             "cnt_hourly"].mean(), marker="o", color="b", ax=ax)
ax.set_title("Pola Perubahan Jumlah Penyewaan Sepeda dalam Sehari")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xticks(range(0, 24))
st.pyplot(fig)
st.markdown("""
#### Berdasarkan visualisasi diatas, kita dapat melihat bahwa jumlah penyewaan sepeda memiliki dua puncak utama dalam sehari:  
- **Pagi hari sekitar jam 8.00** → Kemungkinan besar karena orang menggunakan sepeda untuk pergi bekerja atau sekolah.  
- **Sore hari sekitar jam 17.00 - 18.00** → Ini menunjukkan bahwa banyak pengguna sepeda menggunakannya untuk perjalanan pulang setelah bekerja atau sekolah.  

Selain itu, penyewaan sepeda **relatif rendah pada malam hari dan dini hari**, yang masuk akal karena lebih sedikit orang yang beraktivitas di luar rumah pada waktu tersebut. Hal ini berarti pola penyewaan sepeda menunjukkan lonjakan pada jam sibuk kerja, yaitu pagi dan sore, sedangkan siang hingga malam memiliki jumlah penyewaan yang lebih rendah.  
""")
# 2. Pola penyewaan dengan kondisi cuaca terpilih
st.subheader(
    f"Pola Penyewaan Sepeda dengan Kondisi Cuaca:{weather_options[selected_weather]}")
weather_filtered = data[data["weathersit_hourly"] == selected_weather]
st.write("Untuk Mengubah Kondisi Cuaca bisamenggunakan sidebar di sebelah kiri")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=weather_filtered.groupby("hr")[
             "cnt_hourly"].mean(), marker="o", color="g", ax=ax)
ax.set_title(
    f"Pola Penyewaan Sepeda pada Cuaca {weather_options[selected_weather]}")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_xticks(range(0, 24))
st.pyplot(fig)
st.markdown("""            
 Visualisasi diatas menunjukkan pola penyewaan sepeda **hanya untuk cuaca cerah** (**weathersit = 1**), sehingga faktor cuaca tidak berpengaruh pada pola penggunaan sepeda.  

 
Meskipun cuaca stabil:  
- **Puncak penggunaan tetap terjadi di pagi dan sore hari** (sekitar jam 8 dan 17-18).  
- **Siang dan malam hari tetap memiliki jumlah penyewaan yang lebih rendah**.  

Ini berarti bahwa **cuaca bukan faktor utama yang mempengaruhi lonjakan penyewaan**, melainkan **kebiasaan pengguna** seperti commuting (perjalanan kerja dan pulang kerja). Meskiun jam penggunaan sepeda lebih dipengaruhi oleh kebutuhan perjalanan sehari-hari (commuting) dibandingkan dengan cuaca. Bahkan ketika cuaca cerah, pola penggunaan tetap mengikuti jam sibuk kerja. 
""")

# 3. Waktu paling sibuk dalam seminggu
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=data.groupby("weekday_hourly")["cnt_hourly"].mean().reset_index(),
            x="weekday_hourly", y="cnt_hourly", palette="Reds", ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda per Hari")
ax.set_xlabel("Hari")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_xticklabels(["Minggu", "Senin", "Selasa",
                   "Rabu", "Kamis", "Jumat", "Sabtu"])
st.pyplot(fig)
st.markdown("""            
Berdasarkan visualisasi diatas bisa dilihat bahwa:  
- **Hari kerja (Senin - Jumat) memiliki jumlah penyewaan yang lebih tinggi dibanding akhir pekan**.  
- **Puncak penyewaan terjadi pada Selasa hingga Kamis**, sementara Sabtu dan Minggu memiliki jumlah penyewaan lebih rendah.  

Ini menunjukkan bahwa **mayoritas pengguna sepeda menggunakannya untuk perjalanan ke kantor atau sekolah**, sehingga penyewaan sepeda lebih tinggi pada hari kerja.  

Sebaliknya, pada akhir pekan, jumlah penyewaan cenderung turun, yang mungkin disebabkan oleh:  
- Lebih sedikit orang yang bekerja.  
- Penggunaan sepeda untuk rekreasi yang lebih fleksibel dibanding jadwal harian commuting. 
""")