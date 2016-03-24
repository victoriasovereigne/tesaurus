# tesaurus

Tesaurus bahasa Indonesia dalam format json, diambil dari Tesaurus Bahasa Indonesia Pusat Bahasa karya Departemen Pendidikan Nasional tahun 2008. Versi online diambil dari tautan berikut: 

https://theindonesianwriters.files.wordpress.com/2011/04/kamus-tesaurus_bahasa-indonesia.pdf

File **dict.json** merupakan dump dari dictionary Python, dengan 
- key: entri kata yang ingin dicari
- value: dictionary berisi tag, sinonim, dan antonim

**Contoh:**

unik --> {'tag': 'a', 'sinonim': ['distingtif', 'eksklusif', 'idiosinkratis', 'individual', 'istimewa', 'khas', 'khusus', 'partikular', 'singularis', 'solo', 'spesial', 'spesifik', 'tersendiri', 'tunggal'], 'antonim': ['biasa']}

**Daftar tag:**
- a = adjektiva
- adv = adverbia
- ki = kiasan
- n = nomina
- num = numeralia
- p = partikel
- pron = pronomina
- v = verba

File **tesaurus.py** adalah program Python untuk memperoleh sinonim dan antonim dari suatu kata.
