import winsound as bip
import time as zaman

notalar = {
    "do" : 262,
    "re" : 294,
    "mi" : 330,
    "fa" : 349,
    "sol" : 392,
    "la" : 440,
    "si" : 494,
    "do-" : 523,
}



muzikler = {

    "Çanakkale Türküsü" : [
        {"do":[150, 0.1]},
        {"re":[150, 0.1]},
        {"re":[150, 0.1]},
        {"re":[150, 0.1]},
        {"do-":[150, 0.1]},
        {"si":[150, 0.1]},
        {"do-":[150, 0.1]},
        {"la":[150, 0.1]},
        {"sol":[150, 0.1]},
        {"la":[150, 0.1]},
        {"la":[150, 0.1]},
        {"si":[150, 0.1]},
        {"do-":[150, 0.1]},
        {"si":[150, 0.1]},
        {"la":[150, 0.1]},
        {"sol":[150, 0.1]},
    ],
}

print("Müziklerin isimleri listeleniyor:");
for i in muzikler:
    print(i)

sarki = input("Çalmak istediğiniz müzik adı: ");

if muzikler.get(sarki) :
    print(sarki + ' isimli müziğiniz çalmaya başlıyor!')
    for muzik in muzikler[sarki] :
        for nota in muzik :
            bip.Beep(notalar[nota], muzik[nota][0]);
            zaman.sleep(muzik[nota][1]);
else:
    print(sarki + ' isimli müzik bulunamadı.')