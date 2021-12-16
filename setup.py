import PySimpleGUI as sg
from Scripts.windows import Windows 
from Scripts.insert_dados import InsertDados

menu, nova_encomenda, listar_encomendas, dar_baixa_encomenda, dados_cliente = Windows.janela_principal(), None, None, None, None
tipo_bolo = 0

while True:

    janela, evento, valor = sg.read_all_windows()

    # INSERÇÃO DE CADASTROS DE CLIENTES

    # janela principal
    if janela == menu and evento == sg.WIN_CLOSED:
        break
    if janela == menu:
        if evento == 'Nova encomenda':
            nova_encomenda = Windows.janela_nova_encomenda()
            menu.hide()
        elif evento == 'Listar encomendas':
            listar_encomendas = Windows.janela_listar_encomendas()
            menu.hide()
        elif evento == 'Dar baixa encomenda':
            dar_baixa_encomenda = Windows.janela_baixa_encomenda()
            menu.hide()
        elif evento == 'Sair':
            break
    
    # janela de nova encomenda
    if janela == nova_encomenda and evento == sg.WIN_CLOSED or janela == nova_encomenda and evento == 'Voltar':
        nova_encomenda.hide()
        menu.un_hide()

    if janela == nova_encomenda and evento == 'Confirmar':
        if valor['bolo_aniversario']:
            tipo_bolo = 1
            nova_encomenda.hide()
            dados_cliente = Windows.janela_dados_cliente()
        elif valor['bolo_casamento']:
            tipo_bolo = 2
            nova_encomenda.hide()
            dados_cliente = Windows.janela_dados_cliente()

    # janela de dados do cliente e inserir dados
    if janela == dados_cliente and evento == sg.WIN_CLOSED or janela == dados_cliente and evento == 'Voltar':
        dados_cliente.hide()
        menu.un_hide()
        
    if janela == dados_cliente and evento == 'Confirmar':
        if tipo_bolo == 1:
            valor_bolo = float(valor["peso"]) * 5
            InsertDados(valor_bolo, valor["data_entrega"], valor["nome_cliente"]).inserir_dados()
            sg.popup("Encomenda cadastrada com sucesso!")
            dados_cliente.hide()
            menu.un_hide()
            
        if tipo_bolo == 2:
            valor_bolo = float(valor["peso"]) * 10
            InsertDados(valor_bolo, valor["data_entrega"], valor["nome_cliente"]).inserir_dados()
            sg.popup("Encomenda cadastrada com sucesso!")
            dados_cliente.hide()
            menu.un_hide()
            
    # LISTAR ENCOMENDAS
    if janela == listar_encomendas and evento == sg.WIN_CLOSED or janela == listar_encomendas and evento == 'Voltar':
        listar_encomendas.hide()
        menu.un_hide()

    # DAR BAIXA EM UMA ENCOMENDA