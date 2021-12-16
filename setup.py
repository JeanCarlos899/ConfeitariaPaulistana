import PySimpleGUI as sg
from openpyxl.reader.excel import load_workbook
from Scripts.windows import Windows 
from Scripts.insert_dados import InsertDados
from Scripts.new_index import get_new_index
from Scripts.get_type_bolo import get_type_bolo

menu, nova_encomenda, listar_encomendas, dar_baixa_encomenda, dados_cliente, confirmar_baixa, listar_encomendas_atalho = Windows.janela_principal(), None, None, None, None, None, None
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
        elif evento == 'Dar baixa em encomenda':
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
            InsertDados(valor_bolo, valor["data_entrega"], valor["nome_cliente"], tipo_bolo).inserir_dados()
            sg.popup("Encomenda cadastrada com sucesso!")
            dados_cliente.hide()
            menu.un_hide()
            
        if tipo_bolo == 2:
            valor_bolo = float(valor["peso"]) * 10
            InsertDados(valor_bolo, valor["data_entrega"], valor["nome_cliente"], tipo_bolo).inserir_dados()
            sg.popup("Encomenda cadastrada com sucesso!")
            dados_cliente.hide()
            menu.un_hide()
            
    # LISTAR ENCOMENDAS
    if janela == listar_encomendas and evento == sg.WIN_CLOSED or janela == listar_encomendas and evento == 'Voltar':
        listar_encomendas.hide()
        menu.un_hide()

    # DAR BAIXA EM UMA ENCOMENDA
    if janela == dar_baixa_encomenda and evento == sg.WIN_CLOSED or janela == dar_baixa_encomenda and evento == 'Voltar':
        dar_baixa_encomenda.hide()
        menu.un_hide()

    if janela == dar_baixa_encomenda and evento == "Confirmar":
        planilha = load_workbook("dados.xlsx")
        planilha_ativa = planilha.active

        index_encomenda = int(valor["numero_encomenda"]) + 1
        peso_final = valor["peso_final"]
        tipo_bolo = get_type_bolo(index_encomenda)
        
        if tipo_bolo == "Aniversário":
            valor_bolo = float(peso_final) * 5
        elif tipo_bolo == "Casamento":
            valor_bolo = float(peso_final) * 10

        confirmar_baixa = Windows.janela_confirmar_baixa(valor_bolo)
    
    if janela == dar_baixa_encomenda and evento == "Listar encomendas":
        listar_encomendas_atalho = Windows.janela_listar_encomendas()
        dar_baixa_encomenda.hide()
        
    if janela == listar_encomendas_atalho and evento == sg.WIN_CLOSED or janela == listar_encomendas_atalho and evento == 'Voltar':
        listar_encomendas.hide()
        dar_baixa_encomenda.un_hide()

    # confirmar baixa
    if janela == confirmar_baixa and evento == sg.WIN_CLOSED or janela == confirmar_baixa and evento == 'Não':
        confirmar_baixa.hide()
        menu.un_hide()

    if janela == confirmar_baixa and evento == 'Sim':
        sg.popup(f"Encomenda {index_encomenda - 1} baixada com sucesso!")
        planilha_ativa.delete_rows(index_encomenda)
        planilha.save("dados.xlsx")

        get_new_index()
        confirmar_baixa.hide()
        menu.un_hide()