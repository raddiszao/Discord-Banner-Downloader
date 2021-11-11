import requests, time, os
def getbanner():
    userId = int(input("Digite o ID do Usuário: "))

    r = requests.get("https://discord.com/api/v8/users/%s"%userId, headers={'Authorization': 'Bot ODY3MDQwNjYwMDUzNjg4MzIx.YPbUig.6p3f6HbUp0KW2WI5CsHX5wczOCk'})
    if r.status_code != 404:
        data = eval(r.text.replace("null", '""'))
        if not "banner" in data:
            print("not banner in data. %s"%data)
            return
        
        print("Baixando banner de %s#%s"%(data["username"], data["discriminator"]))

        banner = data["banner"]
        banner_color = data["banner_color"]
        bannerUrl = ""

        r2 = requests.get(f"https://cdn.discordapp.com/banners/{userId}/{banner}.gif", headers={'Authorization': 'Bot ODY3MDQwNjYwMDUzNjg4MzIx.YPbUig.6p3f6HbUp0KW2WI5CsHX5wczOCk'})

        fileType = "png"
        if r2.status_code == 404 or r2.status_code == 415:
            bannerUrl = f"https://cdn.discordapp.com/banners/{userId}/{banner}.png?size=1024"
        else:
            fileType = "gif"
            bannerUrl = f"https://cdn.discordapp.com/banners/{userId}/{banner}.gif?size=1024"
            
        print("URL do Banner: %s\nCor do banner: %s"%(bannerUrl, banner_color))
        
        r3 = requests.get(bannerUrl)
        
        try:
            open("%s/Banner %s.%s"%(os.path.dirname(os.path.abspath(__file__)), data["username"], fileType), "wb").write(r3.content)
            print("Banner baixado.\n\n")
        except:
            print("Erro ao baixar o banner.\n\n")
        getbanner()

getbanner()
