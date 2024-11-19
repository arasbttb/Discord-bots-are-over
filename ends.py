import discord
from discord.ext import commands
import random
import requests
from bot_mantik import gen_pass, yazi_tura, kalp
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def merhaba(ctx):
    await ctx.send('Merhaba! besin kirliliğii hakkında bilgi almak ister misin? `$besin` yazarak başlayabilirsin.')
@bot.command()
async def besin(ctx):

    await ctx.send("Gıda kirliliği; gıda üretim süreçlerinde çevre kirliliği yaratan maddelerin yanı sıra zararlı kimyasalların ve mikropların gıdalara karışması sonucu ortaya çıkan bir sorundur ve insan sağlığı için büyük tehlike oluşturabilir. Tarım alanında kullanılan kimyasal maddeler zamanla ekosistem dengeyi üzerinde olumsuz etki yapabilir çünkü bu maddeler toprak ve suya karışarak zarar verebilirler Bu kimyasalların başında pestisitler tarımsal ilacalar ve gübreler gelir ve bunlar ürünlerde kalıntı bırakma eğilimindedir Vücuda alındığında ise sağlık problemlerine yol açabilirler Bu tür kirleticiler kanser doğurganlık sorunları sinir sistemi hastalıkları ve bağışıklık sistemi rahatsızlıkları gibi ciddi sağlık sorunlarına sebep olabilir Gelişen endüstride kullanılan katı maddeler ve koruyucu maddeler gibi endüstri gıda üretimindeki katık maddelerinde artış sağlık üzerinde risk oluşturabilir ve bu durum özellikle işlenmiş gıdaların miktarındaki artışla doğru orantılı olarak sağlık üzerindeki etkilere de yansımaktadır. Besin kirliliği hem sağlık hem de çevre açısından büyük bir tehdittir. Tarımda kullanılan kimyasalların su kaynaklarına karışması su kirliliğine ve biyoçeşitliğin azalmasına yol açabilir. Ayrıca gıda üretiminde kullanılan sentetik kimyasallar toprak verimini olumsuz etki edebilir. Organik tarım metodlarına geçişin teşviki ve çevrecil pestisitlerin ve gübrelerin kullanılması ile birlikte doğal işleme yöntemlerinin tercihi gibi önlemler alınarak bu sorunun azaltılması mümkündür. Ayrıca bilinçli seçimlerde bulunan ve organik ve güvenli gıdaları tercihe eden insanlar da besin kirliliğinin azaltılmasına yardımcı olabilirler. Sonuc olarak besin kirliliği; hem insan sağlığını hem de çevreyı olumsuz etkiyen ciddî bir sorun olarak karşımıza çıkmaktadır.Gıda üretiminde daha sürdürülebilir ve sağlıklı yöntemlerin benimsenesinin bu soruna önemli bir katki sağlayacağına inanmaktayım.")
    await ctx.send("Su şisesinin doğada erimesini öğrenmek istiyorsan veya cipsin nasıl üretildiğini öğreneceksen'$su'yaz")

@bot.command()
async def su(ctx):
    ipucu = [" Plastik şişeler modern yaşamın vazgeçilmez bir parçası haline geldi. İçinde genellikle su, içecek, temizlik ürünleri ve yiyecek gibi çeşitli ürünlerin yer aldığı plastik şişeler, hafifliği ve dayanıklılığı nedeniyle tercih ediliyor. Ancak plastik şişelerin kullanım kolaylığı ve pratikliğinin yanı sıra çevresel etkileri de ciddi bir sorunu beraberinde getiriyor. Pek çok plastik şişe, uygun şekilde geri dönüştürülmeden çevreye atıldığında yıllarca bozulmaya devam edebilir. Bu durum denizlere, okyanuslara ve kara alanlarına zarar veriyor. Plastik atıkların azaltılması için geri dönüşüm oranlarının artırılması ve alternatif kullanımların teşvik edilmesi gerekiyor. Çevre üzerindeki olumsuz etkileri azaltmak için şişelerin uygun şekilde geri dönüştürülmesi ve geri dönüştürülmesi önemlidir. Aynı zamanda çevre bilinci arttıkça plastik şişe kullanımının sınırlandırılması ve daha sürdürülebilir yöntemlere geçilmesi önem taşıyor."
            "Cipsler genellikle patateslerin ince dilimlenip ezilmesiyle yapılır. Patatesler soyulup dilimlendikten sonra kızgın yağda kızartılır ve patatesler yumuşar. Kızartıldıktan sonra cipsler tuz, baharat veya baharatlarla tatlandırılır. Ancak bu işlem sırasındaki yüksek sıcaklık, talaşlarda yağın kalitesinin düşmesine neden olur. Ayrıca bazı cipsler trans yağlar, glikoz şurubu, koruyucular ve renklendiriciler gibi zararlı kimyasallar da içerebilir. Bu maddeler aşırı tüketildiğinde kalp hastalıkları, obezite, diyabet ve diğer sağlık sorunlarına yol açabilmektedir. Cipslerin yüksek sodyum içeriği aynı zamanda yüksek tansiyon gibi kardiyovasküler hastalıklara da yol açabilir. Daha sağlıklı alternatifler için cipslerin evde daha fazla yağla hazırlanması veya pişirilmesi önerilebilir. Ancak çip kullanımını sağlık açısından sınırlamak önemlidir."]

    random_tip=random.choice(ipucu)

    await ctx.send(f"İşte o plastikin doğaya zararları veya cipsin üretildeğini oğren >>>: {random_tip}")



@bot.command(name='kalp')
async def kalp_komut(ctx):
    sonuc = kalp()
    await ctx.send(sonuc)

@bot.command(name='yazi_tura')
async def yazi_tura_komut(ctx):
    sonuc = yazi_tura()
    await ctx.send(sonuc)

@bot.command(name='parola')
async def parola(ctx):
    sonuc = gen_pass(pass_length=10)
    await ctx.send(sonuc)

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def rastgele(ctx):
    ImageName = random.choice(os.listdir(r'C:\Users\CASPER\Desktop\Kodland\images'))
    with open(f"images/{ImageName}", "rb") as f:
        resim = discord.File(f)
        await ctx.send(file=resim)


@bot.command()
async def hayvan(ctx):
    ImageName = random.choice(os.listdir(r'C:\Users\CASPER\Desktop\Kodland\hayvan'))
    with open(f"hayvan/{ImageName}", "rb") as f:
        resim = discord.File(f)
        await ctx.send(file=resim)


# Örnek bir get_duck_image_url() fonksiyonu
def get_duck_image_url():
    url = "https://random-d.uk/api/v2/random"
    res = requests.get(url)
    return res.json()["url"]



@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)




# Meme API'si kullanarak rastgele bir meme alan komut
def get_meme_image_url():
    url = "https://api.imgflip.com/get_memes"
    res = requests.get(url)
    memes = res.json()["data"]["memes"]
    return random.choice(memes)["url"]




bot.run("your token")
