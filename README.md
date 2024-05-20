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
Berikut merupakan cakupan di dalam proyek ini:
Output:
1. 
Input:
1.
# Setup Environment
1. pip install pandas sqlachemy
2. pip install streamlit
# Persiapan
Sumber data : postgresql://postgres.apbjhbptftppbgeplewk:myprojectjayajayamaju1@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres

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
1. Di dalam proses analisis, di dapatkan satu feature yang memiliki pengaruh kuat terhadap attrition yaitu feature Overtime
2. Tidak semua feature memiliki pengaruh kuat terhadap attrition. sehingga di dalam membangun model dipilih 50% dari keseluruhan feature yang dianggap menjadi feature paling panting.
# Action Recomendation
1. Perusahaan disarankan untuk memperhatikan budaya kerja di dalam perusahaan.
2. Perusahaan disarankan untuk banyak mempertimbangkan dengan gaji perbulan yang didapat oleh karyawan khususnya karyawan yang melakukan Overtime.
3. Perusahaan harus memperhatikan dan membuat kebijakan terkait keterlibatan kerja karyawan.

# Cara menggunakan model prediksi
1. Isi semua data pada kolom feature streamlit
2. Pastikan input data hanya dengan angka saja
3. Jangan menggunakan spasi atau whitespace diantara angka
4. Jangan menggunakan tanda titik atau koma untuk memisah digit. for example: monthly rate = 2555
5. Untuk kolom kategori gunakan angka 1 sebagai kategori (sangat lemah) hingga 5 kategori (sangat tinggi)

