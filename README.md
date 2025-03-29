# YOLO (You Only Look Once) Implementasyonu

Bu proje, YOLO (You Only Look Once) nesne tespit algoritmasının temel bileşenlerinin Python ile implementasyonunu içermektedir.

> **Not**: Bu proje şu anda erken geliştirme aşamasındadır. Şu an için sadece temel YOLOv1 bileşenleri implement edilmiştir. Tam fonksiyonel bir nesne tespit sistemi için daha fazla geliştirme gerekmektedir.

## Proje Yapısı

```
.
├── YOLOv1/
│   └── train.py
└── LICENSE
```

## Özellikler

- YOLOv1 mimarisinin temel bileşenlerinin implementasyonu
- Konvolüsyonel katmanlar (conv2D)
- ReLU aktivasyon fonksiyonu
- Residual bloklar
- Dense (tam bağlantılı) katmanlar

## Gereksinimler

- Python 3.x
- NumPy

## Kullanım

Projeyi kullanmak için:

1. Gerekli bağımlılıkları yükleyin:
```bash
pip install numpy
```

2. `YOLOv1/train.py` dosyasını çalıştırın:
```bash
python YOLOv1/train.py
```

## Implementasyon Detayları

### YoloV1 Sınıfı

`YoloV1` sınıfı şu anda aşağıdaki temel bileşenleri içerir:

- `conv2D`: 2 boyutlu konvolüsyon işlemi
- `relu`: ReLU aktivasyon fonksiyonu
- `residual_block`: Artık (residual) blok implementasyonu
- `flatten`: Giriş tensörünü düzleştirme
- `dense`: Tam bağlantılı katman

### Mevcut Durum

- Temel YOLOv1 bileşenleri implement edilmiştir
- Basit test örnekleri eklenmiştir
- Tam eğitim ve test pipeline'ı henüz eklenmemiştir
- Veri yükleme ve ön işleme fonksiyonları henüz eklenmemiştir

## Gelecek Geliştirmeler

- [ ] Veri yükleme ve ön işleme fonksiyonları
- [ ] Tam eğitim pipeline'ı
- [ ] Test ve değerlendirme fonksiyonları
- [ ] Model kaydetme ve yükleme özellikleri
- [ ] Görselleştirme araçları

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir özellik dalı oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Dalınıza push yapın (`git push origin yeni-ozellik`)
5. Bir Pull Request oluşturun 