# ⚙️ Workflow Automation: ETL Pipeline dengan GX dan MongoDB

Proyek ini bertujuan untuk mengotomatisasi proses Extract-Transform-Load (ETL) menggunakan GX (Great Expectations) untuk validasi data dan MongoDB sebagai penyimpanan data. Dengan memanfaatkan dataset `BankChurner.csv`, pipeline ini memastikan data yang dimuat ke dalam database telah melalui proses pembersihan dan validasi yang ketat.​
## 📁 Struktur Proyek

    -`BankChurner.csv`: Dataset mentah yang berisi informasi pelanggan bank.

    -`extract.py`: Skrip untuk mengekstrak data dari sumber.

    -`transform.py`: Skrip untuk membersihkan dan mentransformasi data.

    -`load.py`: Skrip untuk memuat data yang telah diproses ke MongoDB.

    -`P3_adhi_rizqi.ipynb`: Notebook Jupyter yang mendokumentasikan proses ETL secara keseluruhan.

    -`P3_adhi_rizqi_DAG.py`: Definisi DAG (Directed Acyclic Graph) untuk mengatur alur kerja ETL.

    -`mongodb_success.png`: Tangkapan layar yang menunjukkan data berhasil dimuat ke MongoDB.

    -`workflow_success.png`: Tangkapan layar yang menunjukkan alur kerja ETL berhasil dijalankan.​

## 🔍 Fitur Utama

    -**Automatisasi ETL**: Proses ETL yang terotomatisasi dari ekstraksi hingga pemuatan data.

    -**Validasi Data dengan GX**: Menggunakan Great Expectations untuk memastikan kualitas dan konsistensi data.

    -**Integrasi MongoDB**: Menyimpan data hasil ETL ke dalam database MongoDB untuk kemudahan akses dan analisis lebih lanjut.

    -**Visualisasi Proses**: Menyediakan tangkapan layar sebagai bukti keberhasilan setiap tahap proses.​

## 🛠️ Teknologi yang Digunakan

    -**Python**: Bahasa pemrograman utama untuk scripting ETL.

    -**Jupyter Notebook**: Untuk dokumentasi dan eksplorasi data interaktif.

    -**Great Expectations (GX)**: Alat untuk validasi dan dokumentasi data.

    -**MongoDB**: Database NoSQL untuk penyimpanan data hasil ETL.
