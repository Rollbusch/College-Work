# PILHAR PORTÁVEIS
pilharPortaveis = {
    1:{'nome': 'Pão de Açucar - Barão Geraldo',
    'End': 'Rua Albino José Barbosa Oliveira, 1340 - Barão Geraldo',
    'local':'''22°49'35.0"S 47°04'44.7"W''',
    'dla': 1369.58,
    'dlo': 2824.74},        
    
    2:{'nome': 'Telha Norte Campinas',
    'End': 'Av. Guilherme Campos, 500 - Bloco II',
    'local':'''22°51'02.2"S 47°03'44.2"W''',
    'dla': 1371.03,
    'dlo': 2823.73},
    
    3:{'nome': 'Vivo - Campinas Iguatemi',
    'End': 'Shopping Av. Iguatemi, 777 - Vivo',
    'local': '''22°53'33.9"S 47°01'36.0"W''',
    'dla': 1373.56,
    'dlo': 2821.6},

    4:{'nome': 'Carrefour ',
    'End': 'José de Souza Campos, 690 - Cambuí',
    'local': '''22°53'41.8"S 47°02'48.0"W ''',
    'dla': 1373.69,
    'dlo': 2822.8}
}

# BATERIAS DE CELULAR
bateriasCelular = {
    1:{'nome':'TIM - LOJA CAMPINAS',
    'End': 'Rua Albino José Barbosa Oliveira, 1340 - Barão Geraldo',
    'local':'''22°49'35.0"S 47°04'44.7"W''',
    'dla': 1369.58,
    'dlo': 2824.74}, 

    2:{'nome': 'Vivo ',
    'End': 'Dr. Pereira Lima, S/Nº, Lojas 27M/28M',
    'local': '''22°54'20.1"S 47°04'21.1"W ''',
    'dla': 1374.33,
    'dlo': 2824.35},

    3:{'nome': 'Carrefour ',
    'End': 'Cambuí- Rua Santa Cruz, 281',
    'local': '''22°53'38.8"S 47°03'29.7"W''',
    'dla': 1373.64,
    'dlo': 2823.49},

    4:{'nome': 'Vivo',
    'End': 'Unimart Shopping Av. John Boyd Dunlop, 350 ',
    'local': '''22°54'31.7"S 47°05'41.2"W''',
    'dla': 1374.52,
    'dlo': 2825.68}
}    

# GARRAFAS DE VIDRO
garrafasVidro = {
    1:{'nome':"Sam's Club",
    'End': 'Rod. Dom Pedro I, Km 132, S/Nº',
    'local':'''22°51'38.1"S 47°01'25.3"W''',
    'dla': 1371.63,
    'dlo': 2821.42},

    2:{'nome': 'Carrefour ',
    'End': 'Cambuí- Rua Santa Cruz, 281',
    'local': '''22°53'38.8"S 47°03'29.7"W''',
    'dla': 1373.65,
    'dlo': 2823.49},

    3:{'nome': 'Cooperativa São Bernardo – DLU  ',
    'End': 'Av. Prefeito Faria Lima, 630',
    'local': '''22°54'55.6"S 47°04'16.6"W''',
    'dla': 1374.93,
    'dlo': 2824.28},

    4:{'nome': 'Carrefour Cambuí',
    'End': 'Cambuí- Rua Santa Cruz, 281',
    'local': '''22°53'38.5"S 47°03'29.5"W''',
    'dla': 1373.64,
    'dlo': 2823.49}
}

# PAPELÃO
papelao = {
    1:{'nome':"Cooperativa São Bernardo – DLU ",
    'End': 'Av. Prefeito Faria Lima, 630',
    'local':'''22°54'55.6"S 47°04'16.6"W''',
    'dla': 1374.93,
    'dlo': 2824.28},

    2:{'nome': "Sam's Club",
    'End': 'Rod. Dom Pedro I, Km 132, S/Nº',
    'local': '''22°51'38.1"S 47°01'25.3"W''',
    'dla': 1371.63,
    'dlo': 2821.42},

    3:{'nome': 'Pão de Açúcar',
    'End': 'Itapura - Av. Barão de Itapura, 2233',
    'local': '''22°54'55.6"S 47°04'16.6"W''',
    'dla': 1374.93,
    'dlo': 2824.28},

    4:{'nome': 'Carrefour',
    'End': 'Nova Campinas - Avenida José de Souza Campos  ',
    'local': '''22°53'41.8"S 47°02'48.1"W ''',
    'dla': 1373.70,
    'dlo': 2822.80}
}

# METAIS E FERRAGENS
metaisFerra = {
    1:{'nome':"Cooperativa São Bernardo – DLU ",
    'End': 'Av. Prefeito Faria Lima, 630',
    'local':'''22°54'55.6"S 47°04'16.6"W''',
    'dla': 1374.93,
    'dlo': 2824.28},

    2:{'nome': "Sam's Club",
    'End': 'Rod. Dom Pedro I, Km 132, S/Nº',
    'local': '''22°51'38.1"S 47°01'25.3"W''',
    'dla': 1371.63,
    'dlo': 2821.42},

    3:{'nome': 'Pão de Açúcar',
    'End': 'Barão Geraldo-Rua Albino José Barbosa Oliveira, 1340',
    'local': '''22°49'35.0"S 47°04'44.7"W''',
    'dla': 1369.58,
    'dlo': 2824.74},

    4:{'nome': 'Cooperativa Bom Sucesso',
    'End': 'R. Engenheiro Calcagnolo, 6',
    'local': '''22°52'29.8"S 47°08'29.2"W''',
    'dla': 1372.5,
    'dlo': 2828.49}
}


# Fim variáveis dos lugares

# Funções
def dla():
    '''Calcula o dla da latitude'''
    dlaG = graus * 60
    dlaM = minu * 1
    dlaS = segun / 60
    dlaF = ( dlaG + dlaM + dlaS )
    return dlaF

def dlo():
    '''Calcula o dlo da longitude'''
    dloG = graus * 60
    dloM = minu * 1
    dloS = segun / 60
    dloF = ( dloG + dloM + dloS )
    return dloF
    

def menuDeOpcoes():
    '''Menu onde ficará as opções de reciclagem'''
    print('==================== SEJA BEM VINDO ====================')
    print('''Qual material você deseja encontrar o ponto próximo ?
    [ 1 ] Pilhas portáveis  [ 2 ] Bateria de celular
    [ 3 ] Garrafas de vidro [ 4 ] Papelão
    [ 5 ] Metais/Ferragens  [ 6 ] Sair''')
    material = 0 
    while True:
        try:
            if material < 1 or material > 6:
                print('Escolha uma opção de 1 a 6.')
                material = int(input('Opção: '))
            else:
                break
        except:
            print('Opção inválida.')
    print('=' * 56)
    return material

def refere():
    ''' referencia do material '''
    if material == 1:
        refer = pilharPortaveis.copy()
    elif material == 2:
        refer = bateriasCelular.copy()
    elif material == 3:
        refer = garrafasVidro.copy()
    elif material == 4:
        refer = papelao.copy()
    elif material == 5:
        refer = metaisFerra.copy()
    elif material == 6:
        refer = 0
    return refer

def menuDeOpcoes_2():
    '''Menu de ação'''
    print('========== O que deseja fazer agora ? ==========')
    print('''[ 1 ] Inserir um novo local  [ 2 ] Escolher um novo material
[ 3 ] Ver resultado e continuar  [ 4 ] Ver resultado e sair''')
    opcaoFinal = 0 
    while True:
        try:
            if opcaoFinal < 1 or opcaoFinal > 4:
                print('Escolha uma opção de 1 a 4.')
                opcaoFinal = int(input('Opção: '))
            else:
                break
        except:
            print('Opção inválida.')
    print('=' * 56)
    return opcaoFinal

def impressãoFinal():
    final = True
    while final:
        print('=' * 25)
        for i in range(1, 5):
            if refer[i]['dla'] >= dlaUser:
                dlaF = ( refer[i]['dla'] - dlaUser ) * 1.852
            else:
                dlaF = ( dlaUser - refer[i]['dla'] ) * 1.852

            if refer[i]['dlo'] >= dloUser:
                dloF = ( refer[i]['dlo'] - dloUser ) * 1.852
            else:
                dloF = ( dloUser - refer[i]['dlo'] ) * 1.852

            contaFinal = ((dlaF**2) + (dloF**2))**0.5
            refer[i]['km'] = contaFinal 

        print('ABAIXO ESTÁ A LISTA DOS MELHORES LUGARES PARA SUA REGIÃO')
        for p in range(1, 5):
            print('-' * 50)
            print('Nome: {}\n End: {}\n Coordenada: {}\n Distância: ~ {:.2f} km'.format(refer[p]['nome'], refer[p]['End'], refer[p]['local'], refer[p]['km']))
            sleep(1)
        final = False
    
# Fim das funções

coordenada = True
menu = True
menuDeAcao = True
opcaoFinal = refer = 0


# Módulos
from time import sleep # Importa o modulo que faz o programa 'dormir'

while True: # começo do programa
    while menu:
        material = menuDeOpcoes()
        refer = refere()
        menuDeAcao = True
        if refer == 0:
            coordenada = False
            menuDeAcao = False
            print('Saindo... Volte sempre!')
            opcaoFinal = 4
        menu = False

    ########## COORDENADA ##########
    while coordenada:
        print('Insira a sua coordenada agora.')

        while True: # Latitude
            graus = minu = segun = 0
            
            print('Digite a LATITUDE abaixo.')

            while True:  # Graus 
                try:
                    graus = int(input('Graus: '))
                    break
                except:
                    print('OPS! Parece que você digitou algo errado!')
                    print('=' * 26 )

            while True:  # Minutos
                try:
                    minu = int(input('Minutos: '))
                    break
                except:
                    print('OPS! Parece que você digitou algo errado!')
                    print('=' * 26 )

            while True:  # Segundos
                try:
                    segun = float(input('Segundos: '))
                    break
                except:
                    print('OPS! Parece que você digitou algo errado!')
                    print('=' * 26 )

            print(f"""A LATITUDE está correta ? 
            {graus}° {minu}" {segun}' """)

            correto = 0
            while True: # correção da coordenada
                try:
                    correto = int(input('A coordenada está correta ? 1 - Sim ou 2 - Não: '))
                    if correto == 1:
                        print('     Entendido!!')
                        break
                    elif correto == 2:
                        print('=' * 26)
                        break
                    else:
                        print('Apenas 1 ou 2.')
                except:
                    print('Responda apenas com 1 ou 2.')
            if correto == 1:
                break

        dlaUser = dla() 
        while True:
            correto = 'continuar'
            graus = minu = segun = 0
            print('Digite a LONGITUDE abaixo.')

            while True:  # Graus 
                try:
                    graus = int(input('Graus: '))
                    break
                except:
                    print('OPS! Parece que você digitou algo errado!')
                    print('=' * 26 )

            while True:  # Minutos
                try:
                    minu = int(input('Minutos: '))
                    break
                except:
                    print('OPS! Parece que você digitou algo errado!')
                    print('=' * 26 )

            while True:  # Segundos
                try:
                    segun = float(input('Segundos: '))
                    break
                except:
                    print('OPS! Parece que você digitou algo errado!')
                    print('=' * 26 )

            print(f"""A LONGITUDE está correta ? 
            {graus}° {minu}" {segun}' """)

            correto = 0
            while True: # correção da coordenada
                try:
                    correto = int(input('A coordenada está correta ? 1 - Sim ou 2 - Não: '))
                    if correto == 1:
                        print('     Entendido!!')
                        break
                    elif correto == 2:
                        print('=' * 26)
                        break
                    else:
                        print('Apenas 1 ou 2.')
                except:
                    print('Responda apenas com 1 ou 2.')
            if correto == 1:
                break
        dloUser = dlo()  
        coordenada = False
        menuDeAcao = True    
    ########## FIM COORDENADA ##########

    ########## MENU FINAL DE AÇÃO ##########
    while menuDeAcao:
        print('O que deseja fazer agora ?')
        opcaoFinal = menuDeOpcoes_2()
        if opcaoFinal == 1: # Inserir um novo local
            coordenada = True
            refer = 0
            print('Um momento...')
        elif opcaoFinal == 2: # Escolher um novo material
            menu = True
            print('Lembre-se, sua coordenada já está salva.')
        elif opcaoFinal == 3: # Sair
            print('Mostrando o resultado...')
            impressãoFinal()
            menuDeAcao = False
            final = True
            menu = True
            coordenada = True
        elif opcaoFinal == 4: # Sair
            impressãoFinal()
            print('=' * 26)
            print('Saindo... Esperamos você novamente.')
            print('=' * 26)
        menuDeAcao = False
    if opcaoFinal == 4: # Pega a opção do menu final
        break
    ########## FIM MENU FINAL DE AÇÃO ##########