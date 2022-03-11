- [EN description](#en)  
- [TR açıklama](#tr)
- [Paper(Bildiri)](https://www.fatiiates.com/doc/notice_optimization.pdf)

# Particle Swarm Optimization(Parçacık Sürü Optimizasyonu, PSO)

# [EN]

## What is the Particle Swarm Optimization ?

&emsp;&emsp;This is a meta-heuristic algorithm based on population. Developed by Kennedy and Eberhart in 1995, inspired by the movements of flocks of birds and fish. Each candidate solution is expressed as a particle, and the population is expressed as a flock. Each candidate solution (particle) adjusts its next position according to the velocity vector, its best location (local best) and the best location of the flock (global best). And each swarm member has a speed that determines its movement in the search space and can vary according to conditions. PSO rarely deviates to local optimum points. When a sufficient number of particles are produced the probability is very low.

## How PSO works ? 

&emsp;&emsp;PSO initially creates a flock. Assigns random local values ​​to this flock, assigns locations, and determines a global value and global location within the entire flock. Then it starts to iterate for the desired number. New locations and new fitness values ​​are calculated for each particle at each iteration. If the calculated values ​​are better than the old values ​​of the particle, they replace the local variables of the particle with the new values. At the same time, if these new values ​​are better than the global values ​​of the whole flock, new values ​​are assigned to global values. When the iterations are over, the global location and global fitness value are our global minimum points.

Pseudo Code of Algorithm

- Step 1: Randomly assign the starting positions (xi) and their velocities (vi) in the search space of the particles between specified limits.
- Step 2: At the beginning, the best location of the whole flock is determined with the fitness values ​​and local best positions of the particles.
- Step 3: Iteration is initiated and a new location and the corresponding fitness value are generated for each particle, If the new fitness value is better than the particle's local fitness value, the local best location and the local fitness value are updated with the new values ​​generated.
- Step 4: If the new local fitness value of the particle is better than the global best fit value, the location of that particle and the fit value of the particle are updated as the global best location and global fit value.
- Step 5: The velocities and positions of the particles are updated.
- Step 6: The process is repeated from the third step until the number of iterations is completed.
- Step 7: Global best position achieved at the end of evolution is the solution to the function.


### Results
 
 &emsp;&emsp;The PSO algorithm has been tested on four different metaphor-based functions and the results are as follows. The following parameters are used for the 'particleSwarmOptimization' function in all tests.

- functionToOptimize = [RELATED_FUNCTION]
- lowerBoundary = [RELATED_FUNCTION_LOWER_BOUNDARIES(X,Y)]
- upperBoundary = [RELATED_FUNCTION_UPPER_BOUNDARIES(X,Y)]
- particleSize=100
- c1=0.5
- c2=0.5
- numberOfIterations=50


 #### Ackley Function
 
- Function: ![\Large x=f(x,%20y)={-20exp[-0.2\sqrt{0.5(x^2%20+%20y^2)}]-exp[0.5(cos2{\pi}x%20+%20cos2{\pi}y)]%20+%20e%20+%20{20}}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={-20exp[-0.2\sqrt{0.5(x^2%20+%20y^2)}]-exp[0.5(cos2{\pi}x%20+%20cos2{\pi}y)]%20+%20e%20+%20{20}}) 
- Global minimum: ![\Large x=f(0,%200)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(0,%200)={0})
- Search domain: ![\Large x=-5%20\leq%20x,y%20\leq%205](https://latex.codecogs.com/svg.latex?\Large&space;-5%20\leq%20x,y%20\leq%205)

The obtained values

- For the best solution, x and y: [5.204778213273946e-08, 2.2603977383842164e-07]
- The result for best x and y: 6.560682024314701e-07
- Graphs obtained as a result of 50 iterations;

![pso_ackley](https://user-images.githubusercontent.com/51250249/108910026-56b5d200-7636-11eb-8211-89699a607a0c.png)

 #### Beale Function

- Function: ![\Large x=f(x,%20y)={(1.5%20-%20x%20+%20xy)^2%20+%20(2.25%20-%20x%20+%20xy^2)^2%20+%20(2.625%20-%20x%20+%20xy^3)^2}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={(1.5%20-%20x%20+%20xy)^2%20+%20(2.25%20-%20x%20+%20xy^2)^2%20+%20(2.625%20-%20x%20+%20xy^3)^2}) 
- Global minimum: ![\Large x=f(3,%200.5)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(3,%20{0.5})={0})
- Search domain: ![\Large x=-4.5%20\leq%20x,y%20\leq%204.5](https://latex.codecogs.com/svg.latex?\Large&space;-4.5%20\leq%20x,y%20\leq%204.5)

The obtained values

- For the best solution, x and y: [2.9999945858667654, 0.4999983690893992]
- The result for best x and y: 6.609783593788841e-12
- Graphs obtained as a result of 50 iterations;

![PSO_BEALE](https://user-images.githubusercontent.com/51250249/108909942-4140a800-7636-11eb-86c7-3d44e73895dd.png)

 #### Goldstein-Price Function

- Function: ![\Large x=f(x,%20y)={[1%20+%20(x%20+%20y%20+%201)^2(19%20-%2014x%20+%203x^2%20-%2014y%20+%206xy%20+%203y^2)][30%20+%20(2x%20-%203y)^2(18%20-%2032x%20+%2012x^2%20+%2048y%20-%2036xy%20+%2027y^2)]}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={[1%20+%20(x%20+%20y%20+%201)^2(19%20-%2014x%20+%203x^2%20-%2014y%20+%206xy%20+%203y^2)][30%20+%20(2x%20-%203y)^2(18%20-%2032x%20+%2012x^2%20+%2048y%20-%2036xy%20+%2027y^2)]}) 
- Global minimum: ![\Large x=f(0,%20-1)={3}](https://latex.codecogs.com/svg.latex?\Large&space;f(0,%20-1)={3})
- Search domain: ![\Large x=-2%20\leq%20x,y%20\leq%202](https://latex.codecogs.com/svg.latex?\Large&space;-2%20\leq%20x,y%20\leq%202)

The obtained values

- For the best solution, x and y: [4.9403912363405115e-08, -0.9999999957834693]
- The result for best x and y: 3.0000000000005698
- Graphs obtained as a result of 50 iterations;

![pso_gsp](https://user-images.githubusercontent.com/51250249/108909945-41d93e80-7636-11eb-83b4-e13a5e824014.png)


 #### Lévi Function

- Function: ![\Large x=f(x,%20y)={sin^23{\pi}x%20+%20(x%20-%201)^2(1%20+%20sin^23{\pi}y)%20+%20(y%20-%201)^2(1%20+%20sin^22{\pi}y)}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={sin^23{\pi}x%20+%20(x%20-%201)^2(1%20+%20sin^23{\pi}y)%20+%20(y%20-%201)^2(1%20+%20sin^22{\pi}y)}) 
- Global minimum: ![\Large x=f(1,%201)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(1,%201)={0})
- Search domain: ![\Large x=-10%20\leq%20x,y%20\leq%2010](https://latex.codecogs.com/svg.latex?\Large&space;-10%20\leq%20x,y%20\leq%2010)

The obtained values

- For the best solution, x and y: [1.0000000551840271, 0.9999999103089193]
- The result for best x and y: 2.815908666126024e-13
- Graphs obtained as a result of 50 iterations;

![pso_levi](https://user-images.githubusercontent.com/51250249/108909946-4271d500-7636-11eb-9c91-a92f9963b013.png)

# [TR]

## Parçacık Sürü Optimizasyonu Nedir ?

&emsp;&emsp;Temelinde popülasyon olan meta-sezgisel bir algoritmadır. Kuş ve balık sürülerinin hareketlerinden esinlenerek 1995’te Kennedy ve Eberhart tarafından geliştirilmiştir. Her bir aday çözüm parçacıkla (particle), popülasyon ise sürü ile ifade edilir. Her bir aday çözüm (particle) bir sonraki pozisyonunu, hız (velocity) vektörü, kendi en iyi lokasyonu (yerel en iyi) ve sürünün en iyi lokasyonuna (küresel en iyi) göre ayarlar. Bununla birlikte her sürü üyesinin arama uzayındaki hareketini belirleyen ve şartlara göre değişebilen bir hızı mevcuttur. PSO, çok nadir olarak yerel optimum noktalara takılır. Yeterli sayıda parçacık üretildiğinde ihtimal çok düşüktür.
  
## Parçacık Sürü Optimizasyonu Nasıl Çalışır ? 

&emsp;&emsp;PSO, başlangıçta bir sürü belirler. Bu sürüye rastgele lokal değerler atar, lokasyonlar atar ve tüm sürü içinde bir global değer ve global lokasyon belirler. Daha sonra istenen sayı kadar iterasyona başlanır. Her iterasyonda her parçacık için yeni lokasyonlar ve yeni objektif değerler hesaplanır. Hesaplanan değerler parçacığın eski değerlerinden daha iyiyse yeni değerler parçacığın yerel değişkenleri olarak değiştirirler. Aynı zamanda bu yeni değerler tüm sürünün global değerlerinden de iyiyse global değerlere de yeni değerler atanır. İterasyonlar sonlandığında global lokasyon ve global objektif değer bizim global minimum noktalarımızdır.

Algoritma Sözde Kodu

- Adım 1: Rastgele olarak parçacıkların arama uzayındaki başlangıç konumları (xi) ve hızları (vi), belirlenen sınırlar arasında atanır.
- Adım 2: Başlangıçta parçacıkların uygunluk değerleri ve yerel en iyi konumları ile tüm sürünün en iyi konumu belirlenir.
- Adım 3: İterasyona başlanır ve her parçacık için yeni lokasyon ve buna bağlı olarak uygunluk değeri üretilir, yeni uygunluk değeri parçacığın kendi yerel uygunluk değerinden daha iyi ise yerel en iyi konumu ve yerel uygunluk değeri üretilmiş olan yeni değerlerle güncellenir.
- Adım 4: Parçacığın yeni yerel uygunluk değeri, küresel en iyi uygunluk değerinden daha iyi ise o parçacığın konumu ve parçacığın uygunluk değeri, küresel en iyi lokasyon ve küresel uygunluk değeri olarak da güncellenir.
- Adım 5: Parçacıkların hız ve konumları güncellenir.
- Adım 6: Süreç, iterasyon sayısı tamamlanıncaya kadar üçüncü adımdan itibaren tekrarlanır.
- Adım 7: Evrim sonunda elde edilen global en iyi konum, problemin çözümüdür.


### Sonuçlar

&emsp;&emsp;PSO algoritması metafor bazlı dört farklı fonksiyon üzerinde test edilmiş ve sonuçları aşağıdaki gibidir. Tüm testlerde 'particleSwarmOptimization' fonksiyonu için aşağıdaki parametreler kullanılmıştır.

- functionToOptimize = [İLGİLİ_FONKSİYON]
- lowerBoundary = [İLGİLİ_FONKSİYON_ALT_SINIRLAR(X,Y)]
- upperBoundary = [İLGİLİ_FONKSİYON_ÜST_SINIRLAR(X,Y)]
- particleSize=100
- c1=0.5
- c2=0.5
- numberOfIterations=50

 #### Ackley Fonksiyonu
 
- Fonksiyon: ![\Large x=f(x,%20y)={-20exp[-0.2\sqrt{0.5(x^2%20+%20y^2)}]-exp[0.5(cos2{\pi}x%20+%20cos2{\pi}y)]%20+%20e%20+%20{20}}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={-20exp[-0.2\sqrt{0.5(x^2%20+%20y^2)}]-exp[0.5(cos2{\pi}x%20+%20cos2{\pi}y)]%20+%20e%20+%20{20}}) 
- Global minimum: ![\Large x=f(0,%200)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(0,%200)={0})
- Değer aralığı: ![\Large x=-5%20\leq%20x,y%20\leq%205](https://latex.codecogs.com/svg.latex?\Large&space;-5%20\leq%20x,y%20\leq%205)

Elde edilen değerler

- En iyi çözüm için x ve y: [5.204778213273946e-08, 2.2603977383842164e-07]
- En iyi x ve y için sonuç: 6.560682024314701e-07
- 50 iterasyon sonucunda elde edilen grafikler;

![pso_ackley](https://user-images.githubusercontent.com/51250249/108910026-56b5d200-7636-11eb-8211-89699a607a0c.png)

 #### Beale Fonksiyonu

- Fonksiyon: ![\Large x=f(x,%20y)={(1.5%20-%20x%20+%20xy)^2%20+%20(2.25%20-%20x%20+%20xy^2)^2%20+%20(2.625%20-%20x%20+%20xy^3)^2}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={(1.5%20-%20x%20+%20xy)^2%20+%20(2.25%20-%20x%20+%20xy^2)^2%20+%20(2.625%20-%20x%20+%20xy^3)^2}) 
- Global minimum: ![\Large x=f(3,%200.5)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(3,%20{0.5})={0})
- Değer aralığı: ![\Large x=-4.5%20\leq%20x,y%20\leq%204.5](https://latex.codecogs.com/svg.latex?\Large&space;-4.5%20\leq%20x,y%20\leq%204.5)

Elde edilen değerler

- En iyi çözüm için x ve y: [2.9999945858667654, 0.4999983690893992]
- En iyi x ve y için sonuç: 6.609783593788841e-12
- 50 iterasyon sonucunda elde edilen grafikler;

![PSO_BEALE](https://user-images.githubusercontent.com/51250249/108909942-4140a800-7636-11eb-86c7-3d44e73895dd.png)

 #### Goldstein-Price Fonksiyonu

- Fonksiyon: ![\Large x=f(x,%20y)={[1%20+%20(x%20+%20y%20+%201)^2(19%20-%2014x%20+%203x^2%20-%2014y%20+%206xy%20+%203y^2)][30%20+%20(2x%20-%203y)^2(18%20-%2032x%20+%2012x^2%20+%2048y%20-%2036xy%20+%2027y^2)]}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={[1%20+%20(x%20+%20y%20+%201)^2(19%20-%2014x%20+%203x^2%20-%2014y%20+%206xy%20+%203y^2)][30%20+%20(2x%20-%203y)^2(18%20-%2032x%20+%2012x^2%20+%2048y%20-%2036xy%20+%2027y^2)]}) 
- Global minimum: ![\Large x=f(0,%20-1)={3}](https://latex.codecogs.com/svg.latex?\Large&space;f(0,%20-1)={3})
- Değer aralığı: ![\Large x=-2%20\leq%20x,y%20\leq%202](https://latex.codecogs.com/svg.latex?\Large&space;-2%20\leq%20x,y%20\leq%202)

Elde edilen değerler

- En iyi çözüm için x ve y: [4.9403912363405115e-08, -0.9999999957834693]
- En iyi x ve y için sonuç: 3.0000000000005698
- 50 iterasyon sonucunda elde edilen grafikler;

![pso_gsp](https://user-images.githubusercontent.com/51250249/108909945-41d93e80-7636-11eb-83b4-e13a5e824014.png)


 #### Lévi Fonksiyonu

- Fonksiyon: ![\Large x=f(x,%20y)={sin^23{\pi}x%20+%20(x%20-%201)^2(1%20+%20sin^23{\pi}y)%20+%20(y%20-%201)^2(1%20+%20sin^22{\pi}y)}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={sin^23{\pi}x%20+%20(x%20-%201)^2(1%20+%20sin^23{\pi}y)%20+%20(y%20-%201)^2(1%20+%20sin^22{\pi}y)}) 
- Global minimum: ![\Large x=f(1,%201)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(1,%201)={0})
- Değer aralığı: ![\Large x=-10%20\leq%20x,y%20\leq%2010](https://latex.codecogs.com/svg.latex?\Large&space;-10%20\leq%20x,y%20\leq%2010)

Elde edilen değerler

- En iyi çözüm için x ve y: [1.0000000551840271, 0.9999999103089193]
- En iyi x ve y için sonuç: 2.815908666126024e-13
- 50 iterasyon sonucunda elde edilen grafikler;

![pso_levi](https://user-images.githubusercontent.com/51250249/108909946-4271d500-7636-11eb-9c91-a92f9963b013.png)
