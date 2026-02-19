# Portofolio
Digital Marketing Campaign Analysis: A/B Testing
Project Overview
Proyek ini bertujuan untuk mengevaluasi efektivitas kampanye pemasaran digital melalui metode A/B Testing. Perusahaan menghadapi masalah performa kampanye yang tidak konsisten, yang ditandai dengan penurunan jumlah impressions, clicks, dan purchases pada strategi lama (Control Campaign).

Objectives

Main Metric: Meningkatkan Conversion Rate untuk mendorong volume transaksi.


Guardrail Metrics: Memantau CTR (Click Through Rate) untuk mengukur daya tarik iklan dan CPP (Cost Per Purchase) untuk efisiensi biaya.

Data Understanding & Processing

Dataset: Data bersumber dari Kaggle dengan durasi kampanye selama 1 bulan (Agustus 2019).


Variables: Meliputi Spend [USD], Number of Impressions, Reach, Website Clicks, Searches, View Content, Add to Cart, dan Purchase.


Processing: Penanganan data hilang (missing values), konversi tipe data tanggal, serta feature engineering untuk menghitung nilai CPC, CPM, dan CPP.

Analysis Methodology

Normality Test: Menggunakan uji Shapiro-Wilk. Hasil menunjukkan distribusi data tidak normal pada beberapa metrik utama seperti CTR dan Purchase Conversion Rate.


Hypothesis Testing: Menggunakan metode non-parametrik Mann-Whitney U Test karena data tidak terdistribusi normal.

Key Findings & Results

Conversion Rate: Menunjukkan kenaikan yang signifikan pada Test Group.


CTR: Test Group memiliki CTR 2 kali lebih besar dibanding Control Group, menandakan kreatif iklan jauh lebih menarik bagi audiens.


CPP: Biaya per pembelian pada Test Group sedikit lebih mahal ($4.92) dibandingkan Control Group ($4.56), namun diimbangi oleh volume konversi yang jauh lebih tinggi.

Recommendations

Adopt Test Campaign: Melanjutkan strategi kampanye baru karena terbukti lebih unggul secara konsisten dalam mendorong transaksi.


Creative Benchmarking: Menggunakan elemen visual dan copywriting dari kampanye Test sebagai standar baru untuk iklan berikutnya.


Cost Optimization: Melakukan optimasi biaya untuk menekan CPP seiring dengan peningkatan skala kampanye.

Tech Stack
Language: Python

Libraries: Streamlit (Dashboard), Pandas (Data Manipulation), Plotly (Interactive Visualization)

Statistical Tool: SciPy (Mann-Whitney U Test)