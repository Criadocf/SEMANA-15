#RECEBER A TEMPERATURA MÉDIA DE CADA MÊS DO ANO. (INPUT)(CRIO UMA LISTA)

#TEMPERATURA PODE SER EM KELVIN, FAHERENHEIT OU CELSIUS.

#CALCULE MÉDIA ANUAL E MOSTRE EM KELVIN. (CRIAR FUNÇÃO QUE RECEBE UMA TEMPERATURA E RETORNA ELA KELVIN)

#CALCULE TODAS AS TEMPERATURAS ACIMA DA MÉDIA E EM QUE MÊS ELAS OCORRERAM.

#RECEBER A TEMPERATURA MÉDIA DE CADA MÊS DO ANO. (INPUT)(CRIO UMA LISTA) ! OK

#TEMPERATURA PODE SER EM KELVIN, FAHERENHEIT OU CELSIUS. ! OK

#CALCULE MÉDIA ANUAL E MOSTRE EM KELVIN. (CRIAR FUNÇÃO QUE RECEBE UMA TEMPERATURA E 
# RETORNA ELA EM KELVIN) OK

#CALCULE TODAS AS TEMPERATURAS ACIMA DA MÉDIA E EM QUE MÊS ELAS OCORRERAM.

def temp_func():
    temperatura1 = []
    temperatura = []
    for c in range(0,12):
        a = float(input())
        b = str(input()).upper()
        temperatura.append(a)
        temperatura.append(b)
        y = tuple(temperatura)
        temperatura1.append(y)
        temperatura.clear()
        
    return temperatura1

temperaturas_recebidas = temp_func()

def media_kelvin(temperaturas_recebidas):
    media = 0
    for c in temperaturas_recebidas:
        if c[1] == 'C':
          kc = c[0] + 273.15
          media += kc
        
        if c[1] == 'F':
          kf = ((c[0] - 32) * 5/9) + 273.15
          media += kf

        if c[1] == 'K':
          media += c[0]

    return (media/12).__round__(2)

ch1 = media_kelvin(temperaturas_recebidas)

def temp_acima_media(temperaturas_recebidas, ch1):
            mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
            for c in range(len(mes)):
                if temperaturas_recebidas[c][1] == 'C':
                    kc = temperaturas_recebidas[c][0] + 273.15 
                    if kc > ch1:
                        print(f'{mes[c]}: {kc.__round__(2)}K')

                if temperaturas_recebidas[c][1] == 'F':
                    kf = ((temperaturas_recebidas[c][0] - 32) * 5/9) + 273.15
                    if kf > ch1:
                        print(f'{mes[c]}: {kf.__round__(2)}K')
                
        
                if temperaturas_recebidas[c][1] == 'K':
                    if temperaturas_recebidas[c][0] > ch1:
                        print(f'{mes[c]}: {temperaturas_recebidas[c][0].__round__(2)}K')
                    

print('TEMPERATURA MÉDIA ANUAL')
print(f'{ch1}K')
print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
ch2 = temp_acima_media(temperaturas_recebidas, ch1)



                

                