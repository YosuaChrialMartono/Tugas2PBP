# Referensi
- [https://stackoverflow.com/questions/49183234/how-to-post-data-of-logged-in-user-with-a-form-in-django](https://stackoverflow.com/questions/49183234/how-to-post-data-of-logged-in-user-with-a-form-in-django)
- [https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html](https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html)
- [https://stackoverflow.com/questions/55565726/display-custom-form-in-django-admin](https://stackoverflow.com/questions/55565726/display-custom-form-in-django-admin)
- [https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/)
- [https://docs.djangoproject.com/en/4.1/topics/forms/](https://docs.djangoproject.com/en/4.1/topics/forms/)
- [https://stackoverflow.com/questions/49183234/how-to-post-data-of-logged-in-user-with-a-form-in-django](https://stackoverflow.com/questions/49183234/how-to-post-data-of-logged-in-user-with-a-form-in-django)
- [https://docs.djangoproject.com/en/4.1/topics/db/queries/](https://docs.djangoproject.com/en/4.1/topics/db/queries/)
- [https://stackoverflow.com/questions/311188/how-do-i-edit-and-delete-data-in-django](https://stackoverflow.com/questions/311188/how-do-i-edit-and-delete-data-in-django)
- [Tutorial Lab 3 PBP](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-3/)

# Pertanyaan Tugas 4

### 1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF (Cross Site Request Forgery) adalah bentuk perlindungan django pada serangan melalui request. Dikutip dari [owasp.org](https://owasp.org/www-community/attacks/csrf) serangan ini dapat mengakibatkan kerusakan yang cukup signifikan bila mengenai user dan mungkin fatal apabila mengenai akun administratif. Ia bekerja dengan membuat sebuah token random yang akan dicocokan dengan token pengirim request. Apabila tidak ada potongan kode ini di dalam elemen <form> maka request kita tidak akan mengirimkan token sehingga tidak akan dilakukan.

### 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, melalui [referensi](https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html) yang saya gunakan untuk mengerjakan tugas ini dijelaskan bahwa ada banyak sekali cara untuk menampilkan form dan cara kita membuatnya sangatlah fleksibel. Salah satu caranya adalah dengan mengiterasi setiap field secara manual dan membuat semua attributes yang ingin kita letakkan kepada field tersebut.

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
![FLOW SS](/todolist/Flow.png)
Mengacu kepada PPT 05 - Form, Authentication, Session, and Cookie Kelas PBP C 2022/2023 maka alurnya adalah sebagai berikut.
1. User memasukkan address untuk submisi.
2. Browser mengenerate http request kepada address tersebut.
3. Server menerima request tersebut dan memilih views yang tepat dan mengirimkannya kepada browser.
4. Browser menerima viewsnya dalam bentuk HTML dan menampilkannya kepada User.
5. User mengisi form sesuai dengan apa yang Ia dapatkan di browser.
6. Browser mengenerate http request untuk submisi dari user berdasarkan viewsnya kepada server.
7. Server menghandle request tersebut sesuai dengan apa yang diinginkan.
8. Server mengembalikan HTML view ke browser yang akan dilihat oleh user.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Saya mengimplementasikan checklist di atas dengan melakukan google serta bertanya ke teman-teman saya terutama Azhra Yasna Azka dengan npm 2106705291 yang mengarahkan saya ke dokumentasi yang tepat dan yang harus saya baca. Semua referensi yang saya gunakan telah di list di awal file. Untuk flownya sendiri saya membuat app baru dengan ```python manage.py startapp todolist``` lalu membuat model baru beserta formnya di models.py serta mengimportnya ke views.py untuk digunakan dalam fungsi ```create_task``` yang diberikan syarat login sesuai dengan tutorial lab 3. Function ```create_task``` tadi akan membawa kita ke forms model ```Task``` dan membuat request untuk menyimpan data yang kita input. Jika data yang kita inpud valid maka akan disave ke database dengan ```task_form.save()```. Setelah itu data baru kita akan ditampilkan di ```show_todolist()``` yang hanya akan menunjukkan user yang sesuai setelah data di model difilter.

# Pertanyaan Tugas 5
### 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
* Inline CSS menerapkan style yang ingin kita terapkan di dalam tag elemen itu sendiri. Contoh : `<p style="color:blue;">`. Kelebihan dari Inline CSS adalah kita dapat dengan cepat menerapkan suatu perubahan yang spesifik dan dapat kita bandingkan dengan perubahan lainnya di dalam file. Namun, kekurangannya adalah kita hanya bisa menerapkannya pada satu tag dan apabila ingin kita duplikasi efeknya harus kita lakukan secara berkali-kali.

* Internal CSS menerapkan style pada file html itu sendiri. Internal CSS akan dimasukkan kedalam tag `<style>` di dalam tag `<head>` dengan segala macam elemennya. Kelebihan darii Internal CSS adalah kita tidak perlu membuat file CSS baru yang harus kita import ke dalam HTML jika kita hanya memiliki sedikit atau personalisasi yang spesifik kepada satu file. Namun, ini berarti bahwa kita tidak dapat menggunakan style yang sama pada HTML yang berbeda tanpa harus melakukan modifikasi yang sama sehingga akan menjadi kurang efektif apabila ingin diterapkan kepada banyak file sekaligus.

* External CSS menerapkan style pada file css yang berbeda dari file HTML. External CSS sebenarnya sama dengan Internal CSS dengan perbedaan ia tidak disimpan lagi di dalam tag html seperti `<style>` atau `<head>` dan hanya berisi selector serta element yang ingin diubahnya. Kelebihan dari External CSS adalah sifatnya yang dapat diterapkan ke berbagai file sekaligus sehingga ia lebih efektif untuk memodifikasi banyak file HTML. Namun, karena ia sifatnya diimport dari luar maka jika terjadi gagal import maka file HTML bisa saja tidak memiliki style saat diload.

### 2. Jelaskan tag HTML5 yang kamu ketahui.
* Tag `<h1>` sampai `<h6>` yang membuat heading dengan kebesaran yang ditentukan dengan nomor di heading. Satu paling besar dan 6 paling kecil.
* Tag `<p>` untuk membuat paragraf atau teks normal di dalam html.
* Tag `<div>` untuk membuat division atau mengelompokkan konten di dalam html sehingga dapat kita berikan perlakuan yang berbeda kepada banyak konten sekaligus.
* Tag `<a>` untuk memasukkan link ke dalam html yang akan meredirect kita ke suatu tempat saat diklik baik itu function dalam project atau website di luar project.
* Tag `<title>` untuk memberikan nama kepada kolom web yang sedang kita buka. Biasanya akan diletakkan di dalam tag `<head>`.
* Dan masih banyak lagi yang belum saya ketahui ataupun yang belum saya sebutkan.

### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Selector yang saya ketahui ada tiga yakni :
1. Element selector yang menerapkan style pada suatu tag spesifik seperti `<h1>` atau `<p>`. Selector ini diterapkan dengan langsung menulis tag yang diinginkan dan elemen yang ingin diganti di dalam `{}`. Contoh, diambil dari lab 4:
```css
h1 {
  color: white;
  margin: 10px;
}```
2. ID Selector yang menerapkan style pada suatu tag yang kita berikan id tertentu. Misal kita memiliki div dengan id="Header" maka kita dapat menerapkan style dengan menggunakan #Header {}. Contoh :
 Code di Html
 ```html
 <div id="Header">
    ...
  </div>
  ```
 Code di CSS
 ```css
    #header {
    background-color: blue;
    margin: 0;
    }
 ```
3. Class Selector menerapkan style pada suatu class. Berbeda dengan ID selector Class selector diawali dengan `.` di dalam css. Untuk perbedannya sendiri tidak terlalu banyak tapi kita dapat menggunakan class selector untuk menerapkan framework lainnya seperti bootstrap untuk mempercantik kode kita.
Contoh :
Code di Html
```html
<div class="title">
    ...
    </div>
```
Code di css
```css
.title{
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 44px;
    float: left;
    width: 1519px;
}
```
### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Untuk checklist di atas saya menggunakan bootstrap sebagai landasan saya untuk memberikan style. Pertama-tama kita perlu mengimport stylesheet bootstrap ke dalam file HTML dengan memasukkan `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous"/>` kedalam tag `<head>`.
Karena kita perlu untuk mengedit masing-masing field di dalam form maka kita perlu untuk merender masing-masing field secara manual, untuk hal tersebut saya menggunakan referensi [ini](https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html). Setelah dirender secara manual lalu kita dapat menerapkan style bootstrap pada masing-masing field. Saya membuat row untuk setiap field serta field tagnya lalu merapihkannya dengan margin dan juga ukuran kolomnya. 
Untuk card sendiri saya membuat sebuah row untuk memuat jumlah card yang sesuai dengan media yang telah saya loop sehingga satu task akan membuat satu card. Card ini sendiri lalu saya terapkan style sesuai dengan apa yang bisa saya dapatkan dari bootstrap documentation.
Untuk Responsive media saya menggunakan col-lg, col-md, col-sm, dan col sebagai class bootstrap yang akan mengatur panjangnya kolom saya sesuai dengan media yang sedang digunakan.