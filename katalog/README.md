Link app heroku : https://tugas2pbp-yosua.herokuapp.com
Bagan :
![Bagan hubungan](/katalog/Bagan.jpg)

Penjelasan Bagan :
1. User ingin memanggil suatu tampilan maka Ia memasukkan url di browser yang merupakan alamat yang akan kita berikan lajur melalui urls.py
2. urls.py akan mengarahkan perintah user kepada function yang sesuai dan menampilkan hal yang sesuai pula dengan memanggil function views.py
3. views.py akan mempersiapkan tampilan yang ingin dilihat oleh user baik dari sisi data maupun konten.
4. Data yang diterima oleh views.py akan diatur oleh models.py dimana models.py menyediakan data yang dapat dibaca
5. Sisi konten diatur oleh template HTML yang akan dipilih oleh views.py yang kembali lagi disesuaikan dengan keinginan user.
6. Setelah mendapatkan data dan memilih template HTML yang tepat views.py menampilkannya kembali kepada user.

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual enviroment agar program kita dapat berjalan dengan berbagai dependeciesnya dalam satu sistem os yang sama dengan program-program kita yang lainnya dengan mengisolasi program kita dalam "bubble"nya sendiri. Tentu dalam hal ini berarti bahwa sebenarnya kita bisa membuat aplikasi web berbasi Django tanpa menggunakan virtual enviroment. Namun, hal ini berarti bahwa program kita akan crumble di saat dependenciesnya saling bertabrakan ketika ada pengaruh dari luar seperti update module.

- Sumber referensi : https://www.petanikode.com/python-virtualenv/

Bagaimana cara saya melakukan tahapan 1-4?
1. Saya mengambil referensi dari tutorial lab 1 untuk membuat sebuah fungsi yang mereturn sebuah context yang berisi data dari models.py dan html yang ingin dipilih.
2. Dalam hal ini saya membuat path baru di urls.py di app katalog yang mengarahkan kita ke views.py
3. Untuk tahapan ini saya sekali lagi mengambil inspirasi dari tutorial lab 1 dan mengloop semua model yang didapatkan dari database ke dalam HTML.
4. Untuk deployment sendiri karena dari template sudah disediakan workflowsnya dari awal maka saya hanya perlu untuk memasukkan secrets saya seperti HEROKU_APP_NAME dan HEROKU_API_KEYS kepada repository secrets.