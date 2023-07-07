# Studi Kasus Tiket ColdPlay

![1](https://github.com/kerjabhakti/SisterAryo/assets/56922640/fb529493-8678-4cfb-be15-a68301332a9a)

![2](https://github.com/kerjabhakti/SisterAryo/assets/56922640/5dfa8429-9632-4623-95d4-1f6a52743399)

Dalam program ini, proses dengan rank 0 bertindak sebagai koordinator dan proses-proses lainnya bertindak sebagai agen penjualan tiket. Setiap agen menerima agent_id dari proses koordinator melalui comm.recv(), menjual tiket Coldplay dengan memanggil fungsi sell_tickets(), dan mengirim laporan penjualan kepada proses koordinator melalui comm.send(). Proses koordinator bertanggung jawab untuk membagikan tugas penjualan tiket kepada agen-agen dan mengumpulkan laporan penjualan dari mereka. kita dapat menjalankan program ini menggunakan MPI dengan menjalankan perintah mpiexec -n <jumlah_proses> python coldplay_ticket.py, di mana <jumlah_proses> adalah jumlah proses yang ingin digunakan untuk menjalankan program tersebut.


