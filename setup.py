import PySimpleGUI as sg

from Scripts.data_list import DataList
from Scripts.insert_dados import InsertDados
<<<<<<< HEAD
from Scripts.new_chart import NewChart
from Scripts.price_end import PrecoFinal
=======
from Scripts.finalize_order import FinalizeOrder
>>>>>>> 8fba3c0d0e176f0c78f04865d1978c0cfdfa8d36

from Design.menu_principal import MenuPrincipal
from Design.nova_encomenda import NovaEncomenda
from Design.listar_encomendas import ListarEncomendas
from Design.baixa_encomenda import BaixaEncomenda

<<<<<<< HEAD
menu, nova_encomenda, lista_encomenda, graficos, relatorios = MenuPrincipal.menu_principal(), None, None, None, None
menu_encomenda, dar_baixa_encomenda, dados_cliente = None, None, None
popup_baixa, salgadinhos, mais_informacoes = None, None, None

from Design.graficos import Graficos

=======
####################INICIANDO JANELAS######################
menu, nova_encomenda = MenuPrincipal.menu_principal(), None
lista_encomenda, menu_encomenda = None, None
dar_baixa_encomenda, dados_cliente = None, None
salgadinhos, mais_informacoes = None, None
>>>>>>> 8fba3c0d0e176f0c78f04865d1978c0cfdfa8d36

while True:
    
    # Leitura de todas as janelas abertas
    janela, evento, valor = sg.read_all_windows() 

    ##########################################################################
    ###########################JANELA PRINCIPAL###############################
    ##########################################################################
    
    if janela == menu and evento == sg.WIN_CLOSED:
        break

    if janela == menu:
        if evento == "-SAIR-":
            break
        elif evento == "-NOVA_ENCOMENDA-":
            nova_encomenda = NovaEncomenda.nova_encomenda()
            continue
        elif evento == "-LISTAR_ENCOMENDAS-":
            menu_encomenda = ListarEncomendas.listar_encomendas("Pendente")
            continue
        elif evento == "-DAR_BAIXA_ENCOMENDA-":
            dar_baixa_encomenda = BaixaEncomenda.baixa_encomenda()
<<<<<<< HEAD

        elif evento == 'graficos':
            graficos = Graficos.menu_graficos()

        # elif evento == 'relatorios':
        #     relatorios = FrontRelatorio.menu_relatorios()

        elif evento == 'Sair':
            break
    ##########################################################################
=======
            continue
 
>>>>>>> 8fba3c0d0e176f0c78f04865d1978c0cfdfa8d36
    ##########################################################################
    ###########################NOVA ENCOMENDA#################################
    ##########################################################################

    if (janela == nova_encomenda and evento == sg.WIN_CLOSED  
        or janela == nova_encomenda and evento == "-VOLTAR-"):
        nova_encomenda.hide()
        continue

    if janela == nova_encomenda and evento == "-CONFIRMAR-":
        InsertDados(
            str(valor["-NOME_CLIENTE-"]), 
            str(valor["-DATA_ENTREGA-"]),
            str(valor["-HORA_ENTREGA-"]),
            int(valor["-BOLO_ANIVERSARIO-"]),
            int(valor["-BOLO_CASAMENTO-"]),
            int(valor["-QTD_MINI-"]),
            int(valor["-QTD_NORMAL-"]),
            str(valor["-INFO_COMPLEMENTARES-"])
            ).inserir_dados()

        sg.popup("Encomenda cadastrada com sucesso!")
        nova_encomenda.hide()
        continue

    ##########################################################################
    ###########################LISTAR ENCOMENDAS##############################
    ##########################################################################

    if (janela == menu_encomenda and evento == sg.WIN_CLOSED 
        or janela == menu_encomenda and evento == "-VOLTAR-"):
        menu_encomenda.hide()
        continue

    if janela == menu_encomenda and evento == "-FILTRAR-":
        status_concluido = valor["-STATUS_CONCLUIDO-"] 
        status_pendente = valor["-STATUS_PENDENTE-"]

        if status_concluido == True:
            menu_encomenda.close()
            menu_encomenda = ListarEncomendas.listar_encomendas("Concluído")
            menu_encomenda["-STATUS_CONCLUIDO-"].update(True)
        elif status_pendente == True:
            menu_encomenda.close()
            menu_encomenda = ListarEncomendas.listar_encomendas("Pendente")
            menu_encomenda["-STATUS_PENDENTE-"].update(True)
        continue

    ##########################MAIS INFORMACOES###############################

    if janela == menu_encomenda and evento == "-MAIS_INFORMACOES-":
        index_da_lista = valor["-INDEX_ENCOMENDA-"]
        status_pendente = valor["-STATUS_PENDENTE-"] #true or false
        status_concluido = valor["-STATUS_CONCLUIDO-"] #true or false

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
        continue

    if (janela == mais_informacoes and evento == sg.WIN_CLOSED 
        or janela == mais_informacoes and evento == "-VOLTAR-"):
        mais_informacoes.hide()
        menu_encomenda.un_hide()
        continue

    ##########################################################################
    ###########################BAIXA EM ENCOMENDA#############################
    ##########################################################################

    if (janela == dar_baixa_encomenda and evento == sg.WIN_CLOSED 
        or janela == dar_baixa_encomenda and evento == "-VOLTAR-"):
        dar_baixa_encomenda.hide()
<<<<<<< HEAD

    
    if janela == dar_baixa_encomenda and evento == 'Confirmar':
        id = valor['id']
        kg_aniversario = valor['kg_bolo_aniversario']
        kg_casamento = valor['kg_bolo_casamento']

        preco_final = PrecoFinal(id, kg_aniversario, kg_casamento).modificar_status()

        dar_baixa_encomenda.hide()

        popup_baixa = BaixaEncomenda.popup_baixa(preco_final)

    if janela == popup_baixa and evento == sg.WIN_CLOSED or janela == popup_baixa and evento == 'Ok':
        popup_baixa.hide()


    ##########################################################################
    ##########################################################################
    ###########################GRAFICOS#######################################
    ##########################################################################
    ##########################################################################



    if janela == graficos and evento == sg.WIN_CLOSED or janela == graficos and evento == 'Voltar':
        graficos.hide()
        graficos.un_hide()

    if janela == graficos and evento == '-STATUS_PEDIDO-':
        NewChart.graficoPizza()
        graficos.hide()
        continue

    if janela == graficos and evento == '-TIPO_BOLO-':
        NewChart.graficoTipoBolo()
        graficos.hide()
        continue
    if janela == graficos and evento == '-TIPO_SALGADO-':
        NewChart.graficoTipoSalgados()
        graficos.hide()
        continue

    if janela == graficos and evento == '-MENSAIS-':
        NewChart.graficoBarrasPedidos()
        graficos.hide()
        continue

    if janela == graficos and evento == '-SAIR-':
        graficos.close()

    ##########################################################################
    ##########################################################################
    ###########################RELATORIO#####################################
    ##########################################################################
    ##########################################################################


 
=======
        continue

    if janela == dar_baixa_encomenda and evento == "-FINALIZAR_ENCOMENDA-":
        index_encomenda = valor["-TABLE_LISTAR_ENCOMENDA-"]
        kg_aniversario = valor["-BOLO_ANIVERSARIO-"]
        kg_casamento = valor["-BOLO_CASAMENTO-"]
        lista_encomenda = DataList("Pendente").get_dados_pedido_resumido()

        preco_final = FinalizeOrder(
            lista_encomenda, index_encomenda, 
            kg_aniversario, kg_casamento
            ).get_preco_final()

        dar_baixa_encomenda["-VALOR_FINAL-"].update("R$" + str(preco_final))
        dar_baixa_encomenda["-FINALIZAR_ENCOMENDA-"].update(disabled=True)
        continue

    if janela == dar_baixa_encomenda and evento == "-ATUALIZAR_LISTA-":
        dar_baixa_encomenda["-TABLE_LISTAR_ENCOMENDA-"].update(
            DataList("Pendente").get_dados_pedido_resumido()
            )

        dar_baixa_encomenda["-FINALIZAR_ENCOMENDA-"].update(disabled=False)
        dar_baixa_encomenda["-VALOR_FINAL-"].update("R$0,00")
        dar_baixa_encomenda["-BOLO_ANIVERSARIO-"].update(0)
        dar_baixa_encomenda["-BOLO_CASAMENTO-"].update(0)
        continue
>>>>>>> 8fba3c0d0e176f0c78f04865d1978c0cfdfa8d36
