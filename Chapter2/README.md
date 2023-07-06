# Membuat Form Sign Up untuk POST ke pipedream.com ketika klik button
* Membuat Akun pipedream.com
* Membuat New HTTP / WEBHOOK Request

![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/1bc88d0d-6e18-48bc-9d78-f076f80d3abf)

* Pilih Event Data : Raw Request, HTTP Response : 200 OK . Kemudian klik Save and Continue

![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/33cc51f6-edfd-45d5-836e-2ea4b3db852f)

* Akan keluar unique URL untuk endpoint : https://eornxvetq6guwch.m.pipedream.net . Kemudian coba dengan postman

![1](https://github.com/kerjabhakti/SisterAryo/assets/56922640/8e6d7c8d-18c3-449a-9e1f-6f627dec27a2)

### Melakukan Testing Endpoint
Buka Postman untuk melakukan testing endpoint dengan contoh :
* Method POST Headers isi dengan Key : Login , Value : Bebas. Pada bagian body isi dengan data json .Kemudian klik Send

![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/e6af0a8c-0225-43e4-92a8-34dcf9247208)

![2](https://github.com/kerjabhakti/SisterAryo/assets/56922640/0ce79d87-d3cc-424d-b5be-44d0d46a65e1)

* Dashboard Pipedream akan muncul 1 New Event, kita buka event tersebut.

![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/b6964d0e-3b4f-4fed-b87e-ff6de15fe15c)

![3](https://github.com/kerjabhakti/SisterAryo/assets/56922640/ee70599a-eada-4384-a2f2-394cb7372f7a)

* Disana akan terlihat pada bagian headers ada Login yang kita masukkan dan pada bagian body ada json yang kita masukkan ke postman.
  Artinya endpoint dan http request bekerja dengan baik untuk menangkap header dan body yang dikirimkan.

![4](https://github.com/kerjabhakti/SisterAryo/assets/56922640/8d228237-5a42-4423-a4c0-2346535a79a5)

* Simpan kode javascript yang dibuat oleh postman dengan menekan tanda </> dibagian pojok kanan atas, kemudian pilih javascipt - Fetch

![5](https://github.com/kerjabhakti/SisterAryo/assets/56922640/a943d04a-a0fc-4688-9de5-04844d60888b)

![6](https://github.com/kerjabhakti/SisterAryo/assets/56922640/d8b82561-f85f-4453-86b0-9d9dfd28085b)

### Membuat Form Pendaftaran

* Cari dulu di google dengan keyword sign up form tailwind component free. Contoh : https://tailwindcomponents.com/component/simple-registersign-up-form/landing

![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/dc84ccc4-3e86-4a51-ae99-cd83bb997b9b)

* Unduh kodenya untuk di pakai ditaruh di repo dan coba live server dari vscode.

![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/d38edabc-d903-4196-bce2-c2e18ffd581d)

* Cari element dari input dan buttonnya kemudian kita beri id

![7](https://github.com/kerjabhakti/SisterAryo/assets/56922640/1f466f7b-9778-4f27-a40b-5eef848a25ef)

* Buat file js kita masukkan dahulu javascript yang didapatkan dari postman ke js tersebut, kemudian panggil pada bagian bawah sebelum tag penutup body

![8](https://github.com/kerjabhakti/SisterAryo/assets/56922640/7f3907b8-1e37-4171-b60f-830a5e4d53dd)

### Membuat Fungsi Javascript

Pada bagian ini akan membuat fungsi-fungsi di javascript untuk mengirimkan data dari html menuju endpoint pipedream yang sudah di buat. Harus dibuat fungsi agar kode program javascript tetap rapih dan mudah terbaca

1. Membuat fungsi PostSignUp() yang berfungsi untuk melakukan Post Form Data Sign Up. Fungsi ini diambil dari postman, yang kita modif data inputan dari id form html.
  
   ![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/8cbb4e82-3e6d-4903-a698-4cd74d5b3884)

2. Membuat fungsi PushButton() untuk melakukan aksi setelah menekan tombol, pada bagian html button tambahkan atribut onclick.

   ![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/99035e1b-209c-45f1-8667-c1c1e3b188dc)
   ![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/ce8aff82-a11d-4a8c-88c1-8ec51a8cdb5d)

3. Test dengan klik kanan Open with live server, isi form nya sambil inspect console lalu klik button yang kita buat. Terlihat dari console data success dikirim. kemudian lihat pada dashboard pipedream data sudah diterima dengan baik oleh endpoint baik itu header maupun body.
   ![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/c0523c09-352d-48fd-82fa-049dcb2d143f)
  
   ![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/b68ca948-91f9-4337-a674-c259977b1291)

