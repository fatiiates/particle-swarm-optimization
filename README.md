# Parçacık Sürü Optimizasyonu

  Temelinde popülasyon olan meta-sezgisel bir algoritmadır. Kuş ve balık sürülerinin hareketlerinden esinlenerek 1995’te Kennedy ve Eberhart tarafından geliştirilmiştir. Her bir aday çözüm parçacıkla (particle), popülasyon ise sürü ile ifade edilir. Her bir aday çözüm (particle) bir sonraki pozisyonunu, hız (velocity) vektörü, kendi en iyi lokasyonu (yerel en iyi) ve sürünün en iyi lokasyonuna (küresel en iyi) göre ayarlar. Bununla birlikte her sürü üyesinin arama uzayındaki hareketini belirleyen ve şartlara göre değişebilen bir hızı mevcuttur.
  
## Algoritmada Bulunan Sabitler

- X = SxD boyutlu, parçacıkların lokasyonlarını tutan bir matris
- V = SxD boyutlu, parçacıkların hızlarını tutan bir matris
- pBest = SxD boyutlu, parçacıkların yerel en iyi konumunu tutan bir matris
- gBest = 1xD boyutlu, pBestler arasındaki en iyi lokasyonun tutulduğu bir dizi
- w = Atalet momenti
- c1,c2 = Sabit katsayılar [0.2 ve 2.0] aralığında belirlenir
- r1,r2 = Rassal olarak bulunan sayılar [0.0, 1.0) aralığındadır

## Algoritma İşlem Adımları

- Rastgele olarak parçacıkların arama uzayındaki başlangıç konumları (xi) ve hızları
(vi), belirlenen sınırlar arasında atanır.
- Başlangıçta parçacıkların uygunluk değerleri ve yerel en iyi konumları ile tüm sürünün en iyi
konumu belirlenir.
- Her parçacığın uygunluk değeri, kendi yerel en iyi konumundan daha iyi ise parçacığın konumu ve parçacığın uygunluk değeri, yerel en iyi konumu ve yerel uygunluk değeri olarak güncellenir.
- Yerel en iyi lokasyonun en iyi uygunluk değeri, küresel en iyi lokasyonun uygunluk değeri daha iyi ise o parçacığın konumu ve parçacığın uygunluk değeri, küresel en iyi lokasyon ve küresel uygunluk değeri olarak güncellenir.
- Parçacıkların hız ve konumları güncellenir.
- Süreç, iterasyon sayısı tamamlanıncaya kadar üçüncü adımdan itibaren tekrarlanır.
- Evrim sonunda elde edilen global en iyi konum, problemin çözümüdür.
