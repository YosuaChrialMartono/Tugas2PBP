Link Heroku : https://tugas2pbp-yosua.herokuapp.com

Perbedaan JSON, XML, dan HTML :
JSON : 
Menyimpan data dalam bentuk key-value pair.
XML :
Menyimpan data dalam tag beserta dengan propertiesnya.
HTML :
Digunakan untuk merender text sesuai bagaimana kita membuatnya. HTML tidak terlimit pada data saja dan juga bisa distyle menggunakan CSS.

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? :
Kita memerlukan data delivery karena data tidak bisa berpindah dengan sendirinya. Melalui internet kita dapat menggunakan data delivery sehingga kita bisa mengautomasi proses pengiriman dan penerimaan data tanpa perlu kita buat secara manual lagi.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu.
    Saya melakukannya sesuai dengan tutorial lab 1 yakni dengan melaksanakan perintah python manage.py startapp mywatchlist di terminal
2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist.
    Saya melakukannya dengan mengikuti contoh arahan di tutorial lab 1 dan menambahkan path('mywatchlist/', include('mywatchlist.urls')), di urls.py project_django sehingga ketika user membuka http://localhost:8000/mywatchlist ia dapat mengakses urls.py app mywatchlist.
3. Membuat sebuah model MyWatchList yang memiliki beberapa atribut.
    Kembali lagi saya menggunakan tutorial lab 1 sebagai contoh untuk pembuatannya. Saya menggunakan field yang sesuai dengan properties yang ingin ditambahkan kedalam models.py mywatchlist seperti DateField() untuk release_date dan IntegerField() untuk rating.
4. Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
    Saya menggunakan django admin untuk menambahkan data secara manual kedalam projek lalu saya mengambil keluaran json dari data tersebut dan memasukkannya kedalam initial_watchlist_data.json sebagai data awal. Untuk pengaplikasian django admin saya mengikuti langkah dari : https://www.tutorialspoint.com/adding-json-field-in-django-models
5. Mengimplementasikan sebuah fitur untuk menyajikan data di poin 4 dalam tiga format:
    Untuk checklist ini saya mengikuti tutorial lab 2 untuk membuat fungsi yang disesuaikan kembali dengan apa yang ingin kita return menggunakan HttpResponse untuk mengembalikan views yang ingin dilihat. Semua fungsi yang telah dibuat akan dimasukkan ke dalam views.py app mywatchlist.
6. Membuat routing sehingga data di atas dapat diakses melalui URL.
    Untuk checklist ini kembali saya menggunakan tutorial lab 2 sebagai landasan saya. Saya menambahkan routing pada urls.py app mywatchlist seperti html/ , xml/ , dan json/ untuk memanggil fungsi yang sesuai dari views.py.
7. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    Untuk deployment ke Heroku karena actions dari tugas 2 sudah sesuai dan juga secrets sudah dibuat maka saya hanya melakukan commit dan push kode ke GitHub. Lalu GitHub akan mempush kode saya ke app tugas 2 kemarin.

Screenshot Postman :
- HTML
![HTML SS](/mywatchlist/HTML_Postman.jpg)
- XML
![XML SS](/mywatchlist/XML_Postman.jpg)
- JSON
![JSON SS](/mywatchlist/JSON_Postman.jpg)