import streamlit as st
from modul01 import calculate_risk, risk_category

# Konfigurasi halaman
st.set_page_config(page_title="Cek Risiko Diabetes", page_icon="🩺", layout="wide")

# CSS Global untuk Background Putih
st.markdown("""
<style>
    /* Background putih penuh */
    body {
        background: white; /* Putih */
        color: black; /* Teks hitam */
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
    }
    .stApp {
        background: white; /* Putih */
    }
    /* Sidebar putih */
    .css-1d391kg { /* Kelas Streamlit untuk sidebar */
        background: white; /* Putih */
        color: black; /* Teks hitam */
        border-radius: 0;
        padding: 20px;
    }
    /* Main area putih */
    .css-1lcbmhc { /* Kelas Streamlit untuk main */
        background: white; /* Putih */
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
    }
    /* Responsif: Tetap putih di mobile */
    @media (max-width: 768px) {
        body {
            background: white;
        }
        .css-1d391kg {
            background: white;
        }
    }
</style>
""", unsafe_allow_html=True)

# Navigasi multi-page menggunakan sidebar
st.sidebar.title("🩺 Cek Risiko Diabetes")
page = st.sidebar.selectbox("Pilih Halaman :", ["Home", "Input Data", "Kalkulasi Risiko", "Hasil"])

# Data global untuk menyimpan input (gunakan session_state untuk persistensi)
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = None

# Halaman 1: Landing Page
if page == "Home":

    #CSS kustom untuk landing page (putih dengan animasi)
    st.markdown("""
    <style>
        /* CSS untuk Landing Page - Tema Putih dengan Animasi */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .main-title {
            font-size: 3em;
            text-align: center;
            color: black; /* Hitam */
            margin-bottom: 20px;
            font-weight: bold;
            animation: fadeInUp 1s ease-out;
        }
        .description {
            font-size: 1.3em;
            line-height: 1.7;
            color: black; /* Hitam */
            margin: 20px 0;
            animation: fadeInUp 1.2s ease-out;
        }
        .feature-list {
            list-style-type: none;
            padding: 0;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        .feature-list li {
            margin: 10px 15px;
            padding: 50px 25px;
            background-color: white; /* Putih */
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            font-weight: bold;
            color: black; /* Hitam */
            transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
            animation: fadeInUp 0.5s ease-out, pulse 2s infinite; /* Fade-in + pulse */
        }
        .feature-list li:nth-child(1) {
            animation-delay: 0.5s; /* Delay untuk item pertama */
        }
        .feature-list li:nth-child(2) {
            animation-delay: 1s; /* Delay untuk item kedua */
        }
        .feature-list li:nth-child(3) {
            animation-delay: 1.5s; /* Delay untuk item ketiga */
        }
        .feature-list li:hover {
            transform: translateY(-10px) scale(1.1); /* Naik dan besar saat hover */
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            background-color: #f0f0f0; /* Abu-abu muda saat hover */
            color: #333; /* Teks lebih gelap */
        }
        .image-placeholder {
            margin: 30px auto;
            max-width: 100%;
            height: auto;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            animation: fadeInUp 2s ease-out;
        }
        .call-to-action {
            margin-top: 30px;
            font-size: 1.2em;
            color: black; /* Hitam */
            font-weight: bold;
            background-color: white; /* Putih */
            padding: 10px 20px;
            border-radius: 10px;
            display: inline-block;
            animation: fadeInUp 2.5s ease-out;
        }
        /* Responsif untuk mobile */
        @media (max-width: 768px) {
            .main-title { font-size: 2.2em; }
            .description { font-size: 1.1em; }
            .feature-list { flex-direction: column; align-items: center; }
            .feature-list li {
                animation: fadeInUp 0.5s ease-out; /* Sederhanakan animasi di mobile */
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Konten halaman dengan kelas CSS
    st.markdown('<div class="landing-container">', unsafe_allow_html=True)
    st.markdown('<div class="main-title">🩺 Selamat Datang di Aplikasi Cek Risiko Diabetes</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Aplikasi ini membantu Anda mengecek risiko diabetes berdasarkan data pribadi. Diabetes adalah kondisi kronis yang dapat dicegah dengan gaya hidup sehat.</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="feature-list">
        <li>Yuk! Input data sederhana</li>
        <li>Lalu, Kalkulasi risikonya</li>
        <li>Dan Cek Saran Pencegahannya</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown('<div class="call-to-action">Navigasi ke halaman berikutnya untuk mulai!</div>', unsafe_allow_html=True)
    st.image("foto.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Halaman 2: Input Data
elif page == "Input Data":
    st.title("📝 Input Data Anda")
    st.markdown("Masukkan data berikut untuk kalkulasi risiko diabetes.")
    
    with st.form("input_form"):
        age = st.number_input("Usia (tahun)", min_value=0, value=0, step=1)
        weight = st.number_input("Berat Badan (kg)", min_value=0, value=0, step=1)
        height = st.number_input("Tinggi Badan (cm)", min_value=0, value=0, step=1)
        family_history = st.selectbox("Riwayat Keluarga Diabetes?", ["Tidak", "Ya"])
        activity_level = st.selectbox("Tingkat Aktivitas Fisik?", ["Rendah", "Sedang", "Tinggi"])
        submitted = st.form_submit_button("Simpan Data")
        
        if submitted:
            st.session_state.user_data = {
                'age': age,
                'weight': weight,
                'height': height,
                'family_history': family_history,
                'activity_level': activity_level
            }
            st.success("Data tersimpan! Lanjut ke halaman Kalkulasi Risiko.")

# Halaman 3: Kalkulasi Risiko
elif page == "Kalkulasi Risiko":
    st.title("🔍 Kalkulasi Risiko Diabetes")
    if not st.session_state.user_data:
        st.warning("Silakan isi data di halaman Input Data terlebih dahulu.")
    else:
        data = st.session_state.user_data
        st.markdown("Data Anda:")
        st.json(data)
        
        if st.button("Hitung Risiko"):
            # Panggil fungsi dari modul
            score = calculate_risk(data)
            st.session_state.risk_score = score
            st.success(f"Skor risiko dihitung: {score}. Lihat hasil di halaman Hasil.")

# Halaman 4: Hasil
elif page == "Hasil":
    st.title("📊 Hasil Cek Risiko Diabetes")
    if st.session_state.risk_score is None:
        st.warning("Silakan lakukan kalkulasi di halaman Kalkulasi Risiko.")
    else:
        score = st.session_state.risk_score
        category = risk_category(score)
        st.metric("Skor Risiko", score)
        st.subheader(f"Tingkat Risiko: {category}")
        
        if category == "Rendah":
            st.success("Risiko Anda rendah. Jaga pola hidup sehat!")
        elif category == "Sedang":
            st.warning("Risiko sedang. Periksa kesehatan secara berkala.")
        else:
            st.error("Risiko tinggi. Konsultasikan dokter segera.")
        
        st.markdown("*Saran Pencegahan:* Olahraga rutin, makan seimbang, hindari gula berlebih.")