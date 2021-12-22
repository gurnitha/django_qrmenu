### MEMBUAT APLIKASI QRMenu Menggunakan React dan Django


#### DAY:1 - 22/12/21


#### 1. Apa yang akan kita buat?

        Kita akan membuat aplikasi QRMenu.
        Aplikasi ini adalah salah satu solusi
        di masa pandemi Covid-19.

        Restauran, Cafe dan usaha sejenis di masa normal,
        biasanya mencetak menu untuk para pelanggannya.

        Namun dengan QRMenu, mereka tidak perlu lagi mencetak
        menu secara manual, tetapi mereka bisa membuat
        menu secara digital.


#### 2. Project Structure - DONE

        Proyek ini akan terdiri dari dua bagian utama, yakni:

        1. Frontend menggunakan React.
        2. Backend menggunkan Django Framework.


#### 3. Setting Up

        1. Menginstal Python versi 3.9
        2. Menginstal Git
        3. Menginstal Text Editor (Visual Studio Code)
        4. Menginstal browser Google Chrome
        5. Menginstal JSONView extensions


#### 4. Inisialisasi proyek

        Steps:

        1. Membuat root folder 'QRMenu'
        2. Masuk ke QRMenu folder
        3. Membuat dua buah file:
           - .gitignore
           - README.md
        4. Memastikan versi python dan pip 
        5. Membuat virtual environment 'venvqr3932'
        6. Mengaktifkan venvqr3932
        7. Menginstall django 3.2
        8. Mengupdate pip
        9. Membuat django proyek dengan nama 'qrmenu_backend'
        10. cd qrmenu_backend
        11. Jalan server untuk menguji 
        12. Copy http://127.0.0.1:8000
        13. Buka browser dan paste code itu + enter
        14. Membuat repositori local

        DONE:)

        new file:   .gitignore
        new file:   README.md
        new file:   manage.py
        new file:   qrmenu_backend/__init__.py
        new file:   qrmenu_backend/asgi.py
        new file:   qrmenu_backend/settings.py
        new file:   qrmenu_backend/urls.py
        new file:   qrmenu_backend/wsgi.py


#### 5. Django Admin Dashboard

        Steps:

        1. Jalankan perintah migrasi untuk membuat tabel-tabel default
        2. Membuat superuser
        3. Jalankan server
        4. Login ke admin dashboard

        modified:   README.md


#### 6.1 Django App


        Steps:

        1. Membuat django app dgn nama 'core'
        2. Install/registrasikan django app 'core' pada proyek (settings.py)
        3. Jalankan server untuk menguji hasilnya

        modified:   README.md
        new file:   core/__init__.py
        new file:   core/admin.py
        new file:   core/apps.py
        new file:   core/migrations/__init__.py
        new file:   core/models.py
        new file:   core/tests.py
        new file:   core/views.py
        modified:   qrmenu_backend/settings.py


#### 6.2 Install djoser


        Steps:

        1. Instal djoser
           > pip install djoser==2.1.0
        2. Register djoser pada settings.py
        3. Configure rest_framework pada settings.py
        4. Buat path untuk djoser pada qrmenu_backend/urls.py
        5. Jalan migrasi
        6. Jalankan server untuk menguji hasilnya

        modified:   README.md
        modified:   qrmenu_backend/settings.py
        modified:   qrmenu_backend/urls.py