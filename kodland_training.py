meme_sozlugu = {
        "CRINGE": "Garip ya da utandırıcı bir şey",
        "LOL": "Komik bir şeye verilen cevap",
        "ez": "Oyunda sizi yenip kendini çok iyi sanan toxic insanların dediği şey",
        "gg": 'açılımı good game olan oyun bittiğinde chate yazdığınız şey',
        'bruh': 'bruh moment öyle bir andır ki capslerinde kullanılan kelime',
            }
   
kelime = input('Anlamadığınız bir kelimeyi yazınız')

if kelime in meme_sozlugu:
    print('sözlükte var')
    
else:
    print('sözlükte yok')
