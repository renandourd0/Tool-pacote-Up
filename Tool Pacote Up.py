###################################
#criado por Phablo & Renan Dourado#
###################################


from os import *
from webbrowser import open
from time import sleep

def procura(nomeProgrma):
    procu = system(f'dir "\{nomeProgrma}.exe /s')
    

codico_ativacao = ('TX9XD-98N7V-6WMQ6-BX7FG-H8Q99', 'PVMJN-6DFY6-9CCP6-7BKTT-D3WVR'\
        , ' 7HNRX-D7KGG-3K4RQ-4WPJ4-', '3KHY7-WNT83-DGQKR-F7HPR-844BM', 'W269N-WFGWX-YVC9B-4J6C9-T83GX',\
        'MH37W-N47XK-V7XM9-C7227-GCQG9')

def Ativacao(numeroCodico):
    print(system(f'cscript slmgr.vbs /ipk {codico_ativacao[numeroCodico]}'))
    sleep(3)
    print(system('cscript slmgr.vbs /skms kms.lotro.cc'))
    sleep(3)
    print(system('cscript slmgr.vbs /ato'))


while True:
        system('cls')
        opicao = int(input("""

        =============================================
       + (1)Ativa a Licença                          +
       + ------------------------------------        +
       + (2)Instalar Pacote Office + Ativador        +
       + ------------------------------------        +
       + (3)Drive Boost                              +
       + ------------------------------------        +
       + (4)Atualiza programa do computador          +
       + -------------------------------------       +
       + (5)Programas de extrai e Compactar arquivos + 
       + -------------------------------------       +
       + (6)Navegadores de Intenet                   +
       + --------------------------------------      +
       + (7)Sair                                     +
        =============================================
        
        """))

        if opicao == 1:
                system('cls')
                opicao = int(input('Qual Sua Edição do Windows?\n(1)Home Core\n(2)Home/Core (Country Specific)\n(3)Home/Core (Single Language)\n(4)Home/Core N\n(5)Professional\n(6)Professional N\n:'))

                if opicao == 1:
                    Ativacao(0)
                elif opicao == 2:
                    Ativacao(1)
                elif opicao == 3:
                    Ativacao(2)
                elif opicao == 4:
                    Ativacao(3)
                elif opicao == 5:
                    Ativacao(4)
                elif opicao == 6:
                    Ativacao(5)
                else:
                    print('Escolha uma opição valida!')
        
        elif opicao == 2:
            system('cls')
            link_url = r'https://github.com/renandourd0/Pakgade/archive/refs/heads/main.zip'
            open(link_url)
            input('Aperte "Enter" Quando o programa for baixado')
            sleep(3)
            system('start Office.exe')
            sleep(3)
            continue
            
        elif opicao == 3:
            system('cls')
            link_drive_boost = r'https://cdn.iobit.com/dl/driver_booster_setup.exe'
            open(link_drive_boost)
            input('Aperte "Enter" Quando o programa for baixado')
            sleep(3)
            system('start driver_booster_setup.exe')
            sleep(3)
            continue
        
        elif opicao == 4:
            system('cls')
            print(system('winget upgrade --all'))
            input('Pressone "Enter Para Continua')
            system('cls')

        elif opicao == 5:
            system('cls')
            opicao2 = int(input('(1)Winrar\n(2)Z-zip\n'))
            if opicao2 == 1:
                link_winrar = 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-622br.exe'
                open(link_winrar)
                input('Aperte "Enter" Quando o programa for baixado')
                sleep(3)
                system('start winrar-x64-622br.exe')
                sleep(3)
                continue

            elif opicao2 == 2:
                link_Zzip = 'https://www.7-zip.org/a/7z2201-x64.exe'
                open(link_Zzip)
                input('Aperte "Enter" Quando o programa for baixado')
                sleep(3)
                system('start 7z2201-x64.exe')
                sleep(3)
                continue
            else:
                print('Opição invalida!')

        elif opicao == 6:
            system('cls')
            opicao3 = int(input('(1)Google Chrome\n(2)Opera\n(3)Opera GX\n:'))

            if opicao3 == 1:
                link_chrome = r'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B91601462-9562-B504-87A1-C2009A4804DA%7D%26lang%3Dpt-PT%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DFKPE%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe'
                open(link_chrome)
                input('Aperte "Enter" Quando o programa for baixado')
                sleep(3)
                system('start ChromeSetup.exe')
                sleep(3)
                continue

            elif opicao3 == 2:
                link_opera = r'https://www.opera.com/pt-br/computer/thanks?ni=stable&os=windows&utm_campaign=%2300+-+WW+-+Search+-+EN+-+Branded'
                open(link_opera)
                input('Aperte "Enter" Quando o programa for baixado')
                sleep(3)
                system('start OperaSetup.exe')
                sleep(3)
                continue
            
            elif opicao3 == 3:
                link_opera_gx = r'https://www.opera.com/pt-br/computer/thanks?ni=eapgx&os=windows&utm_source=google&utm_medium=pa&utm_campaign=OGX_BR_Search_PT_T1_Brand_V2&utm_id=CjwKCAjw4ZWkBhA4EiwAVJXwqTdOEvs1wXTf4Qtfkzdxz-U5XmWZtg8PDowUOMF10odMrka8TvcKOBoCKIQQAvD_BwE'
                open(link_opera_gx)
                input('Aperte  "Enter" Quando o programa for baixado')
                sleep(3)
                system('start OperaGXSetup.exe')
                sleep(3)
                continue


        elif opicao == 7:
            break


        else:
            print('Opoção Ivalida!')
