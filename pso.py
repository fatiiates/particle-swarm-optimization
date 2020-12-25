from random import random
import math
import matplotlib
import matplotlib.pyplot as plt


# Verilerin grafiksel olarak ifade edilmes için kullanılan fonksiyon
def createPlot(OBJECTIVE_ARRAY, LOCATION_ARRAY):
    fig = plt.figure() # Yeni bir figür oluşturuluyor
    ax1 = fig.add_subplot(211) # Yeni bir alan oluşturuluyor row = 2, col = 1, index = 1
    ax1.plot(OBJECTIVE_ARRAY,'g.-') # Objective değerleri ax1 alanına dahil ediliyor, yeşil renk
    ax1.legend(['Objective']) # Objective grafiğine özel başlık veriliyor

    ax2 = fig.add_subplot(212) # Yeni bir alan oluşturuluyor row = 2, col = 3, index = 2
    LOCATION_X = [] # X lokasyon değerleri için başlangıç dizisi oluşturuluyor 
    LOCATION_Y = [] # Y lokasyon değerleri için başlangıç dizisi oluşturuluyor 
    for i in range(len(LOCATION_ARRAY)):
        # X lokasyon değerleri güncelleniyor
        LOCATION_X.append(LOCATION_ARRAY[i][0])
        # Y lokasyon değerleri güncelleniyor
        LOCATION_Y.append(LOCATION_ARRAY[i][1])

    # X lokasyon değerleri ax2 alanına dahil ediliyor, mavi renk
    ax2.plot(LOCATION_X, 'b.-')
    # Y lokasyon değerleri ax2 alanına dahil ediliyor, kırmızı renk
    ax2.plot(LOCATION_Y, 'r--')
    # X ve Y grafiklerine özel başlık veriliyor
    ax2.legend(['x','y'])

    # Alanlar ekrana çizdiriliyor
    plt.show()

def particleSwarmOptimization(functionToOptimize = None, 
                              lowerBoundary = [-1, -1], 
                              upperBoundary = [1, 1], 
                              particleSize=100, 
                              c1=0.5, 
                              c2=0.5, 
                              numberOfIterations=50):
    
    if lowerBoundary[0] >= upperBoundary[0]:
        raise Exception(
            "X'in alt aralığı, X'in üst aralığından daima küçük olmalıdır.")
    elif lowerBoundary[1] >= upperBoundary[1]:
        raise Exception(
            "Y'in alt aralığı, Y'nin üst aralığından daima küçük olmalıdır.")
    elif particleSize < 10:
        raise Exception("Parçacık sayısı 10'dan daha az olamaz.")
    elif c1 < .2 or c1 > 2:
        raise Exception("C1 değeri 0.2 ve 2 aralığında bir değer almalıdır.")
    elif c2 < .2 or c1 > 2:
        raise Exception("C2 değeri 0.2 ve 2 aralığında bir değer almalıdır.")
    elif numberOfIterations < 10:
        raise Exception("İterasyon sayısı 10'dan daha az olamaz.")

    # ---------- SABİT DEĞİŞKEN TANIMLAMALARI

    FUNCTION_TO_OPTIMIZE = functionToOptimize # Optimize edilecek fonksiyon
    LOWER_BOUNDARY = lowerBoundary # Fonksiyonun alt aralıkları [min_x, min_y]
    UPPER_BOUNDARY = upperBoundary # Fonksiyonun alt aralıkları [max_x, max_y]
    PARTICLE_SIZE = particleSize # Fonksiyonun alt aralıkları [min_x, min_y]
    C1 = c1 # Hız hesaplaması için belirlenen c1 sabiti
    C2 = c2 # Hız hesaplaması için belirlenen c2 sabiti
    N = numberOfIterations # İterasyon sayısı
    DIMENSION = len(LOWER_BOUNDARY) # Parçacıkların hareket ettiği boyut sayısı varsayılan len([x,y]) = 2


    # --------- BAŞLANGIÇ DEĞERLERİNİN ATANMASI

    # Parçacığın max sahip olabileceği hız [max_x, max_y]
    MAX_VELOCITY = [abs(UPPER_BOUNDARY[0]) + abs(LOWER_BOUNDARY[0]), abs(UPPER_BOUNDARY[1]) + abs(LOWER_BOUNDARY[1])]
    # Parçacığın min sahip olabileceği hız [min_x, min_y] (ters yön)
    MIN_VELOCITY = [-MAX_VELOCITY[0], -MAX_VELOCITY[1]]

    
    PARTICLE_LOCATION = [] # Parçacıkların lokasyonlarının tutulduğu dizi SxD matris  
    VELOCITY = [] # Parçacıkların hızlarının tutulduğu dizi SxD matris  
    LOCAL_BEST_LOCATION = [] # Parçacıkların yerel en iyi lokasyonlarının tutulduğu dizi SxD matris
    BEST_PARTICLE = [] # Parçacıkların yerel en iyi objective değerlerin tutulduğu dizi Sx1 matris

    GLOBAL_PARTICLE_LOCATION = []  # En iyi global objective değerin tutulduğu 1xD matris
    GLOBAL_BEST = 1e100 # Başlangıçta en iyi global objective değer

    # Varsayılan değerlerin oluşturulması
    for i in range(PARTICLE_SIZE):
        PARTICLE_LOCATION.append([]) # Parçacık için boş bir lokasyon vektörü oluşturuluyor
        VELOCITY.append([]) # Parçacık için boş bir hız vektörü oluşturuluyor
        LOCAL_BEST_LOCATION.append([]) # Parçacık için boş, yerel en iyi lokasyonlarının vektörü oluşturuluyor
        BEST_PARTICLE.append(0) # Parçacık için varsayılan(0) olarak yerel en iyi objective değerler üretiliyor

        for j in range(DIMENSION):
            PARTICLE_LOCATION[i].append(0) # Parçacık için varsayılan(0) başlangıç vektörleri üretiliyor
            VELOCITY[i].append(0) # Parçacık için varsayılan(0) hız vektörleri üretiliyor
            LOCAL_BEST_LOCATION[i].append(0) # Parçacık için varsayılan(0) yerel en iyi lokasyonları üretiliyor

    ALL_GLOBAL_BEST_LOCATIONS = [] # Grafik çiziminde kullanılan, en iyi lokasyon değerlerinin tutulduğu S*D matris
    ALL_GLOBAL_BESTS = [] # Grafik çiziminde kullanılan, en iyi objective değerlerin tutulduğu S*1 matris

    for i in range(N):
        ALL_GLOBAL_BESTS.append(0) # Global en iyi değerlerin varsayılan(0) değerleri üretiliyor
        ALL_GLOBAL_BEST_LOCATIONS.append(0) # Global en iyi lokasyonların varsayılan(0) değerleri üretiliyor
    
    for i in range(PARTICLE_SIZE):
        
        for j in range(DIMENSION):
            # Parçacıkların başlangıç lokasyonları rassal olarak üretiliyor
            PARTICLE_LOCATION[i][j] = random() * (UPPER_BOUNDARY[j] - LOWER_BOUNDARY[j]) + LOWER_BOUNDARY[j]
            # Başlangıç lokasyonları ilk lokasyonlarla bağdaştırılıyor
            LOCAL_BEST_LOCATION[i][j] = PARTICLE_LOCATION[i][j]
              
        # Başlangıç için parçacığın  en iyi lokasyonu hesaplanıyor
        BEST_PARTICLE[i] = FUNCTION_TO_OPTIMIZE(LOCAL_BEST_LOCATION[i][0], LOCAL_BEST_LOCATION[i][1])
        
        # Sadece ilk iterasyona özel olarak global lokasyon ilk parçacığın lokasyonuyla bağdaştırılıyor
        if i == 0:
            GLOBAL_PARTICLE_LOCATION = LOCAL_BEST_LOCATION[0].copy()

        # Eğer geçerli parçacığın objective değeri global değerden daha iyi ise
        if BEST_PARTICLE[i] < GLOBAL_BEST:
            # Yeni global en iyi değer geçerli parçacığın objective değeriyle bağdaştırılıyor
            GLOBAL_BEST = BEST_PARTICLE[i]          
            # Yeni global en iyi lokasyon geçerli parçacığın en iyi lokasyonuyla bağdaştırılıyor
            GLOBAL_PARTICLE_LOCATION = LOCAL_BEST_LOCATION[i].copy()
       
        # Başlangıç için parçacık hızları rassal olarak hızlar üretiliyor
        for j in range(DIMENSION):
            VELOCITY[i][j] = random() * (MAX_VELOCITY[j] - MIN_VELOCITY[j]) + MIN_VELOCITY[j] 
        
    # Global en iyi objective değer ve global en iy lokasyonu bulmak için iterasyonlara başlıyor
    k = 1
    # Maximum iterasyon sayısına ulaşılmadıysa
    while k <= N:
        # Hız hesaplamasında kullanılan iterasyona bağlı omega değeri
        OMEGA = 1 - k * 0.9/N
        # Her parçacık için en iyi değerler bulmak için parçacık sayısı kadar iterasyon başlatılıyor
        for i in range(PARTICLE_SIZE):        
            for j in range(DIMENSION):
                # Parçacığın yeni hızı hesaplanıyor
                VELOCITY[i][j] = OMEGA * VELOCITY[i][j] + C1 * random() * (LOCAL_BEST_LOCATION[i][j] - PARTICLE_LOCATION[i][j]) + C2 * random() * (GLOBAL_PARTICLE_LOCATION[j] - PARTICLE_LOCATION[i][j])
                # Parçacığın yeni lokasyonu hesaplanıyor
                PARTICLE_LOCATION[i][j] = PARTICLE_LOCATION[i][j] + VELOCITY[i][j]  
                # Parçacığın yeni lokasyon değerleri objective fonksiyon sınırlarından taşıyorsa, değerler kırpılıyor
                PARTICLE_LOCATION[i][j] = min(PARTICLE_LOCATION[i][j], UPPER_BOUNDARY[j]) if PARTICLE_LOCATION[i][j] > 0 else max(PARTICLE_LOCATION[i][j], LOWER_BOUNDARY[j])

            # Yeni lokasyona bağlı olarak objective değer üretiliyor
            NEW_PARTICLE_LOCATION = FUNCTION_TO_OPTIMIZE(PARTICLE_LOCATION[i][0], PARTICLE_LOCATION[i][1])
            
            # Eğer yeni objective değer daha iyi ise 
            if NEW_PARTICLE_LOCATION < BEST_PARTICLE[i]:
                # Yerel en iyi lokasyon güncelleniyor
                LOCAL_BEST_LOCATION[i] = PARTICLE_LOCATION[i].copy()
                # Yerel en iyi objective değer güncelleniyor
                BEST_PARTICLE[i] = NEW_PARTICLE_LOCATION

                # Eğer yeni değer globalden daha iyi ise 
                if NEW_PARTICLE_LOCATION < GLOBAL_BEST:
                    # Global en iyi lokasyon güncelleniyor
                    GLOBAL_PARTICLE_LOCATION = PARTICLE_LOCATION[i].copy()
                    # Global en iyi objective değer güncelleniyor
                    GLOBAL_BEST = NEW_PARTICLE_LOCATION
                    


        # Global en iyi lokasyon, grafik için oluşturulan dizimizde saklanıyor
        ALL_GLOBAL_BEST_LOCATIONS[k - 1] = GLOBAL_PARTICLE_LOCATION.copy()
        # Global en iyi objective değer, grafik için oluşturulan dizimizde saklanıyor
        ALL_GLOBAL_BESTS[k - 1] = GLOBAL_BEST
        # Her iterasyon başına hesaplama sonuçlarını ekrana yazıyor
        print('İterasyon {0}: {1} {2}'.format(k, GLOBAL_PARTICLE_LOCATION, GLOBAL_BEST))
        k += 1

    print('\nOptimizasyon tamamlandı en iyi değerler;')
    # Hesaplanan en iyi lokasyon
    print(GLOBAL_PARTICLE_LOCATION)
    # Hesaplanan en iyi objective değer
    print(GLOBAL_BEST)

    # Hesaplanan değerlere bağlı olarak grafikler çizdiriliyor
    createPlot(ALL_GLOBAL_BESTS, ALL_GLOBAL_BEST_LOCATIONS)

# ACKLEY TEST FONKSİYONU
def ACKLEY(x, y):
    val = - 20 * math.exp(-0.2 * math.sqrt(0.5*(x**2 + y**2)))
    val += - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20
    return val

# ACKLEY TEST FONKSIYONU alt sınırları
ACKLEY_LOWER_BOUNDARY = [-5, -5]
# ACKLEY TEST FONKSIYONU üst sınırları
ACKLEY_UPPER_BOUNDARY = [5, 5]

# BEALE TEST FONKSİYONU
def BEALE(x, y):
    val = (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2
    return val

# BEALE TEST FONKSIYONU alt sınırları
BEALE_LOWER_BOUNDARY = [-4.5, -4.5]
# BEALE TEST FONKSIYONU alt sınırları
BEALE_UPPER_BOUNDARY = [4.5, 4.5]

# GOLDSTEIN-PRICE TEST FONKSİYONU
def GSP(x, y):
    val = 1 + ((x + y + 1)**2)*(19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)
    val *= 30 + ((2*x - 3*y)**2)*(18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)
    return val

# GOLDSTEIN-PRICE TEST FONKSIYONU alt sınırları
GSP_LOWER_BOUNDARY = [-2, -2]
# GOLDSTEIN-PRICE TEST FONKSIYONU üst sınırları
GSP_UPPER_BOUNDARY = [2, 2]

# LEVI TEST FONKSIYONU
def LEVI(x, y):
    val = math.sin(3*math.pi*x)**2 + ((x - 1)**2)*(1 + math.sin(3 * math.pi*y)**2)
    val += ((y - 1)**2)*(1 + math.sin(2*math.pi*y)**2)
    return val

# LEVI TEST FONKSIYONU alt sınırları
LEVI_LOWER_BOUNDARY = [-10, -10]
# LEVI TEST FONKSIYONU üst sınırları
LEVI_UPPER_BOUNDARY = [10, 10]

# MAIN fonksiyonu
def main():
    # Parçacık sürüsü optimizasyonu metodumuz çalıştırılıyor
    try:
        particleSwarmOptimization(LEVI, 
                                  LEVI_LOWER_BOUNDARY, 
                                  LEVI_UPPER_BOUNDARY)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

