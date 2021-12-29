import PySimpleGUI as sg
from Scripts.data_list import DataList
from Scripts.insert_dados import InsertDados
from Scripts.finalize_order import FinalizeOrder

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

        index_da_lista = int(index_da_lista[0])

        if status_concluido == True:
            lista_clientes = DataList("Concluído").get_dados_pedido_resumido()
            mais_informacoes = ListarEncomendas.mais_informacoes(
                "Concluído", lista_clientes[index_da_lista], index_da_lista
                )
            menu_encomenda.hide()

        if status_pendente == True:
            lista_clientes = DataList("Pendente").get_dados_pedido_resumido()
            mais_informacoes = ListarEncomendas.mais_informacoes(
                "Pendente", lista_clientes[index_da_lista], index_da_lista
                )
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

    if janela == dar_baixa_encomenda and evento == 'Finalizar encomenda':
        index_encomenda = valor["-TABLE_LISTAR_ENCOMENDA-"]
        kg_aniversario = valor['bolo_aniversario']
        kg_casamento = valor['bolo_casamento']
        lista_encomenda = DataList("Pendente").get_dados_pedido_resumido()

        preco_final = FinalizeOrder(lista_encomenda, index_encomenda, kg_aniversario, kg_casamento).get_preco_final()

        dar_baixa_encomenda["-VALOR_FINAL-"].update("R$" + str(preco_final))
        dar_baixa_encomenda["Finalizar encomenda"].update(disabled=True)
    if janela == dar_baixa_encomenda and evento == "Atualizar lista":
        dar_baixa_encomenda["-TABLE_LISTAR_ENCOMENDA-"].update(
            DataList("Pendente").get_dados_pedido_resumido()
        )
        dar_baixa_encomenda["Finalizar encomenda"].update(disabled=False)



