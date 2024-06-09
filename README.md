# Proyek akhir: Menyelesaikan permasalahan perusahaan Jaya Jaya maju
# Business Understanding
Perusahaan jaya jaya maju adalah perusahaan yang bergerak skala multinasional dengan jumlah karyawan yaitu 1470 karyawan. Perusahaan ini telah berdiri sejak tahun 2000 dan telah berumur 24 tahun saat ini. Namun, perusahaan jaya-jaya maju saat ini memiliki permasalahan yang belum pernah terjadi sebelumnya. perusahaan jaya-jaya maju meminta seorang data scientist untuk menganalisis untuk menghasilkan sebuah insight atas permasalahan bisnis serta membuat sebuah keputusan dari data yang telah dianalisis dan membuat sebuah rekomendasi action. Adapun bentuk permasalahan di dalam perusahaan tersebut yaitu sebagai berikut. Terdapat 36 feature di dalam dataset perusahaan Jaya Jaya Maju diantaranya adalah:
1. index = Berisi nilai unique untuk setiap baris
2. EmployeeId = nomor identifikasi karyawan
3. Age = umur karyawan  
4. Attrition = nilai kategori untuk karyawan meninggalkan perusahaan dan tidak meninggalkan perusahaan
5. BusinessTravel = kelaur masuk perusahaan
6. DailyRate = Tarif harian karyawan
7. Department = Divisi perusahaan 
8. DistanceFromHome = Jarak antara rumah karyawan dengan perusahaan
9. Education = pendidikan karyawan
10. EducationField = bagian spesifik pendidikan karyawan
11. EmployeeCount = total karyawan
12. EnvironmentSatisfaction = Kepuasan lingkungan
13. Gender = Jenis kelamin karyawan
14. HourlyRate = Tarif perjam karyawan 
15. JobInvolvement = keterlibatan kerja karyawan  
16. JobLevel = tingkat pekerjaan keryawan  
17. JobRole = Bidang pekerjaan karyawan 
18. JobSatisfaction = kepuasan pekerjaan  
19. MaritalStatus = status menikah
20. MonthlyIncome = Gaji perbulan karyawan
21. MonthlyRate = Tarif perbulan karyawan 
22. NumCompaniesWorked = Tahun bekera di perusahaan 
23. Over18 = apakah karyawan telah berumur 18 tahun ke atas?
24. OverTime = karyawan melakukan overtime atau tidak
25. PercentSalaryHike = percentase kenaikan gaji karyawan
26. PerformanceRating = tingkat kinerja karyawan
27. RelationshipSatisfaction = Kepuasan hubungan  
28. StandardHours = standard kerja perjam karyawan  
29. StockOptionLevel = level pilihan investasi  
30. TotalWorkingYears = total kerja setiap tahun  
31. TrainingTimesLastYear = pelatihan yang diikuti karyawan dalam tahun terakhir  
32. WorkLifeBalance = keseimbangan antara pekerjaan dengan kehidupan
33. YearsAtCompany = tahun di dalam perusahaan
34. YearsInCurrentRole = total tahun di dalam pekerjaan saat ini
35. YearsSinceLastPromotion = total tahun sejak promosi terakhir
36. YearsWithCurrManager = total tahun bersama manager saat ini

# Permasalahan Bisnis
karyawan berperan penting di dalam perusahaan untuk mewujudkan visi dan misi perusahaan. Permasalahan pada karyawan di dalam perusahaan biasanya identik disebabkan oleh internal perusahaan sendiri seperti gaji tidak sesuai dengan jam kerja dan bidang pekerjaan, budaya kerja yang sangat tidak sehat, serta kebijakan-kebijakan yang dibuat dinilai buruk untuk karyawan sehingga kebijakan tersebut dapat menghambat kinerja karyawan. Disetiap bidang atau divisi pekerjaan di dalam perusahaan memiliki kesinambungan secara kontinu sehingga antar divisi dengan divisi lain selalu saling membutuhkan aghar perusahaan terus berproduksi dan menghasilkan keuntungan. Saat ini perusahaan jaya-jaya maju tengah menghadapi permasalahan yaitu lebih dari 10% banyaknya karyawan yang melakukan churn atau attrition. Permasalahan ini jika diabaikan, maka akan jadi hambatan besar untuk perusahaan dalam mencapai visi dan misinya dan bahkan resiko peluang untuk bangkrut sangat besar. Maka dari itu, untuk mengurangi dan mencegah akibat dari masalah itu sendiri saya akan menganalisis masalah tersebut untuk mencari faktor-faktor yang mempengaruhi attrition serta membuat model machine learning untuk memprediksi identifikasi keputusan attrition pada karyawan.

# Cakupan proyek
Di dalam proyek ini mencakup pekerjaan memyiapkan dataset meliputi tahap assesing hingga tahap cleaning pada data jika terdapat duplikat data dan missing value. Selain itu tahap menganalisis data untuk kebutuhan memahami pola data yang dapat disebut tahap exploratory data analisis. Kemudian tahap membuat model machine learning untuk model prediksi pada proyek tersebut serta membuat dashboard bisnis untuk parameter untuk memantau perkembangan masalah pada proyek. Adapun output yang diharapkan dari proyek ini adalah sebagai berikut: 
1. Visualisasi data exploratory data analisis, diharapkan dapat menjadi ringkasan dari data sehingga dapat mempermudah dalam memahami prilaku data.
2. Tabel statistik korelasi, untuk menentukan faktor yang paling berpengaruh terhadap attrition
3. Model machine learning, membuat model machine learning sebagai proses untuk memilih dan menentukan model yang tepat.
4. Evaluate model, mengevaluasi model yang dihasilkan.
5. Model prediksi, membuat model prediksi untuk mengidentifikasi attrition
6. Model Deployment, membuat deployment menggunakan streamlit untuk mempermudah para pemangku kebijakan dan divisi terkait menggunakan prediksi attrition.
7. Dashboard Business.

# Persiapan
1. Sumber data : postgresql://postgres.apbjhbptftppbgeplewk:myprojectjayajayamaju1@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres
2. Setup Environment, dikarenakan saya menggunakan google colab, jadi untuk setup environment nya sedikit berbeda dengan virtual environment anaconda dan lain sebagainya.
berikut tahap-tahap yang harus dilakukan untuk memulai file project saya pada google colab: Tahap pertama, Buka google colab.
tahap kedua, Upload file (My_project_first_expert_level.ipynb) di dalam folder notebook ke google colab. tahap ke tiga, Install library yang tidak secara otomatis disediakan oleh google colab dengan cara >> pip install 'library' serta untuk kebutuhan versi dapat merujuk pada file requirements.txt

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

# Business Dashboard
Adapun untuk memantau perkembangan masalah attrition di dalam perusahaan jaya jaya maju, hal tersebut menggunakan Dashboard yang di mana untuk memantau perkembangan masalah tersebut. berikut penjelasan mengenai isi Dashboard tersebut:
1. Parameter gaji perbulan di setiap bidang pekerjaan menjadi salah satu faktor yang dapat mempengaruhi karyawan keluar dari perusahaan selain faktor-faktor berikutnya. apabila gaji yang diterima tidak sesuai dengan bidang pekerjaan yang dilakukan, maka hal ini dapat menyebabkan attrition.
2. Parameter attrtition berdasarkan bidang pekerjaan dan keterlibatan kerja juga menjadi faktor cukup penting selain gaji bulanan yang diterima oleh karyawan. Jika karyawan kurang terlibat di dalam pekerjaan maka hal ini dapat menyebabkan attrition tinggi yang di mana ini akan berkaitan secara langsung terhadap performance, prestasi dan promosi jabatan karyawan tersebut.
3. Parameter attrition berdasarkan kepuasan lingkungan kerja dan kepuasan hubungan kerja baik antar karyawan maupun dengan atasan. parameter ini merupakan parameter yang menganalisis budaya kerja di dalam perusahaan.  Parameter ini cukup penting di lakukan karena akan menyangkut visi dan misi perusahaan. apabila budaya kerja dinilai buruk, maka karyawan cenderung untuk memilih untuk meninggalkan perusahaan dan mencari perusahaan lain yang memiliki budaya kerja yang tinggi meliputi kepuasan lingkungan yang tinggi dan kepuasan hubungan yang tinggi juga.
4. parameter attrition berdasarkan karyawan yang melakukan overtime. parameter ini dilakukan untuk memantau karyawan yang melakukan attrition dan melakukan overtime sehingga yang tidak secara langsung akan berkaitan dengan work life balance dan gaji perbulan yang diterimanya. Apabila karyawan terus melakukan overtime dan berdampak dengan work life balance serta tidak ada perkembangan dalam gaji perbulan yang diterima oleh karyawan tersebut, maka akan menjadi peluang besar untuk karyawan tersebut untuk meninggalkan perusahaan.
5. Adapun link dashboard untuk submission project ini yaitu sebagai berikut 
6. Link Dashboard : https://public.tableau.com/views/Project_Dashboard_17157405024960/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link

# Conclusion
berdasarkan analisis hingga membangun sebuah model, maka dapat ditarik beberapa poin keputusan.
1. Di dalam proses analisis, di dapatkan satu feature yang memiliki pengaruh kuat terhadap attrition yaitu feature Overtime.
2. Karakteristik karyawan yang meninggalkan perusahaan didominasi oleh gaji yang relatif kurang dari 5000 dollar, seperti pekerjaan di bidang sales representatif, research scientist dan laboratory technician. dari ketiga bidang pekerjaan tersebut merupakan karyawan yang paling banyak melakukan attrition di bidang tersebut.
3. Tidak semua feature memiliki pengaruh kuat terhadap attrition. sehingga di dalam membangun model dipilih 50% dari keseluruhan feature yang dianggap menjadi feature paling panting.

# Action Recomendation
1. Perusahaan disarankan untuk memperhitungkan dan menaikkan gaji karyawan yang melakukan overtime atau lembur kerja. berdasarkan grafik karyawan yang meninggalkan perusahaan adalah karyawan yang melakukan lembur kerja namun gaji lembur yang cenderung tidak besar dalam artian karyawan yang melakukan lembur dan yang tidak mmelakukan lembur memiliki gaji yang tidak cukup berbeda.
1. Perusahaan disarankan untuk memperhatikan kualitas budaya kerja di dalam perusahaan seperti disiplin, amanah, kerjasama yang baik, pola perilaku positive di dalam perusahaan.
2. Perusahaan disarankan untuk menaikkan gaji karyawan di department sales dan resaerch representatif khususnya di bidang pekerjaan sales representatif, research scientist dan laboratory techinician yang dimana gaji mereka masih dibawah 5000 dollar, hal ini dapat dinaikkan menjadi lebih dari 5000 dollar atau minimal 5000 dollar untuk mencegah karyawan memutuskan meninggalkan perusahaan.
3. Perusahaan harus memperhatikan dalam membuat kebijakan terkait keterlibatan kerja karyawan. hal ini dapat menyangkut tingkat kompetisi karyawan untuk bersaing dalam mencari promosi jabatan. Jika karyawan selalu kalah dalam berkompetisi maka hal tersebut akan berdampak kualitas kinerja karyawan tersebut.

# Cara menggunakan script model yang dijalankan secara local
1. buka folder deployment lalu copy path file
2. kemudian buka cmd pada komputer anda lalu tulis >> python (path file copied) lalu run
3. kemudian pastikan environment pada komputer anda telah terinstall python, numpy, scikit-learn dan streamlit
4. Jika belum terinstall anda perlu menginstalnya contoh library streamlit dengan cara >> pip install streamlit
5. khusus versi scikit-learn, pastikan anda menggunakan scikit-learn versi 1.2.2 bukan yang terbaru
3. jika anda sudah menyiapkan library tersebut anda dapat kembali ke poin pertama lalu tulis pada box code selanjutnya >> streamlit run streamlit_project.py lalu run
4. apabila anda berhasil tanpa error, anda akan diarahkan ke local host streamlit dan model prediksi deployment siap digunakan
5. setelah itu silahkan isi kolom kosong di dalam deployment dan pastikan nilai bertipe integer bukan string.
6. khusus untuk kolom feature kategorik anda dapat menyesuaikan yang artinya semakin angka yang anda masukkan besar maka semakin besar pula level tersebut
7. khusus untuk kolom marital status angka 1 untuk single, 2 untuk married dan 3 untuk divorced
8. khusus untuk kolom overtime nilai 1 untuk NO dan 2 untuk YES
9. jika sudah terisi semuanya, silahkan klik tombol prediction test result
