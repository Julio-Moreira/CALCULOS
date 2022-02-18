# ;)
# ! {<J>}
# ! autor: Julio C. Moreira 
# ! feito entre 17/01/2022 ate 11/02/2022


# ? BIBLIOTECAS                                          (**/**:)

import sympy
from sympy.abc import x
from time import sleep
from num2words import num2words
from random import randint

# ?  MENU PRINCIPAL {                                      (17/01:)

sleep(0.3)
print('\033[33m/ '*17)
print('  \033[31;1m{:^28}\033[m'.format('BEM VINDO'))
print('\033[33m\ \033[m'*17)
sleep(0.4)
print('\n\033[31m[\033[36mC\033[31m]\033[36mcalcular   \033[31m[\033[35mE\033[31m]\033[35mequacao  \033[31m[\033[32mU\033[31m]\033[32muteis\033[m \033[31m[\033[33mS\033[31m]\033[33msair') # printa com os caracteres com cores =
# para declarar uma cor e so usar \033[m dentro desse colchete voce pode dar ate 3 info (cor do fundo;cor do texto;tipo do texto)
# tipo do texto = 0:none 1:bold (negrito) 4:underline 7: negative (inveroso)
# cor do fundo = 40:branco 41:vermelho 42:verde 43:amarelo 44:azul 45:roxo 46:ciano 47:cinza
# cor do texto = 30:branco 31:vermelho 32:verde 33:amarelo 34:azul 35:roxo 36:ciano 37:cinza
sleep(0.5)
esc_prin = str(input('\n\033[34m[\033[36mC\033[34m/\033[35mE\033[34m/\033[32mU\033[34m/\033[33mS\033[34m]\n\033[36m: \033[m')).strip().lower()[0]

# ?  }

#  ? CALCULAR  {                                           (18/01:)

if esc_prin == 'c':
    sleep(0.3)
    print('\033[31m\nOK\nindo para \033[31;1mcalculos\n{<J>}\033[m')
    #  * MENU PRINCIPAL 
    sleep(0.5)    
    print('\n\n')
    print('\033[36m/ '*17)
    print('  \033[31;1m{:^28}\033[m'.format('CALCULOS'))
    print('\033[36m\ \033[m'*17)
    sleep(0.6)
    print('\n\033[36m[\033[34mC\033[36m]\033[34mcalculadora \033[36m[\033[32mS\033[36m]\033[32msintaxe \033[36m[\033[31mF\033[36m]\033[31mfinalizar\033[m\n')
    sleep(0.7)
    esc_cal = str(input('\033[36m[\033[34mC\033[36m/\033[31mF\033[36m/\033[32mS\033[36m]\n\033[36m:\033[m')).strip().lower()[0]    
    if esc_cal == 'c':
        sleep(0.3)
        print('\033[31m\nOK\nindo para \033[31;1mcalculadora\n{<J>}\033[m')
        sleep(0.4)
        # *  CALCULADORA
        conta = input('\n\033[36;1mescreva sua conta: \033[m').lower().replace('x','*').replace(':','/').replace('p','**').replace('rq','**(1/2)').replace(',','.') # troca todos os caracteres por operadores do python
        sleep(0.2)
        print('\n\033[31mcalculando...\n\033[m')
        sleep(0.6)
        res_con = eval(conta) # resolve a conta
        print('\033[31;1m{}\033[m'.format(res_con))
        sleep(10)
        print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
        exit() # sai do programa
    #  * SINTAXE
    if esc_cal == 's':
        sleep(0.3)
        print('\033[31m\nOK\nindo para \033[31;1msintaxe\n{<J>}\033[m')
        sleep(0.3)
        print('\n\033[31;1mx ou * = multiplicacao\n: ou / = divisao\n+ = adicao\n- = subtracao\np ou ** = potencia\nrq = raiz quadrada\033[m')
        sleep(10)
        print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
        exit()
    # * VOLTAR
    if esc_cal == 'f':
        sleep(0.3)
        print('\033[36mOK\nfinalizando\033[m')
        sleep(0.5)
        exit()

# ?  }

# ?  EQUACAO {                                           (19/01:)

if esc_prin == 'e':
    sleep(0.3)
    print('\033[31m\nOK\nindo para \033[31;1mequacao\n{<J>}\033[m')
    #  * MENU PRINCIPAL
    sleep(0.5)   
    print('\n\n')
    print('\033[35m/ '*17)
    print('  \033[31;1m{:^28}\033[m'.format('EQUACAO'))
    print('\033[35m\ \033[m'*17)
    sleep(0.6)
    print('\n\033[35m[\033[34mE\033[35m]\033[34mequacao \033[35m[\033[32mS\033[35m]\033[32msintaxe \033[35m[\033[31mF\033[35m]\033[31mfinalizar\033[m\n')
    sleep(0.7)
    esc_equa = str(input('\033[35m[\033[34mE\033[35m/\033[31mF\033[35m/\033[32mS\033[35m]\n\033[36m:\033[m')).strip().lower()[0]   
    if esc_equa == 'e':
        sleep(0.3)
        print('\033[31m\nOK\nindo para \033[31;1mequacao\n{<J>}\033[m')
        #  *  EQUACAO
        sleep(0.3)
        x = sympy.Symbol('x') # declara 'x' como icognita
        equacao = input('\n\033[36mdigite a equacao (apenas o primeiro membro): \033[m').strip().replace('x','*x').replace('p','**').replace('.','*').replace(':','/')
        sleep(0.4)
        eq_res = sympy.solve(equacao,x) # resolve a equacao
        print('\n\033[1;31m{}\033[m'.format(eq_res))  
        sleep(10)
        print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
        exit()
    if esc_equa == 's':
        sleep(0.3)
        print('\033[31m\nOK\nindo para \033[31;1msintaxe\n{<J>}\033[m')
        #  * SINTAXE
        sleep(0.3)
        print('\033[31;1mx = icognita\n. ou * = multiplicacao\n: ou / = divisao\n+ = adicao\n- = subtracao\np ou ** = potencia')
        sleep(10)
        print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
        exit()
    if esc_equa == 'f':
        # *  FINALIZAR
        sleep(0.3)
        print('\033[35mOK\nfinalizando\033[m')
        sleep(0.5)
        exit()   

# ?  }
     
# ?  UTEIS {                                    (21/01;22/01;29/01;6/02;8/2;11/2:)

if esc_prin == 'u':
    sleep(0.3)
    print('\033[31m\nOK\nindo para \033[31;1muteis\n{<J>}\033[m')
    # *  MENU PRINCIPAL
    sleep(0.5)   
    print('\n\n')
    print('\033[35m/ '*17)
    print('  \033[31;1m{:^28}\033[m'.format('UTEIS'))
    print('\033[35m\ \033[m'*17)
    sleep(0.6)
    print('\n\033[32m[\033[35mP\033[32m]\033[35mporcentagem \033[32m[\033[36mC\033[32m]\033[36mconversor \033[32m[\033[31mT\033[32m]\033[31mterminar \033[32m[\033[33mA\033[32m]\033[33manalizador \033[32m[S]sorteio \033[m\n')
    sleep(0.7) 
    esc_uteis = str(input('\033[35m[\033[35mP\033[35m/\033[mF\033[35m/\033[36mC\033[35m/\033[31mT\033[35m/\033[33mA\033[35m/\033[32mS\033[35m]\n\033[36m: \033[m')).strip().lower()[0]
    if esc_uteis == 'a':
        sleep(0.3)
        print('\033[31m\nOK\nindo para \033[31;1manalizador\n{<J>}\033[m')
        # * ANALIZADOR DE NUMEROS  
        sleep(0.4)
        num_ana_str = str(input('\n\033[33mdigite um numero inteiro para analizar: \033[m'))
        num_an_len = len(num_ana_str.replace(' ','')) # pega todos os caracteres e tira o espaco 
        num_ana = int(num_ana_str) # transforma a str em int
        na_bin_etc = '\033[33mem binario: \033[31;1m{}\n\033[33mem hexadecimal: \033[31;1m{}\n\033[33mem octal: \033[31;1m{}\033[m'.format(bin(num_ana)[2:],hex(num_ana)[2:],oct(num_ana)[2:]) # pega o bin etc em os 2 primeiros caracteres
        na_ant_suc = '\033[33mseu antecessor e \033[31;1m{}\n\033[33me seu sucessor: \033[31;1m{}\033[m'.format(num_ana-1,num_ana+1)
        #-=-=-=-=-=-=-=-=-=-=-#
        na_dob_etc = '\033[33mseu dobro e \033[31;1m{}\n\033[33mo triplo \033[31;1m{}\n\033[33mquadruplo \033[31;1m{}\n\033[33mquintuplo \033[31;1m{}\n\033[33mmetade \033[31;1m{}\n\033[33mum terco \033[31;1m{}\n\033[33mum quarto \033[31;1m{}\n\033[33mum quinto \033[31;1m{}'.format(num_ana*2,num_ana*3,num_ana*4,num_ana*5,num_ana/2,num_ana/3,num_ana/4,num_ana/5)
        #-=-=-=-=-=-=-=-=-=-=-#
        if num_ana % 2 == 0: # se um numero e divisivel por 2 ele e par
            na_par_imp = '\033[33messe numero e \033[31;1mpar'
        else:
            na_par_imp = '\033[33messe numero e \033[31;1mimpar'
        ale = 1
        div = 0
        div_num = []            
        while ale <= num_ana: # enquanto um numero qualquer seja menor que o escolhido pelo usu
            if num_ana % ale == 0:
                div += 1
                div_num.append(ale)
            ale += 1
            if div == 2: # um numero primo so pode ser dividido por 1 e por ele mesmo ou seja ele so tem 2 divisores
                na_primo = f'\033[33messe numero e \033[31;1mprimo ou seja divisivel por \033[31;1m1 e {num_ana}\033[m'
            else:
                na_primo = f'\033[33messe numero \033[31;1mnao e primo \033[33mpois e divisivel por \033[31;1m{div_num}'
        exten = num2words(num_ana,lang='pt_BR')
        sleep(0.5)
        print('\n\033[31manalizando numero...\033[m')
        sleep(0.6)
        print(f'\n\033[31manalizando o numero \033[31;1m{num_ana}\033[31m obtive os resultados:\033[33m\nquantidades de numeros: \033[31;1m{num_an_len}\n{na_bin_etc}\n{na_ant_suc} \n{na_par_imp}\n{na_primo}\n{na_dob_etc}\n\033[33mseu extenso e: \033[31;1m{exten}\n\033[33msua raiz quadrada: \033[31;1m{num_ana**(1/2)}')
        sleep(10)
        print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
        exit()
    if esc_uteis == 's':
        sleep(0.3)
        print('\033[31m\nOK\nindo para \033[31;1msorteio\n{<J>}\033[m')
        # * SORTEIO
        sort = 's'
        while sort == 's':
            sleep(0.4)
            sort_comec = int(input('\n\033[32mdigite o comeco: '))
            sleep(0.5)
            sort_fim = int(input('\033[32mdigite o fim: \033[m'))
            num_sort = randint(sort_comec,sort_fim)
            sleep(0.4)
            print(f'\n\033[35mo numero sorteado foi: \033[31;1m{num_sort}\033[m')
            sleep(0.6)
            sort = str(input('\n\033[31mquer continuar? [S/N] \033[m')).strip()[0]
            while sort not in 'sn':
                sleep(0.7)
                print('\n\033[31;1mERRO\nopcao nao encontrada...\ntende novamente')
                sleep(0.8)
                sort = str(input('\033[31mquer continuar? [S/N] \033[m')).strip()[0] 
        sleep(10)
        print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
        exit()
    if esc_uteis == 'c':
        sleep(0.3)
        print('\033[31m\nOK\nindo para \033[31;1mconversor\n{<J>}\033[m')
        # * MENU PRINCIPAL
        sleep(0.5)   
        print('\n\n')
        print('\033[36m/ '*17)
        print('  \033[31;1m{:^28}\033[m'.format('conversor'))
        print('\033[36m\ \033[m'*17)
        sleep(0.6)
        print('\n\033[32m[\033[35mM\033[32m]\033[35mmedidas \033[32m[\033[31mT\033[32m]\033[31mtemperaturas \033[32m[\033[33mP\033[32m]\033[33mpesos \033[32m[\033[36mS\033[32m]\033[36msair\033[m\n')
        sleep(0.7) 
        esc_conv = str(input('\033[35m[\033[33mP\033[35m/\033[31mT\033[35m/\033[35mM\033[35m/\033[36mS\033[35m]\n\033[36m: \033[m')).strip().lower()[0]
        if esc_conv == 't':
            sleep(0.3)
            print('\033[31m\nOK\nindo para \033[31;1mtemperaturas\n{<J>}\033[m')
            # * TEMPERATURAS
            sleep(0.4)
            print('\n\033[31;1mcoloque a letra da temperatura \033[31m(c/f/k)\033[31;1m no primero caracter e depois a temperatura\n\033[35mpor exemplo: C 17.5 \033[m')
            temp = str(input('\n\033[36m: ')).strip().lower().split()
            temp_cfk = temp[0]
            temp_int = float(temp[1])
            if temp_cfk == 'c':
                sleep(0.3)        
                print('\n\033[35mcalculando...')  
                sleep(0.6)      
                print(f'\n\033[33m{temp_int} celcius em \033[31mkelvin: \033[31;1m{temp_int+273} \033[35mfarenhait: \033[35;1m{temp_int*1.8+32:.2f} \033[m')
                sleep(2)
                print(f'\n\n\033[33mformulas usadas:\n\033[31mC p/ K: \033[31;1mc + 273 ({temp_int} + 273 = {temp_int+273})\n\033[35mC p/ F: \033[35;1mc x 1.8 + 32 ({temp_int} x 1.8 + 32 = {temp_int*1.8+32:.2f})\033[m') 
                sleep(10)
                print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
                exit()       
            if temp_cfk == 'k':
                sleep(0.3)        
                print('\n\033[35mcalculando...')  
                sleep(0.6)      
                print(f'\n\033[33m{temp_int} kelvin em \033[31mcelsius: \033[31;1m{temp_int-273} \033[35mfarenhait: \033[35;1m{(temp_int-273)*1.8+32:.2f} \033[m')
                sleep(2)
                print(f'\n\n\033[33mformulas usadas:\n\033[31mK p/ C: \033[31;1mk - 273 ({temp_int} - 273 = {temp_int-273})\n\033[35mK p/ F: \033[35;1m(k-273) x 1.8 + 32 (({temp_int}-273) x 1.8 + 32 = {(temp_int-273)*1.8+32:.2f})\033[m') 
                sleep(10)
                print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
                exit()    
            if temp_cfk == 'f':
                sleep(0.3)        
                print('\n\033[35mcalculando...')  
                sleep(0.6)      
                print(f'\n\033[33m{temp_int} farenhait em \033[31mkelvin: \033[31;1m{(temp_int-32) * 5/9 + 273:.2f} \033[35mcelsius: \033[35;1m{(temp_int-32)/1.8:.2f} \033[m')
                sleep(2)
                print(f'\n\n\033[33mformulas usadas:\n\033[31mF p/ K: \033[31;1m(f-32) x 5/9 + 273 (({temp_int}-32) x 5/9 + 273 = {(temp_int-32)*5/9+273:.2f})\n\033[35mF p/ C: \033[35;1m(f-32)/1.8 (({temp_int}-32)/1.8 = {(temp_int-32)/1.8:.2f})\033[m') 
                sleep(10)
                print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
                exit()   
        if esc_conv == 'p':
            sleep(0.3)
            print('\033[31m\nOK\nindo para \033[31;1mpesos\n{<J>}\033[m')
            # * PESOS
            sleep(0.5)
            print('\n\033[31mcoloque o peso e depois a unidade (kg/g) por exemplo: 12.5 kg\033[m')
            peso = str(input('\n\033[33m: \033[m')).lower().strip().split()
            peso_uni = peso[1]
            peso_num = float(peso[0])
            if peso_uni == 'kg':
                sleep(0.6)
                print('\n\033[31mcalculando...')
                sleep(0.9)
                print(f'\n\033[31m{peso_num} kg em g: \033[31;1m{peso_num * 1000}\033[31m\npara fazer isso e so multiplicar por 1000: {peso_num} x 1000 = {peso_num*1000}')
            if peso_uni == 'g':
                sleep(0.6)
                print('\n\033[31mcalculando...')
                sleep(0.9)
                print(f'\n\033[31m{peso_num} g em kg: \033[31;1m{peso_num/1000}\033[31m\npara fazer isso e so dividir por 1000: {peso_num} : 1000 = {peso_num/1000}')
        if esc_conv == 'm':
            sleep(0.3)
            print('\033[31m\nOK\nindo para \033[31;1mmedidas\n{<J>}\033[m')
            # * MEDIDAS
            sleep(0.5)
            print('\n\033[31mcoloque a medida e depois a unidade (km/m/cm) por exemplo: 12.5 km\033[m')
            medidas = str(input('\n\033[33m: \033[m')).lower().strip().split()
            med_uni = medidas[1]
            med_num = medidas[0]
            if med_uni == 'km':
                sleep(0.6)
                print('\n\033[31mcalculando...')
                sleep(0.9)
                print(f'\n\033[31m{med_num} km em m: \033[31;1m{med_num*1000}\033[31m\npara fazer isso e so multiplicar por 1000: {med_num} x 1000 = {med_num*1000}\n{med_num} km em cm: {med_num*100000}')
            if med_uni == 'm':
                sleep(0.6)
                print('\n\033[31mcalculando...')
                sleep(0.9)
                print(f'\n\033[31m{med_num} m em km: \033[31;1m{med_num/1000}\033[31m\npara fazer isso e so divida por 1000: {med_num} : 1000 = {med_num/1000}\n{med_num} m em cm: {med_num*100}')
            if med_uni == 'cm':
                sleep(0.6)
                print('\n\033[31mcalculando...')
                sleep(0.9)
                print(f'\n\033[31m{med_num} cm em km: \033[31;1m{med_num/100000}\033[31m\npara fazer isso e so divida por 100000: {med_num} : 100000 = {med_num/1000}\n{med_num} cm em m: {med_num/100}')
        if esc_conv == 's': 
            # * SAIR
            sleep(0.3)
            print('\n\n\n\033[31mfinalizando programa\n(reinicie para voltar)')
            exit() 
    if esc_uteis == 'p':
        sleep(0.3)
        print('\033[31m\nOK\nindo para \033[31;1mporcentagem\n{<J>}\033[m')
        # * PORCENTAGEM
        sleep(0.5)   
        print('\n\n')
        print('\033[36m/ '*17)
        print('  \033[31;1m{:^28}\033[m'.format('porcentagem'))
        print('\033[36m\ \033[m'*17)
        sleep(0.6)
        print('\n\033[32m[\033[35mA\033[32m]\033[35maumento \033[32m[\033[31mT\033[32m]\033[31mtransformador\033[32m[\033[33mD\033[32m]\033[33mdiminuicao \033[32m[\033[36mS\033[32m]\033[36msair\033[m\n')
        sleep(0.7) 
        esc_porc = str(input('\033[35m[\033[33mD\033[35m/\033[31mT\033[35m/\033[35mA\033[35m/\033[36mS\033[35m]\n\033[36m: \033[m')).strip().lower()[0]
        if esc_porc == 't':
            sleep(0.3)
            print('\033[31m\nOK\nindo para \033[31;1mtransformador\n{<J>}\033[m')
            # * TRANSFORMADOR
            sleep(0.5)  
            print('\n\033[31mdigite a porcentagem primeiro e depois o numero por exemplo: 80 de 4')
            trans_num = str(input('enter the percentage: ')).strip().split()
            num_por = int(trans_num[0])
            num_id = int(trans_num[2])
            print(f'\033[31;1m{(num_por/100)*num_id}')
        if esc_porc == 'a':
            sleep(0.3)
            print('\033[31m\nOK\nindo para \033[31;1maumento\n{<J>}\033[m')
            # * AUMENTO
            sleep(0.5)  
            print('\n\033[31menter percentage and amount for example: 30 300')
            increase_num = str(input('enter the percentage: ')).strip().split()
            au_num_por = int(increase_num[0])
            au_num_id = int(increase_num[1])
            print(f'\n\033[31;1m{((au_num_por/100)+1)*au_num_id}')
        if esc_porc == 'd':
            sleep(0.3)
            print('\033[31m\nOK\nindo para \033[31;1mdiminuicao\n{<J>}\033[m')
            # * DIMINUICAO
            sleep(0.5)  
            print('\n\033[31menter percentage and amount for example: 30 300')
            decrease_num = str(input('enter the percentage: ')).strip().split()
            di_num_por = int(decrease_num[0])
            di_num_id = int(decrease_num[1])
            print(f'\n\033[31;1m{((di_num_por/100)-1)*di_num_id}')
        if esc_porc == 's':
            # * SAIR
            sleep(0.3)
            print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
            exit()
    if esc_uteis == 't':
        # * TERMINAR
        sleep(0.3)
        print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
        exit()
# ?  }

# ?  ERRO {                                              (17/01:)

if esc_prin not in 'ceus': # se a escolha do usuario nao for nem c nem e nem u e nem s aparece o erro
    sleep(0.6)
    print('\033[31m\nERROR\nresultado nao encontrado\n\033[m')    
    sleep(10)
    print('\n\n\n\033[35mfinalizando programa\n(reinicie para voltar)')
    exit()

# ?  }

# ?  SAIR {                                              (17/01:)

if esc_prin == 's':
    sleep(0.3)
    print('\033[34mOK \nfinalizando programa...\033[m')
    sleep(0.8)
    exit()

# ?  }
