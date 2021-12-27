import PySimpleGUI as sg
from Scripts.insert_dados import InsertDados
from Scripts.price_end import PrecoFinal

from Design.menu_principal import MenuPrincipal
from Design.nova_encomenda import NovaEncomenda
from Design.listar_encomendas import ListarEncomendas
from Design.baixa_encomenda import BaixaEncomenda

menu, nova_encomenda, lista_encomenda = MenuPrincipal.menu_principal(), None, None
menu_encomenda, dar_baixa_encomenda, dados_cliente = None, None, None
popup_baixa, salgadinhos, mais_informacoes = None, None, None


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

        elif evento == 'Listar encomendas':
            menu_encomenda = ListarEncomendas.listar_encomendas("Pendente")

        elif evento == 'Dar baixa em encomenda':
            dar_baixa_encomenda = BaixaEncomenda.baixa_encomenda()

        elif evento == 'Sair':
            break
    ##########################################################################
    ##########################################################################
    ###########################NOVA ENCOMENDA#################################
    ##########################################################################
    ##########################################################################
    if janela == nova_encomenda and evento == sg.WIN_CLOSED or janela == nova_encomenda and evento == 'Voltar':
        nova_encomenda.hide()


    if janela == nova_encomenda and evento == 'Confirmar':
        InsertDados(
            str(valor["nome_cliente"]), 
            str(valor["data_entrega"]),
            str(valor["horario_entrega"]),
            int(valor["bolo_aniversario"]),
            int(valor["bolo_casamento"]),
            int(valor["qtd_mini"]),
            int(valor["qtd_normal"]),
            str(valor["info_complementares"])
        ).inserir_dados()

        sg.popup("Encomenda cadastrada com sucesso!")
        nova_encomenda.hide()

        
    ##########################################################################
    ##########################################################################
    ###########################LISTAR ENCOMENDAS##############################
    ##########################################################################
    ##########################################################################

    if janela == menu_encomenda and evento == sg.WIN_CLOSED or janela == menu_encomenda and evento == 'Voltar':
        menu_encomenda.hide()

    if janela == menu_encomenda and evento == 'Filtrar':
        status_pendente = valor["status_pendente"] #true or false
        status_concluido = valor["status_concluido"] #true or false

        if status_concluido == True:
            menu_encomenda.close()
            menu_encomenda = ListarEncomendas.listar_encomendas("Concluído")
            menu_encomenda["status_concluido"].update(True)
        elif status_pendente == True:
            menu_encomenda.close()
            menu_encomenda = ListarEncomendas.listar_encomendas("Pendente")
            menu_encomenda["status_pendente"].update(True)

    ##########################MAIS INFORMAÇÕES###############################
    if janela == menu_encomenda and evento == 'Mais informações':
        index_da_lista = valor["index_encomenda"]
        status_pendente = valor["status_pendente"] #true or false
        status_concluido = valor["status_concluido"] #true or false

        if status_concluido == True:
            lista_clientes = ListarEncomendas.valores_tabela("Concluído")
        elif status_pendente == True:
            lista_clientes = ListarEncomendas.valores_tabela("Pendente")
        
        index_da_lista = int(index_da_lista[0])

        mais_informacoes = ListarEncomendas.mais_informacoes(lista_clientes[index_da_lista], index_da_lista)
        menu_encomenda.hide()

    if janela == mais_informacoes and evento == sg.WIN_CLOSED or janela == mais_informacoes and evento == 'Voltar':
        mais_informacoes.hide()
        menu_encomenda.un_hide()


    ##########################################################################
    ##########################################################################
    ###########################BAIXA EM ENCOMENDA#############################
    ##########################################################################
    ##########################################################################

    if janela == dar_baixa_encomenda and evento == sg.WIN_CLOSED or janela == dar_baixa_encomenda and evento == 'Voltar':
        dar_baixa_encomenda.hide()

    
    if janela == dar_baixa_encomenda and evento == 'Confirmar':
        id = valor['id']
        kg_aniversario = valor['kg_bolo_aniversario']
        kg_casamento = valor['kg_bolo_casamento']

        preco_final = PrecoFinal(id, kg_aniversario, kg_casamento).modificar_status()

        dar_baixa_encomenda.hide()

        popup_baixa = BaixaEncomenda.popup_baixa(preco_final)

    if janela == popup_baixa and evento == sg.WIN_CLOSED or janela == popup_baixa and evento == 'Ok':
        popup_baixa.hide()


