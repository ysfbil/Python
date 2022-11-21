@echo off
rem aşağıdaki ifade işlemlerin yazılmasını engeller

cd /D C:\Users\ysfbil\AppData\Local\Programs\Python\Python310\Scripts
echo Ornek modul (kutuphane) son versiyon yukleme ifadesi:
echo python -m pip install modulAdi
echo. 
echo Modulu guncellemek icin:
echo python -m pip install --upgrade SomePackage
echo.
echo pip ile baslayan bir komutla yukleme yapmak icin cd scripts yazip pip programinin oldugu klasoru actiktan sonra asagidaki ifade kullanilir:
echo pip install moduAdi
echo.
echo indirilen bir tar.gz dosyasindan modul yuklemek icin scripts klasoru acildiktan sonra dosya bu klasore yuklenir ve asagidaki ifade kullanilir:
echo pip install dosyaAdi.tar.gz
echo .
echo Belirli bir versiyonu yuklemek icin
echo pip install paketAdi==1.2.2
echo .
echo Paket kaldirmak icin
echo pip uninstall paketAdi
rem echo. ile bir boş satır oluşturuluyor
echo. 
echo yuklu modulleri gormek icin
echo pip freeze
echo .
rem aşağıdaki ifade cmd'nin kapanmasını engeller
cmd /k