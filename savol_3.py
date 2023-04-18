# Pandas Python dasturlash tili uchun yaratilgan bolib matematik hisob-kitoblari 
# malumotlar analizi va malumotlar tahlilini amalga oshirish uchun qollaniladi. 
# Uning asosiy funksiyalari malumotlar keltirish va tahlil qilish malumotlar ustida 
# filtrlash birlashtirish tartiblash va boshqa kabi amallarni amalga oshirishni 
# osonlashtirishdir. Pandas "DataFrame" va "Series" nomli iki asosiy obyektlarga 
# ega bolib ular matnlarni qabul qiladigan kopincha turdagi malumotlar bilan 
# ishlash imkoniyatini beradi. Pandas kutubxonasini ishlatib odatda CSV Excel va 
# SQL malumotlarini oqish va yozish malumotlarning boshqa turlari bilan ham ishlash 
# mumkin. Pandas kutubxonasining foydalanishidan avval uni ornatish talab qilinadi. 
# Pandas kutubxonasi Pythonning hamma versiyalarida qollanilishi mumkin.


#Misol:
import pandas as pd

data = {'Ism': ['Jamshid', 'Ogabek', 'Sarvinoz', 'Ansor'],
        'Yosh': [25, 18, 35, 40],
        'Jins': ['Erkak', 'Erkak', 'Qiz', 'Erkak']}
df = pd.DataFrame(data)
print(df)
#         Ism  Yosh   Jins
# 0   Jamshid    25  Erkak
# 1    Ogabek    18  Erkak
# 2  Sarvinoz    35    Qiz
# 3     Ansor    40  Erkak
print("="*50)
df_filtered = df[df['Yosh'] > 30]
print(df_filtered)
#         Ism  Yosh   Jins
# 2  Sarvinoz    35    Qiz
# 3     Ansor    40  Erkak
print("="*50)

df_sorted = df.sort_values(by='Yosh', ascending=False)
print(df_sorted)

#         Ism  Yosh   Jins
# 3     Ansor    40  Erkak
# 2  Sarvinoz    35    Qiz
# 0   Jamshid    25  Erkak
# 1    Ogabek    18  Erkak