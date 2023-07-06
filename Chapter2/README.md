# Membuat Form Sign Up untuk POST ke pipedream.com ketika klik button
* Membuat Akun pipedream.com
* Membuat New HTTP / WEBHOOK Request

![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/1bc88d0d-6e18-48bc-9d78-f076f80d3abf)

* Pilih Event Data : Raw Request, HTTP Response : 200 OK . Kemudian klik Save and Continue

![image](https://github.com/kerjabhakti/SisterAryo/assets/56922640/33cc51f6-edfd-45d5-836e-2ea4b3db852f)

* Akan keluar unique URL untuk endpoint : https://eornxvetq6guwch.m.pipedream.net . Kemudian coba dengan postman

![1](https://github.com/kerjabhakti/SisterAryo/assets/56922640/8e6d7c8d-18c3-449a-9e1f-6f627dec27a2)

# Melakukan Testing Endpoint
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
