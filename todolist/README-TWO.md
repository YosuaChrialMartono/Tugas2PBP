# Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming berarti program akan dijalankan secara sequential atau berurutan sehingga satu program akan menunggu program lain sebelum dijalankan. Namun, untuk asynchronous programming akan berjalan tanpa urutan atau bisa berjalan secara berdampingan sehingga tidak saling tunggu-menunggu.
# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma Event-Driven Programming berarti bahwa flow dari program ditentukan sepenuhnya dari event seperti input user maupun output dari program atau device eksternal. Dalam tugas ini penerapannya adalah ketika user ingin membuat task baru dengan meng-click tombol create task sehingga akan muncul suatu modal yang akan menyediakan form yang bersangkutan.
# Jelaskan penerapan asynchronous programming pada AJAX.
Dalam programming AJAX asynchronous programming berarti program akan berjalan tanpa menunggu program sebelumnya selesai dijalankan. Sehingga program akan berjalan secara bersamaan dan tidak perlu menunggu satu sama lain.
# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Saya menerapkan tugas kali ini menggunakan beberapa referensi :
1. http://www.learningaboutelectronics.com/Articles/How-to-perform-an-AJAX-POST-request-in-Django.php
2. https://www.w3schools.com/jquery/jquery_dom_set.asp
3. Solusi tutorial 5 PBP. https://github.com/pbp-fasilkom-ui/tutorial-5-example
4. https://youtu.be/j6DFxCs9mf0
5. https://getbootstrap.com/docs/5.2/components/modal/#how-it-works

Pertama-tama saya membuat view json menggunakan contoh dan referensi yang sudah ada dari tutorial dan tugas sebelumnya. Lalu saya menerapkan gabungan dari referensi 2, 3, dan 4 untuk mengambil data dari view json tersebut. 
Untuk AJAX POST Saya menggunakan referensi 5 dari yang sudah disediakan di repository tugas untuk membuat modal serta button untuk memanggil modal tersebut. Lalu saya mengikuti referensi 1 menerapkan AJAX POST dalam tugas saya.