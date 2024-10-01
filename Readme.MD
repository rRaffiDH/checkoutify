## PWS LINK

- PWS Deployment Website : [checkoutify](http://raffi-dary-checkoutify.pbp.cs.ui.ac.id/).

## Tugas 2

1.  - [x] Membuat sebuah proyek Django baru.
      - Membuat direktori untuk menyimpan proyek Django, di kasus ini saya membuat direktori checkout-ify.
      - Buat virtual environment baru di direktori tersebut lalu aktifkan virtual environment tsb.
      - Gunakan requirements.txt untuk menyimpan dependencies yang akan di install di proyek lalu jalankan install terhadap txt file tsb.
      - Konfigurasi proyek dan coba jalankan server.
    - [x] Membuat aplikasi dengan nama main pada proyek tersebut.
      - Aktifkan environment lalu buat aplikasi main dengan menjalankan command, masukkan main kedalam installed apps.
      - Buat direktori templates untuk menyimpan file html sebagai tampilan dan struktur dasar dari web app.
    - [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
      - Dengan menambahkan kode di urls.py di tingkat proyek kita dapat menghubungkan main dengan proyek utama kita.
    - [x] Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
      - name dengan models.CharField(max_length=255) untuk menyimpan data string dengan panjang maksimal 255.
      - price dengan models.IntegerField() untuk menyimpan data Integer.
      - description models.TextField() untuk menyimpan data string yang panjang.
      - stock models.IntegerField() untuk menyimpan data Integer.
    - [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
      - Import render kedalam views.py untuk merender html dengan fungsi views.py yang kita definisikan.
      - Buat fungsi show_main yang berisikan nama aplikasi, nama, dan kelas yang nanti akan dihubungkan dengan file html.
    - [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
      - Untuk routing, buat urls.py di direktori main yang menyimpan path yang berisikan fungsi dari views.py yang ingin dihubungkan dengan tampilan main.
    - [x] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
      - Buat proyek baru di PWS dan sambungkan dengan direktori proyek dengan menggunakan remote add.
      - Push proyek lokal ke PWS agar bisa dijalankan di PWS.

2.  Client -> urls.py -> views.py -> models.py -> HTML PAGE

    - Request: Client mengirimkan permintaan HTTP/HTTP Request ke aplikasi Django.
    - Django pertama-tama memeriksa urls.py untuk menemukan view mana yang seharusnya menangani permintaan tersebut.
    - Setelah urls.py memetakan URL ke view yang sesuai, fungsi view ini dipanggil. View ini biasanya mengolah data dari models.py.
    - Ketika view membutuhkan data dari database, view akan berinteraksi dengan model dan mengambil data yang dibutuhkan.
    - Response : Setelah data diolah di views.py, data tersebut dikirim ke template untuk dirender menjadi halaman HTML yang dikirim ke klien sebagai respons.

3.  Git adalah alat manajemen versi (version control system) yang sangat penting dalam pengembangan perangkat lunak, dengan git kita dapat menyimpan semua perubahan yang terjadi terhadap proyek kita dan melakukan rollback apabila ingin kembali ke versi lama dari program teresbut, dengan git kita juga dapat mengerjakan proyek secara kolaboratif dengan mudah.

4.  Django adalah framework yang sangat cocok untuk pemula karena memberikan keseimbangan antara kemudahan penggunaan dan kekuatan fungsional. dokumentasi yang banyak, keamanan , dan skalabilitas yang baik menjadikan Django sebagai framework yang bagus untuk memulai pembelajaran pengembangan perangkat lunak, khususnya di bidang pengembangan web.

5.  Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan model sebagai cara untuk menghubungkan kode Python dengan tabel-tabel dalam database relasional.

## Tugas 3

1. Data delivery digunakan untuk pengiriman data dari suatu komponen ke komponen lain dalam sebuah platform. Dengan adanya data delivery yang efisien dan andal, berbagai komponen dalam platform dapat berkomunikasi secara lancar, dan informasi yang dibutuhkan selalu tersedia tepat waktu dan dalam kondisi yang benar.

2. Menurut saya, JSON lebih baik daripada XML karena readabilitynya yang lebih mudah dibaca dan penggunaan object dalam JSON yang saya sudah lebih familiar dalam penggunaanya. Secara umum JSON lebih populer dibandingkan XML karena JSON dirancang untuk bekerja dengan JavaScript

3. Method isvalid() digunakan untuk memberikan validasi input kepada form sesuai dengan data model yang telah kita buat, metode is_valid() akan memeriksa tipe data yang dimasukkan pengguna. Jika ada field yang mengharuskan tipe data tertentu, seperti integer, maka is_valid() akan memvalidasi bahwa input tersebut sesuai dengan tipe data yang ditentukan. Jika tidak, form tidak akan dianggap valid, dan submisi tidak akan terjadi.

4. csrf_token digunakan untuk melindungi sebuah proyek django dari serangan csrf atau cross site request forgery, serangan ini dapat dicegah dengen menggunakan csrf_token adalah sebuah nilai acak yang dihasilkan oleh server dan akan ada dalam setiap form yang diisi oleh pengguna. Ketika form dikirimkan, server akan memeriksa apakah csrf_token yang diterima sesuai dengan yang diharapkan, jika tidak server akan menolak request tsb.

5.  - [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.
      - Buat berkas baru bernama forms.py di dalam direktori main.
      - Import ModelForm dari django.forms dan Attribute dari model di main/models.py.
      - Pilih field yang ingin ditampilkan di form.
      - Membuat View untuk Menangani Form
      - Buat fungsi add_product yang menangani request form dari user.
      - Jika form valid, simpan data menggunakan form.save() dan redirect ke halaman utama setelah penyimpanan.
      - Return context berisi form untuk dirender ke template add_product.html.
      - Modifikasi fungsi show_main untuk mengambil semua data dari model Attribute.
      - Pass data attribute_entries ke template main.html.
      - Tambahkan URL di urls.py path baru dalam urlpatterns yang mengarahkan ke view add_product.
      - Buat form HTML yang menggunakan POST method.
      - Tambahkan csrf_token untuk keamanan.


    - [x] Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
        - Terdapat 4 fungsi view yang ditambahkan kedalam views.py yang masing2 digunakan untuk menampilkan data yang sudah ditambahkan ke model Attribute
            - show_xml
            - show_json
            - show_xml_by_id
            - show_json_by_id
        
    Semua fungsi yang ada di views.py ini mengambil semua objek Attribute dari database dan mengubahnya menjadi format xml, json, xml dengan id spesifik, dan json dengan id spesifik, kemudian mengirimkannya sebagai HTTP response.

    - [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
        - Untuk mengakses fungsi yang ada di views yang telah dibuat di projek django, kita harus menambahkan rute (URL patterns) di dalam urls.py. 
        - Hal pertama yang dilakukan adalah mengimport fungsi dari views.py kedalam file urls.py
        - Tambahkan path url fungsi kedalam urlpatterns untuk mengakses fungsi yang sudah diimpor

Screenshots
- XML Data Postman
![xml](assets/xml.png)
- JSON Data Postman
![json](assets/json.png)
- XML Data with ID Postman
![xml id](assets/xml_id.png)
- JSON Data with ID Postman
![json id](assets/json_id.png)

## Tugas 4
1.  - HttpResponseRedirect()
      - Hanya dapat menerima 1 argumen berupa url
      - Secara eksplisit mengirimkan respons pengalihan HTTP 302 ke URL yang ditentukan.
    - redirect()
      - Dapat menerima lebih dari 1 argumen seperti model, view, atau url
      - Mereturn HttpResponseRedirect ke url yang ditentukan dalam argumennya secara otomatis

2.  - Relasi ForeignKey : Pada berkas models.py, model Product dihubungkan dengan User menggunakan ForeignKey untuk memastikan bahwa setiap produk terkait dengan pengguna tertentu. 
    - Mengaitkan Produk dengan Pengguna Terlogin : Saat pengguna membuat produk baru, kita perlu memastikan bahwa produk tersebut dihubungkan dengan pengguna yang sedang login, karena itu kita harus melakukan modifikasi pada views.py di fungsi untuk menambahkan product atau add_product product.user = request.user: Menghubungkan produk dengan pengguna yang sedang login
    - Menampilkan Produk yang Dimiliki oleh Pengguna : Setelah produk yang dimiliki pengguna telah di save, selanjutnya aplikasi harus menampilkan hanya produk yang dimiliki oleh pengguna yang sedang login.
3.  - Authentication : 
      - Proses memverifikasi identitas pengguna. Sistem mengecek apakah pengguna yang mencoba login adalah pengguna yang terdaftar.
      - Menentukan siapa pengguna tersebut (misalnya, dengan memeriksa username dan password).
      - Dilakukan saat pengguna login untuk memverifikasi kredensial.
    - Authorization : 
      - Proses menentukan apa yang diizinkan untuk dilakukan oleh pengguna.
      - Menentukan apa yang dapat dilakukan pengguna (misalnya, apakah mereka dapat mengakses halaman admin atau mengedit data).
      - Dilakukan setelah login untuk membatasi akses ke halaman atau tindakan tertentu.

    Django mengimplementasikan authentication dan authorization melalui library yang dimiliki django, yaitu django.contrib.auth.
    Otentikasi di Django adalah proses memverifikasi identitas pengguna, biasanya melalui username dan password. Django menyediakan mekanisme otentikasi bawaan yang menangani banyak aspek seperti login, logout, dan sesi pengguna.
    Otorisasi di Django adalah proses menentukan hak akses pengguna setelah mereka berhasil login. Django memiliki sistem izin  yang dapat membatasi akses pengguna, seperti membatasi sebuah halaman hanya setelah user telah berhasil login.

4.  Django mengingat pengguna yang telah login dengan menggunakan cookies dan session.
    - Saat pengguna berhasil login, Django menyimpan status login dalam sesi. Django menciptakan sebuah sesi di server, dan setiap sesi memiliki ID unik yang mengidentifikasi sesi tersebut.
    - Setelah sesi dibuat, Django mengirimkan cookie sesi ke browser pengguna, Cookie ini disimpan di browser pengguna dan dikirim kembali ke server pada setiap permintaan HTTP yang dibuat pengguna.
    - Django menyimpan detail otentikasi pengguna dalam sesi dan menautkannya ke cookie sesi yang dikirim ke browser pengguna. Setiap kali pengguna mengakses situs, cookie sesi ini dikirimkan kembali ke server. Django menggunakan ID sesi dari cookie tersebut untuk mengambil informasi terkait pengguna yang sedang login dari database atau penyimpanan sesi.

    Tidak semua cookies aman digunakan. Keamanan cookies tergantung pada cara mereka digunakan dan data yang disimpan, bisa saja terjadi serangan dimana penyerang mencuri cookie sesi pengguna, penyerang dapat menyamar sebagai pengguna tanpa perlu mengetahui username atau password pengguna, untuk menghindari ini maka diperlukan HTTPS untuk mengenkripsi cookies.

5.  - [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
      - Registrasi :
        - Dengan menggunakan UserCreationForm dari django, kita dapat mempermudah pembuatan form registrasi.
        - Membuat fungsi register di views.py dimana kita memanggil fungsi UserCreationForm untuk membuat form registrasi kita.
        - Setelah fungsi kita dibuat, kita harus membuat html file berupa register.html yang akan menyimpan halaman register kita.
        - Menambahkan path url ke ursl.py untuk melakukan redirect ke /register apabila user mengklik tombol di halaman login registrasi.
      - Login :
        - Dengan menggunakan AuthenticationForm dari django, kita dapat mempermudah membuat fungsi yang bekerja untuk autentikasi login.
        - Membuat fungsi login_user di views.py dimana apabila input dari user itu valid, maka akan memanggil fungsi login untuk melakukan pengecekan username dan password dari user dan akan membuat session baru untuk logged in user.
        - Setelah fungsi kita dibuat, kita harus membuat html file berupa login.html yang akan menyimpan halaman login kita.
        - Menambahkan path url ke ursl.py untuk melakukan redirect ke /login apabila user pertama kali membuka halaman web dengan melakukan restriksi terhadap halaman halaman lain.
      - Logout :
        - Membuat fungsi logout dimana kita akan melakukan logout request ke server agar user yang sedang logged in bisa dihapus sesinya.
        - Membuat tombol logout agar pengguna dapat logout dari program di halaman utama.
        - Menambahkan path url ke ursl.py agar pengguna dapat redirect ke logout.
    - [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
      - Melakukan registrasi dengan isian yang sesuai dengan field form yang telah kita buat.
      - Melakukan login sesuai dengan data yang telah kita registrasikan setelah berhasil registrasi dan membuat 3 data product menggunakan form add_product sebagai bentuk dummy data yang dibutuhkan.
    - [x] Menghubungkan model Product dengan User.
      - Penghubungan models kita yaitu pada kasus saya sebuah class Attribute ke User menggunakan relasi ForeignKey dimana setiap entry model dihubungkan ke satu user, Pada Attribute di models.py, kita tambahkan user = models.ForeignKey(User) menunjukkan hubungan many-to-one. Artinya, setiap objek Product hanya dapat terhubung dengan satu objek User dan syntax on_delete=models.CASCADE di argumen ke 2 menunjukkan bahwa apabila user tsb di delete, maka setiap data yang terkait dengan user tersebut juga akan di delete dari database.
      - Setelah relasi antara Product dan User dibuat, kita perlu memastikan bahwa setiap entri yang dibuat dihubungkan dengan pengguna yang sedang login, karena itu kita harus melakukan modifikasi pada views.py di fungsi untuk menambahkan product atau pada kasus saya add_product product.user = request.user: Menghubungkan produk dengan pengguna yang sedang login
      - Setelah produk yang dimiliki pengguna telah di save, selanjutnya aplikasi harus menampilkan hanya produk yang dimiliki oleh pengguna yang sedang login, dengan Product.objects.filter(user=request.user), query ini memastikan bahwa hanya produk yang dimiliki oleh pengguna yang sedang login yang akan ditampilkan.
      
    - [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
      - Tampilan informasi pengguna yang sedang logged in seperti username dapat dilakukan dengan memodifikasi show_main dengan 'name': request.user.username, dimana apabila user telah berhasil login kita akan melakukan request terhadap username dari user yang sedang login dan mengirim context ini kepada file html dimana halaman main ditampilkan.
      - Untuk menerapkan cookies terhadap projek django kita, dimana data yang akan disimpan adalah last_login, pada saat user login, kita perlu menambahkan response.set_cookie('last_login', str(datetime.datetime.now())) yang akan menyimpan cookies berupa datetime dimana last_login itu terjadi.
      - Untuk dapat melakukan request terhadap data last_login yang disimpan di cookies kita akan menambahkan kode 'last_login': request.COOKIES['last_login'] di show_main kita yang disimpan di context atau dictionary sehingga kita dapat pass ke file html kita sehingga dapat menampilkan last_login dari user.
      - Apabila user telah logout maka kita perlu menghapus cookie last_loginnya dengan menambahkan response.delete_cookie('last_login') di fungsi logout_user.

## Tugas 5
1.
2. Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena dengan adanya responsive design, user dapat mengakses aplikasi web kita dengan berbagai macam perangkat yang user miliki. Dengan perkembangan teknologi di dunia, jumlah perangkat yang memiliki ukuran layar dan resolusi yang berbeda juga semakin banyak, hal ini akan menyebabkan web kita tidak tertampilkan sesuai dengan keinginan kita di perangkat perangkat tertentu, dengan menerapkan konsep responsive design, web kita akan ditampilkan di semua perangkat dengan rapih dan sesuai dengan design yang telah kita buat. 
Contoh Web Responsive : 
  - Twitter
  - Google
Contoh Web Tidak Responsive : 
  - Web Lama 
  - Web Bisnis Lokal Kecil
3. Margin, border, dan padding merupakan konsep yang penting dalam melakukan styling dengan css, ketiga komponen ini merupakan bagian dari box model pada css setelah content, sebagai bentuk visual silahkan liat gambar dibawah ini :
  - CSS BOX MODEL
  ![box_model](assets/box_model.png)
  - Margin : Margin adalah ruang kosong di luar border elemen, yang memisahkan elemen tersebut dari elemen lainnya di halaman. 
    - Implementasi : 
      .element {
        margin: 20px; Memberikan margin seragam di semua sisi 
        margin-top: 20px; Memberikan margin bagian atas elemen
        margin-right: 20px; Memberikan margin bagian kanan elemen
        margin-bottom: 20px; Memberikan margin bagian bawah elemen
        margin-left: 20px; Memberikan margin bagian kiri elemen
      }
  - Border : Border adalah garis yang mengelilingi konten elemen, termasuk padding tetapi di luar konten elemen itu sendiri.
    - Implementasi : 
      .element {
          border: 2px solid black;  Border hitam tebal 2px di semua sisi 
          border-top: 2px dashed red;  Border atas bergaya dashed merah 2px 
          border-bottom: 2px dotted green; Border bawah dengan garis titik-titik hijau 2px 
      }
  - Padding : Padding adalah ruang antara konten elemen dan border elemen tersebut. Padding berada di dalam border, dan memberikan jarak antara isi elemen dengan tepi dalam elemen.
    - Implementasi : 
      .element {
        padding: 10px; Padding seragam di semua sisi 
        padding-top: 10px; Padding atas 10px 
        padding-right: 10px; Padding kanan 10px
        padding-bottom: 10px; Padding bawah 10px 
        padding-left: 10px; Padding kiri 10px 
      }


4. Flexbox dan Grid Layout adalah dua metode tata letak di CSS yang sangat berguna untuk membuat tata letak yang responsif dan fleksibel di halaman web.
  - Flexbox : Flexbox adalah sistem tata letak yang memudahkan pengaturan item-item dalam sebuah kontainer. Flexbox berfokus pada distribusi ruang di antara items di dalam flexbox itu sendiri.
    - Kegunaan : 
      Dengan Flexbox, kita dapat membuat styling yang lebih responsif, dengan jarak yang telah didefinisikan oleh flexbox contohnya space-between, space-around dll, dan dengan arah yang kita tentukan contohnya flex-direction:row/column.
  - Grid Layout : Grid Layout adalah sistem tata letak yang memungkinkan Anda untuk mengatur item dalam baris dan kolom. Dengan grid, kita dapat membuat desain yang lebih kompleks, di mana elemen-elemen bisa ditempatkan dalam area grid yang kita definisikan.
    - Kegunaan : 
      Grid layout sangat bermanfaat untuk membuat tata letak yang lebih rumit, di mana elemen-elemen harus ditempatkan dengan posisi dan size yang spesifik dalam baris dan kolom.

5.










