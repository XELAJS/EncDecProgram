import random
import string
from Crypto.Random import get_random_bytes

# Büyük ve küçük harfleri, ve rakamları içeren karakterlerin listesi
karakterler = string.ascii_letters + string.digits

# Rastgele karakter dizisini oluştur
uzunluk = 10  # İfade uzunluğu
rastgele_ifade = ''.join(random.choice(karakterler) for _ in range(uzunluk))

print("Rastgele ifade:", rastgele_ifade)

