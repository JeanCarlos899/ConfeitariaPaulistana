import PySimpleGUI as sg

from Scripts.data_list import DataList
from Scripts.insert_dados import InsertDados
from Scripts.finalize_order import FinalizeOrder
from Scripts.new_chart import NewChart
from Scripts.reports import Relatorios
from Scripts.delete_order import DeleteOrder

from Design.menu_principal import MenuPrincipal
from Design.nova_encomenda import NovaEncomenda
from Design.listar_encomendas import ListarEncomendas
from Design.baixa_encomenda import BaixaEncomenda
from Design.graficos import Graficos
from Design.relatorios import FrontRelatorio
from Design.deletar_encomenda import DeletarEncomenda


def buttons(on_off):
    if on_off == "on":
        menu["-NOVA_ENCOMENDA-"].update(disabled=False)
        menu["-LISTAR_ENCOMENDAS-"].update(disabled=False)
        menu["-DAR_BAIXA_ENCOMENDA-"].update(disabled=False)
        menu["-EDITAR_ENCOMENDA-"].update(disabled=False)
        menu["-GRAFICOS-"].update(disabled=False)
        menu["-RELATORIOS-"].update(disabled=False)
        menu["-DELETAR_ENCOMENDA-"].update(disabled=False)
        menu["-SAIR-"].update(disabled=False)
    else: 
        menu["-NOVA_ENCOMENDA-"].update(disabled=True)
        menu["-LISTAR_ENCOMENDAS-"].update(disabled=True)
        menu["-DAR_BAIXA_ENCOMENDA-"].update(disabled=True)
        menu["-EDITAR_ENCOMENDA-"].update(disabled=True)
        menu["-GRAFICOS-"].update(disabled=True)
        menu["-RELATORIOS-"].update(disabled=True)
        menu["-DELETAR_ENCOMENDA-"].update(disabled=True)
        menu["-SAIR-"].update(disabled=True)

####################INICIANDO JANELAS######################
menu, nova_encomenda = MenuPrincipal.menu_principal(), None
lista_encomenda, menu_encomenda = None, None
dar_baixa_encomenda, dados_cliente = None, None
salgadinhos, mais_informacoes = None, None
graficos, relatorios, deletar_encomenda = None, None, None

menu.maximize()

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
            buttons("off")
            continue
        elif evento == "-LISTAR_ENCOMENDAS-":
            menu_encomenda = ListarEncomendas.listar_encomendas("Pendente")
            buttons("off")
            continue
        elif evento == "-DAR_BAIXA_ENCOMENDA-":
            dar_baixa_encomenda = BaixaEncomenda.baixa_encomenda()
            buttons("off")
            continue
        elif evento == '-GRAFICOS-':
            graficos = Graficos.menu_graficos()
            buttons("off")
            continue
        elif evento == '-RELATORIOS-':
            relatorios = FrontRelatorio.menu_relatorios()
            buttons("off")
            continue
        elif evento == '-DELETAR_ENCOMENDA-':
            deletar_encomenda = DeletarEncomenda.deletar_encomenda("Pendente")
            buttons("off")
            continue
        
    ##########################################################################
    ###########################NOVA ENCOMENDA#################################
    ##########################################################################

    if (janela == nova_encomenda and evento == sg.WIN_CLOSED  
        or janela == nova_encomenda and evento == "-VOLTAR-"):
        nova_encomenda.hide()
        buttons("on")
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
        buttons("on")
        continue

    ##########################################################################
    ###########################LISTAR ENCOMENDAS##############################
    ##########################################################################

    if (janela == menu_encomenda and evento == sg.WIN_CLOSED 
        or janela == menu_encomenda and evento == "-VOLTAR-"):
        menu_encomenda.hide()
        buttons("on")
        continue

    if janela == menu_encomenda:
        status_concluido = valor["-STATUS_CONCLUIDO-"] 
        status_pendente = valor["-STATUS_PENDENTE-"]

    if janela == menu_encomenda and evento == "-FILTRAR-":
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
        index_da_lista = int(valor["-INDEX_ENCOMENDA-"][0])

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
        buttons("on")
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

    ##########################################################################
    ###########################GRAFICOS#######################################
    ##########################################################################

    if (janela == graficos and evento == sg.WIN_CLOSED 
        or janela == graficos and evento == '-VOLTAR-'):
        graficos.hide()
        buttons("on")

    if janela == graficos and evento == '-STATUS_PEDIDO-':
        NewChart.graficoPizza()
        continue

    if janela == graficos and evento == '-TIPO_BOLO-':
        NewChart.graficoTipoBolo()
        continue

    if janela == graficos and evento == '-TIPO_SALGADO-':
        NewChart.graficoTipoSalgados()
        continue

    if janela == graficos and evento == '-MENSAIS-':
        NewChart.graficoBarrasPedidos()
        continue

    ##########################################################################
    ###########################RELATÓRIOS#####################################
    ##########################################################################

    if (janela == relatorios and evento == sg.WIN_CLOSED 
        or janela == relatorios and evento == '-VOLTAR-'):
        relatorios.hide()
        buttons("on")
    
    if janela == relatorios and evento == '-PEDIDOS_ENTREGUES-':
        Relatorios.historico_pedidos_concluido()
        sg.popup("Relatório gerado com sucesso!")
        continue

    if janela == relatorios and evento == '-PEDIDOS_NAO_ENTREGUES-':
        Relatorios.historico_pedidos_naoentregues()
        sg.popup("Relatório gerado com sucesso!")
        continue

    if janela == relatorios and evento == '-PEDIDOS_PENDENTES-':
        Relatorios.pedidos_pendentes()
        sg.popup("Relatório gerado com sucesso!")
        continue

    if janela == relatorios and evento == '-TODOS_PEDIDOS-':
        Relatorios.historico_todos_pedidos()
        relatorios.hide()
        sg.popup("Relatório gerado com sucesso!")
        continue

    ##########################################################################
    ############################DELETAR ENCOMENDA#############################
    ##########################################################################

    if (janela == deletar_encomenda and evento == sg.WIN_CLOSED 
        or janela == deletar_encomenda and evento == "-VOLTAR-"):
        deletar_encomenda.hide()
        buttons("on")
    
    if janela == deletar_encomenda:
        status_concluido = valor["-STATUS_CONCLUIDO-"] 
        status_pendente = valor["-STATUS_PENDENTE-"]
    
    if janela == deletar_encomenda and evento == "-FILTRAR-":
        if status_concluido == True:
            lista_clientes = DataList("Concluído").get_dados_pedido_resumido()
            deletar_encomenda.close()
            deletar_encomenda = DeletarEncomenda.deletar_encomenda("Concluído")
            deletar_encomenda["-STATUS_CONCLUIDO-"].update(True)

        elif status_pendente == True:
            lista_clientes = DataList("Pendente").get_dados_pedido_resumido()
            deletar_encomenda.close()
            menu_encomenda = DeletarEncomenda.deletar_encomenda("Pendente")
            deletar_encomenda["-STATUS_PENDENTE-"].update(True)
        continue

    ##########################DELETAR ENCOMENDA###############################

    if janela == deletar_encomenda and evento == "-DELETAR_ENCOMENDA-":
        if status_pendente == True:
            lista_clientes = DataList("Pendente").get_dados_pedido_resumido()
        else:
            lista_clientes = DataList("Concluído").get_dados_pedido_resumido()
            
        index_encomenda = valor["-INDEX_ENCOMENDA-"]
        DeleteOrder(index_encomenda, lista_clientes).deletar_encomenda()
        deletar_encomenda["-DELETAR_ENCOMENDA-"].update(disabled=True)

        if status_concluido == True:
            deletar_encomenda.close()
            deletar_encomenda = DeletarEncomenda.deletar_encomenda("Concluído")
            deletar_encomenda["-STATUS_CONCLUIDO-"].update(True)
        elif status_pendente == True:
            deletar_encomenda.close()
            deletar_encomenda = DeletarEncomenda.deletar_encomenda("Pendente")
            deletar_encomenda["-STATUS_PENDENTE-"].update(True)
        continue