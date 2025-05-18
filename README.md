# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya jaya Institut adalah lembaga pendidikan yang berkomitmen untuk meningkatkan kualitas akademik siswanya. ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. 
Salah satu tantangan utama dalam dunia pendidikan adalah hingga saat ini 
ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. 
Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Mengidentifikasi sejak dini 
siswa yang berisiko mengalami penurunan prestasi atau tidak mencapai target akademik. Dengan memahami faktor-faktor yang memengaruhi kinerja siswa, 
pihak institusi dapat mengambil langkah-langkah yang tepat untuk meningkatkan hasil belajar.

## Permasalahan Bisnis

1. Tingginya tingkat dropout

2. Kesenjangan antara mahasiswa dengan dan tanpa beasiswa

3. Mahasiswa yang hadir di malam hari cenderung dropout lebih tinggi

4. Pengaruh status pemindahan (displaced)

5. Pengaruh status utang mahasiswa

## Cakupan Proyek

* Analisis performa mahasiswa berdasarkan berbagai dimensi seperti gender, waktu kehadiran, status beasiswa, status utang, dan status perpindahan.

* Identifikasi faktor utama penyebab dropout untuk membantu institusi merancang strategi penanggulangan yang efektif.

* Segmentasi mahasiswa berdasarkan risiko untuk mengetahui kelompok yang rentan gagal atau dropout.

* Penyusunan rekomendasi strategi berbasis data untuk meningkatkan tingkat kelulusan.

## Persiapan

Sumber data : [Student Performance](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup Environtment : ``` pip install numpy pandas matplotlib seaborn scikit-learn==1.2.2 joblib==1.4.2 streamlit==1.24.1 ```

## Business Dashboard

Link : [Dashboard Student Performance](https://public.tableau.com/views/studnetperformace/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

![alt text](https://github.com/mfatarsyah/student-performace-Dicoding/blob/main/Dashboard%20student%20performance.png)

Dashboard Tableau ini menyajikan visualisasi menyeluruh mengenai performa mahasiswa berdasarkan beberapa variabel penting. Secara keseluruhan, terdapat 3.630 mahasiswa yang terbagi menjadi dua kelompok utama, yaitu 2.209 mahasiswa yang berhasil lulus (graduate) dan 1.421 mahasiswa yang mengalami putus studi (dropout). Salah satu visualisasi utama menunjukkan distribusi gender, di mana 65,59% adalah perempuan dan 34,41% adalah laki-laki. Visualisasi lainnya memperlihatkan bahwa sebagian besar mahasiswa yang lulus tidak memiliki utang (debtor) dan telah melunasi biaya kuliah mereka. Selain itu, grafik distribusi waktu kehadiran menunjukkan bahwa mahasiswa yang mengikuti kelas pada malam hari lebih rentan terhadap dropout dibanding yang mengikuti kelas di siang hari. Tabel "Displaced & Status" mengindikasikan bahwa mahasiswa yang mengalami pemindahan (displaced) juga memiliki jumlah dropout yang tinggi. Sementara itu, grafik kelulusan berdasarkan status beasiswa memperlihatkan bahwa mahasiswa penerima beasiswa memiliki tingkat kelulusan yang lebih rendah dibanding mereka yang tidak menerima beasiswa. Secara keseluruhan, dashboard ini memberikan gambaran yang informatif mengenai faktor-faktor yang memengaruhi kelulusan mahasiswa, serta mengidentifikasi kelompok-kelompok mahasiswa yang memerlukan perhatian dan intervensi lebih lanjut.

## Menjalankan Sistem Machine Learning

1. Buka terminal atau PowerShell

2. Aktifkan virtual environment yang telah dibuat sebelumnya

3. Masuk ke lokasi dimana file streamlit (streamlit_app.py) berada

4. Jalankan file streamlit dengan perintah berikut ini:

```
streamlit run streamlit_app.py
```

## Link untuk mengakses ptototype streamlit

```
https://student-performace-dicoding-nzptgmdwez6wcg3j3usmgc.streamlit.app/
```

## Conclusion

* Mahasiswa yang hadir pada malam hari, memiliki status displaced,  tidak memegang beasiswa, dan memiliki utang, lebih cenderung mengalami dropout.

* Faktor keuangan dan beban hidup di luar kampus merupakan faktor signifikan yang memengaruhi performa akademik.

* Tindakan intervensi yang tepat sasaran berdasarkan faktor-faktor tersebut dapat membantu menurunkan tingkat dropout dan meningkatkan tingkat kelulusan secara menyeluruh.

## Rekomendasi Action Items

1. Program Pendampingan Khusus untuk Mahasiswa Risiko Tinggi

Buat program mentoring dan dukungan belajar bagi mahasiswa dengan ciri:

* Kehadiran malam hari

* Status beasiswa

* Status "displaced"

* Mahasiswa yang memiliki utang


2. Evaluasi dan Revisi Skema Beasiswa dan Bantuan Keuangan

* Pastikan penerima beasiswa juga mendapatkan dukungan akademik dan sosial

* Buat sistem utang pendidikan yang fleksibel dan tidak membebani mahasiswa selama studi

3. Menyediakan tutor atau mentor, kelas remedial, bimbingan akademik, dan dukungan bagi penerima beasiswa.
