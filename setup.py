import PySimpleGUI as sg
from openpyxl.reader.excel import load_workbook

from Scripts.insert_dados import InsertDados
from Scripts.new_index import get_new_index
from Scripts.get_type_bolo import GetTypeBolo

from Design.menu_principal import MenuPrincipal
from Design.nova_encomenda import NovaEncomenda
from Design.listar_encomendas import ListarEncomendas
from Design.baixa_encomenda import BaixaEncomenda

menu, nova_encomenda = MenuPrincipal.menu_principal(), None
listar_encomendas, dar_baixa_encomenda, dados_cliente = None, None, None
confirmar_baixa, listar_encomendas_atalho, salgadinhos = None, None, None

tipo_bolo = 0

while True:
    janela, evento, valor = sg.read_all_windows()

    ##########################################################################
    ##########################################################################
    ###########################JANELA PRINCIPAL###############################
    ##########################################################################
    ##########################################################################

    if janela == menu and evento == sg.WIN_CLOSED:
        break

    if janela == menu:
        if evento == 'Nova encomenda':
            nova_encomenda = NovaEncomenda.nova_encomenda()
            menu.hide()
        elif evento == 'Listar encomendas':
            listar_encomendas = ListarEncomendas.listar_encomendas()
            menu.hide()
        elif evento == 'Dar baixa em encomenda':
            dar_baixa_encomenda = BaixaEncomenda.baixa_encomenda()
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
            dados_cliente = NovaEncomenda.dados_encomenda()
        elif valor['bolo_casamento']:
            tipo_bolo = 2
            nova_encomenda.hide()
            dados_cliente = NovaEncomenda.dados_encomenda()

    if janela == nova_encomenda and evento == "Confirmar":
        if valor['salgadinhos']:
            salgadinhos = NovaEncomenda.salgadinhos()
    
    # janela de salgadinhos
    if janela == salgadinhos and evento == sg.WIN_CLOSED or janela == salgadinhos and evento == 'Voltar':
        salgadinhos.hide()
        nova_encomenda.un_hide()

    # janela de dados do cliente e inserir dados
    if janela == dados_cliente and evento == sg.WIN_CLOSED or janela == dados_cliente and evento == 'Voltar':
        dados_cliente.hide()
        nova_encomenda.un_hide()
        
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
            
    ##########################################################################
    ##########################################################################
    ###########################LISTAR ENCOMENDAS##############################
    ##########################################################################
    ##########################################################################

    if janela == listar_encomendas and evento == sg.WIN_CLOSED or janela == listar_encomendas and evento == 'Voltar':
        listar_encomendas.hide()
        menu.un_hide()

    ##########################################################################
    ##########################################################################
    ###########################BAIXA EM ENCOMENDA#############################
    ##########################################################################
    ##########################################################################

    if janela == dar_baixa_encomenda and evento == sg.WIN_CLOSED or janela == dar_baixa_encomenda and evento == 'Voltar':
        dar_baixa_encomenda.hide()
        menu.un_hide()

    if janela == dar_baixa_encomenda and evento == "Confirmar":
        planilha = load_workbook("dados.xlsx")
        planilha_ativa = planilha.active

        index_encomenda = int(valor["numero_encomenda"]) 
        peso_final = valor["peso_final"]
        tipo_bolo = GetTypeBolo(index_encomenda).return_type_bolo()
        
        if tipo_bolo == "Aniversário":
            valor_bolo = float(peso_final) * 5
        elif tipo_bolo == "Casamento":
            valor_bolo = float(peso_final) * 10

        confirmar_baixa = BaixaEncomenda.confirmar_baixa(valor_bolo)
    
    # Atalho para ver as encomendas
    if janela == dar_baixa_encomenda and evento == "Listar encomendas":
        listar_encomendas_atalho = ListarEncomendas.listar_encomendas()
        dar_baixa_encomenda.hide()
        
    if janela == listar_encomendas_atalho and evento == sg.WIN_CLOSED or janela == listar_encomendas_atalho and evento == 'Voltar':
        listar_encomendas.hide()
        dar_baixa_encomenda.un_hide()

    # confirmar baixa
    if janela == confirmar_baixa and evento == sg.WIN_CLOSED or janela == confirmar_baixa and evento == 'Não':
        confirmar_baixa.hide()
        menu.un_hide()

    if janela == confirmar_baixa and evento == 'Sim':
        sg.popup(f"Encomenda {index_encomenda} baixada com sucesso!")
        planilha_ativa.delete_rows(index_encomenda + 1)
        planilha.save("dados.xlsx")

        get_new_index()
        confirmar_baixa.hide()
        menu.un_hide()