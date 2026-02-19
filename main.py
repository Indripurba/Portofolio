import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Portofolio | Indri Dwiwanty Purba", layout="wide")

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pindah ke:", ["Home & Profil", "Project Background", "Data Analysis", "Kesimpulan & Rekomendasi"])

# --- PAGE 1: HOME & PROFIL ---
if page == "Home & Profil":
    st.title("Welcome to My Portofolio")
    st.subheader("Indri Dwiwanty Purba - Data Analyst")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://drive.google.com/file/d/1MDY9hk7JC-82nsoB7ADxPJGJYsUJPEjL/view?usp=sharing", caption="Indri Dwiwanty Purba") # Ganti dengan link foto Anda
    
    with col2:
        st.markdown("### Experience")
        st.write("- **Data Science Intern** at Id/x Partners")
        st.write("- **Engineering Analyst** at PT Danliris Sukoharjo")
        
        st.markdown("### Education")
        st.write("- **Institut Teknologi Del** - Industrial Engineering")
        st.write("- **Dibimbing** - Data Analyst and Data Science")

# --- PAGE 2: PROJECT BACKGROUND ---
elif page == "Project Background":
    st.title("A/B Testing: Digital Marketing Campaign")
    st.markdown("---")
    
    st.write("""
    Perusahaan menjalankan kampanye digital marketing, namun performa sering kali tidak konsisten. 
    Dilakukan **A/B Testing** untuk membandingkan **Control Campaign** (lama) dan **Test Campaign** (baru).
    """)
    
    st.info("**Objective:** Meningkatkan Conversion Rate dan Revenue dengan mempertimbangkan CTR dan Biaya.")

    # Visualisasi Tren Penurunan (Simulasi Data dari Page 5 PDF)
    st.subheader("Latar Belakang: Tren Penurunan Kampanye Kontrol")
    data_trend = pd.DataFrame({
        'Date': pd.date_range(start='2019-01-01', periods=15),
        'Impressions': [120000, 115000, 112000, 110000, 108000, 105000, 102000, 100000, 98000, 95000, 92000, 90000, 88000, 85000, 82000],
        'Purchases': [520, 510, 505, 490, 480, 460, 440, 430, 420, 400, 380, 360, 340, 320, 310]
    })
    
    fig_trend = px.line(data_trend, x='Date', y='Purchases', title='Penurunan Purchase pada Kampanye Kontrol')
    st.plotly_chart(fig_trend, use_container_width=True)

# --- PAGE 3: DATA ANALYSIS ---
elif page == "Data Analysis":
    st.title("Data Analysis & Testing")
    
    # Metrik Utama
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Main Metric", "Conversion Rate")
    col_m2.metric("Guardrail 1", "CTR (%)")
    col_m3.metric("Guardrail 2", "CPP (Cost Per Purchase)")

    st.markdown("### Hasil Uji Normalitas (Shapiro Wilk)")
    st.warning("Beberapa metrik seperti CTR (Test) dan Search Rate menunjukkan distribusi **Tidak Normal**.")
    st.write("Metode Statistik yang digunakan: **Mann-Whitney U Test**.")

    # Perbandingan Performa (Simulasi Data Page 15-16)
    st.subheader("Comparison: Control vs Test Group")
    comparison_data = pd.DataFrame({
        'Metric': ['CTR (%)', 'CPP (USD)', 'Purchase Volume'],
        'Control': [2.5, 4.56, 100],
        'Test': [5.0, 4.92, 140]
    })
    
    fig_comp = px.bar(comparison_data, x='Metric', y=['Control', 'Test'], barmode='group', title='Perbandingan Metrik Utama')
    st.plotly_chart(fig_comp, use_container_width=True)

# --- PAGE 4: KESIMPULAN & REKOMENDASI ---
elif page == "Kesimpulan & Rekomendasi":
    st.title("Strategic Recommendations")
    
    # Tabel Kesimpulan
    st.subheader("Summary Table")
    summary_df = pd.DataFrame({
        'Metrik': ['Conversion Rate', 'CTR (%)', 'CPP'],
        'Hasil': ['Signifikan Naik', '2x Lebih Besar', 'Sedikit Naik'],
        'Keputusan': ['Pilih Test Campaign', 'Pertahankan Kreativitas', 'Optimasi Biaya']
    })
    st.table(summary_df)

    # Detail Rekomendasi
    with st.expander("Lihat Detail Rekomendasi"):
        st.write("**1. Gunakan Strategi Test:** Konversi terbukti lebih unggul secara volume.")
        st.write("**2. Benchmark Kreatif:** CTR yang tinggi menunjukkan visual/copy pada Test Campaign sangat efektif.")
        st.write("**3. Optimasi Biaya:** Walau volume naik, CPP sedikit lebih mahal ($4.92 vs $4.56). Diperlukan optimasi biaya pada skala besar.")