from PIL import Image, ImageDraw, ImageFont



def main():

    '''
        Inicia parametros da function
    '''

    #Abre a imagem de template
    imagem = Image.open("./template.jpg")

    #Abre a imagem de logo
    logo = Image.open("./logo.png").convert("RGBA")

    #Derfine a fonte a ser utilizada
    font1 = ImageFont.truetype('./orange.ttf', size=50)
    
    #Abre a imagem de template
    imagem = Image.open("./template.jpg")

    #Abre a imagem de logo
    logo = Image.open("./logo.png").convert("RGBA")

    #Derfine a fonte a ser utilizada
    font1 = ImageFont.truetype('./orange.ttf', size=50)

    #Define ferramenta de desenho
    lapis = ImageDraw.Draw(imagem)


    cria_linha(lapis)
    imagem.save("./nova_imagem.jpg")
    cria_texto(lapis,font1)
    imagem.save("./nova_imagem.jpg")
    cola_logo(imagem,logo)
    


def cria_linha(lapis):
    #Cria a linha amarela na imagem    
    lapis.line(
        (82, 105, 536, 105),
        fill="#FFCC00",
        width=5
    )
    

def cria_texto(lapis,font1):
    #Monta o texto padrão
    lapis.text (
        (82,68),
        text="teste logo",
        fill="#000",
        font=font1
    )

def cola_logo(imagem,logo):
    #copia imagem
    back_im = imagem.copy()
    
    #seta tamanho do logo
    new_width  = 300
    new_height = 300
    logo = logo.resize((new_width, new_height), Image.ANTIALIAS)

    #cola o logo
    back_im.paste(logo, (150, 130), logo)

    salva(back_im)

def salva(back_im):
    #Salva a nova imagem alterada
    back_im.save("./nova_imagem.jpg")

#Inicia
main()
    

