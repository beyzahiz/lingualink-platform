import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

void main() {
  // 1. Uygulamanın çalışmasını başlatan ana fonksiyon
  // Riverpod kütüphanesinin (State Management) çalışabilmesi için tüm uygulamayı
  // "ProviderScope" dediğimiz bir görünmez koruyucu katmanla sarmalıyoruz.
  runApp(
    const ProviderScope(
      child: MyApp(),
    ),
  );
}

// 2. Uygulamamızın ana widget'ı (Kök Tasarım)
// Bu widget sabit bir ayar katmanı olduğu için StatelessWidget olarak tanımladık.
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    // MaterialApp, Flutter'ın bize sunduğu hazır tasarım dilidir (Material Design).
    // Uygulamanın yazı tipleri, renkleri ve teması buradan yönetilir.
    return MaterialApp(
      title: 'LinguaLink',
      debugShowCheckedModeBanner: false, // Sağ üstteki "Debug" şeridini kaldırır
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterialDesign: true, // Modern görünüm standartlarını aktif eder
      ),
      // Uygulama ilk açıldığında ekranda ne görüneceğini "home" parametresi belirler.
      // Şimdilik test amaçlı oluşturduğumuz Giriş Ekranını çağırıyoruz.
      home: const DummyLoginScreen(),
    );
  }
}

// 3. Geçici Giriş Ekranımız (dummy)
// Kodumuz hata vermesin ve ekranda bir şey görebilelim diye basit bir arayüz oluşturduk.
class DummyLoginScreen extends StatelessWidget {
  const DummyLoginScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // Scaffold, bir mobil ekranın temel iskeletidir (Beyaz boş sayfa sunar).
    return Scaffold(
      // AppBar, ekranın en üstündeki başlık çubuğudur.
      appBar: AppBar(
        title: const Text('LinguaLink Mobil'),
        backgroundColor: Colors.deepPurple,
        foregroundColor: Colors.white,
      ),
      // Body, ekranın geri kalan ana gövdesidir.
      // Center widget'ı, içindeki her şeyi ekranın tam ortasına hizalar.
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center, // Elemanları dikeyde ortalar
          children: [
            const Text(
              'LinguaLink Uygulamasına Hoş Geldin!',
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 20), // İki eleman arasına 20 piksel boşluk koyar
            ElevatedButton(
              onPressed: () {
                // Butona basıldığında şimdilik konsola yazı yazdırıyoruz
                print('Giriş Yap Butonuna Basıldı!');
              },
              child: const Text('Giriş Yap'),
            ),
          ],
        ),
      ),
    );
  }
}