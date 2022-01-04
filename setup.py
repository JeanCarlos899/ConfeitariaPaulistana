import os
import sys

try:
    import PySimpleGUI as sg

    from Scripts.data_list import DataList
    from Scripts.insert_dados import InsertDados
    from Scripts.finalize_order import FinalizeOrder
    from Scripts.new_chart import NewChart
    from Scripts.reports import Relatorios
    from Scripts.delete_order import DeleteOrder
    from Scripts.edit_order import EditOrder

    from Design.menu_principal import MenuPrincipal
    from Design.nova_encomenda import NovaEncomenda
    from Design.listar_encomendas import ListarEncomendas
    from Design.baixa_encomenda import BaixaEncomenda
    from Design.graficos import Graficos
    from Design.relatorios import FrontRelatorio
    from Design.deletar_encomenda import DeletarEncomenda
    from Design.editar_encomenda import EditarEncomenda
    from Design.faturamento import Faturamento
    from Scripts.revenues import Revenues
    from Scripts.pronfit_in_the_month import Lucromensal

except:
    print("Instalando bibliotecas necessárias...")
    os.system("requirements.bat")
    print("Bibliotecas instaladas com sucesso!\nReabra o programa.")
    sys.exit()

def buttons(on_off):
    keys = [
        "-NOVA_ENCOMENDA-", 
        "-LISTAR_ENCOMENDAS-",
        "-DAR_BAIXA_ENCOMENDA-",
        "-EDITAR_ENCOMENDA-",
        "-GRAFICOS-",
        "-RELATORIOS-",
        "-FATURAMENTO-",
        "-DELETAR_ENCOMENDA-",
        "-LUCRO_MENSAL-",
        "-SAIR-"
        ]

    if on_off == "on":
        for button in keys:
            menu[button].update(disabled=False)
    else: 
        for button in keys:
            menu[button].update(disabled=True)

####################INICIANDO JANELAS######################
menu, nova_encomenda = MenuPrincipal.menu_principal(), None
lista_encomenda, menu_encomenda = None, None
dar_baixa_encomenda, dados_cliente = None, None
salgadinhos, mais_informacoes = None, None
graficos, relatorios, deletar_encomenda = None, None, None
editar_encomenda, faturamento = None, None
lucro_do_mes = None

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
            nova_encomenda = NovaEncomenda.nova_encomenda("Nova Encomenda")
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
        elif evento == "-GRAFICOS-":
            graficos = Graficos.menu_graficos()
            buttons("off")
            continue
        elif evento == "-RELATORIOS-":
            relatorios = FrontRelatorio.menu_relatorios()
            buttons("off")
            continue
        elif evento == "-FATURAMENTO-":
            faturamento = Faturamento.faturamento()
            buttons("off")
            continue
        elif evento == "-EDITAR_ENCOMENDA-":
            editar_encomenda = EditarEncomenda.listar_encomendas("Pendente")
            buttons("off")
            continue
        elif evento == "-DELETAR_ENCOMENDA-":
            deletar_encomenda = DeletarEncomenda.deletar_encomenda("Pendente")
            buttons("off")
            continue
        elif evento == "-LUCRO_MENSAL-":
            lucro_do_mes = Lucromensal.lucro()
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
        verificacao = InsertDados([
            str(valor["-NOME_CLIENTE-"]), 
            str(valor["-DATA_ENTREGA-"]), 
            str(valor["-HORA_ENTREGA-"]), 
            int(valor["-BOLO_ANIVERSARIO-"]),
            int(valor["-BOLO_CASAMENTO-"]), 
            int(valor["-QTD_MINI-"]), 
            int(valor["-QTD_NORMAL-"]), 
            str(valor["-INFO_COMPLEMENTARES-"]) 
        ]).inserir_dados()

        if verificacao == True:
            sg.popup("Encomenda cadastrada com sucesso!")
            nova_encomenda.hide()
            buttons("on")
            continue
        elif verificacao == False:
            sg.popup("Erro ao cadastrar encomenda!")

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
            menu_encomenda["-INDEX_ENCOMENDA-"].update(
                values=DataList("Concluído").get_dados_pedido_resumido()
                )
            menu_encomenda["-STATUS_CONCLUIDO-"].update(True)
        elif status_pendente == True:
            menu_encomenda["-INDEX_ENCOMENDA-"].update(
                values=DataList("Pendente").get_dados_pedido_resumido()
                )
            menu_encomenda["-STATUS_PENDENTE-"].update(True)
        continue

    ##########################MAIS INFORMACOES###############################

    if janela == menu_encomenda and evento == "-MAIS_INFORMACOES-":
        try:
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
        except:
            sg.popup("Selecione uma encomenda para mais informações!")
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
        try:
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
        except:
            sg.popup("Selecione uma encomenda para finalizar!")
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
        or janela == graficos and evento == "-VOLTAR-"):
        graficos.hide()
        buttons("on")

    if janela == graficos and evento == "-STATUS_PEDIDO-":
        NewChart.graficoPizza()
        continue

    if janela == graficos and evento == "-TIPO_BOLO-":
        NewChart.graficoTipoBolo()
        continue

    if janela == graficos and evento == "-TIPO_SALGADO-":
        NewChart.graficoTipoSalgados()
        continue

    if janela == graficos and evento == "-MENSAIS-":
        NewChart.graficoBarrasPedidos()
        continue

    if janela == graficos and evento == "-LUCRO_MENSAL-":
        NewChart.graficoganho()
        continue

    if janela == graficos and evento == "-LUCRO_POR_TIPO_DE_FESTAS-":
        NewChart.lucroporfesta()
        continue

    ##########################################################################
    ###########################RELATÓRIOS#####################################
    ##########################################################################

    if (janela == relatorios and evento == sg.WIN_CLOSED 
        or janela == relatorios and evento == "-VOLTAR-"):
        relatorios.hide()
        buttons("on")
    
    if janela == relatorios and evento == "-PEDIDOS_ENTREGUES-":
        Relatorios.historico_pedidos_concluido()
        sg.popup("Relatório gerado com sucesso!")
        continue

    if janela == relatorios and evento == "-PEDIDOS_NAO_ENTREGUES-":
        Relatorios.historico_pedidos_naoentregues()
        sg.popup("Relatório gerado com sucesso!")
        continue

    if janela == relatorios and evento == "-PEDIDOS_PENDENTES-":
        Relatorios.pedidos_pendentes()
        sg.popup("Relatório gerado com sucesso!")
        continue

    if janela == relatorios and evento == "-TODOS_PEDIDOS-":
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
            deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                values=DataList("Concluído").get_dados_pedido_resumido()
                )
            deletar_encomenda["-STATUS_CONCLUIDO-"].update(True)

        elif status_pendente == True:
            lista_clientes = DataList("Pendente").get_dados_pedido_resumido()
            deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                values=DataList("Pendente").get_dados_pedido_resumido()
                )
            deletar_encomenda["-STATUS_CONCLUIDO-"].update(False)
        continue

    ##########################DELETAR ENCOMENDA###############################

    if janela == deletar_encomenda and evento == "-DELETAR_ENCOMENDA-":
        try:
            if status_pendente == True:
                lista_clientes = DataList("Pendente").get_dados_pedido_resumido()
            elif status_concluido == True:
                lista_clientes = DataList("Concluído").get_dados_pedido_resumido()
                
            index_encomenda = valor["-INDEX_ENCOMENDA-"]
            DeleteOrder(index_encomenda, lista_clientes).deletar_encomenda()

            if status_concluido == True:
                deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=DataList("Concluído").get_dados_pedido_resumido()
                    )
                deletar_encomenda["-STATUS_CONCLUIDO-"].update(True)

            elif status_pendente == True:
                deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=DataList("Pendente").get_dados_pedido_resumido()
                    )
                deletar_encomenda["-STATUS_CONCLUIDO-"].update(False)
            continue
        except:
            sg.popup("Nenhuma encomenda selecionada!")
            continue

    ##########################################################################
    ###########################EDITAR ENCOMENDAS##############################
    ##########################################################################

    if (janela == editar_encomenda and evento == sg.WIN_CLOSED 
        or janela == editar_encomenda and evento == "-VOLTAR-"):
        editar_encomenda.hide()
        buttons("on")
        continue

    if janela == editar_encomenda:
        try:
            status_concluido = valor["-STATUS_CONCLUIDO-"] 
            status_pendente = valor["-STATUS_PENDENTE-"]
        except:
            pass

    if janela == editar_encomenda and evento == "-FILTRAR-":
        if status_concluido == True:
            editar_encomenda["-INDEX_ENCOMENDA-"].update(
                values=DataList("Concluído").get_dados_pedido_resumido()
                )
            editar_encomenda["-STATUS_CONCLUIDO-"].update(True)
        elif status_pendente == True:
            editar_encomenda["-INDEX_ENCOMENDA-"].update(
                values=DataList("Pendente").get_dados_pedido_resumido()
                )
            editar_encomenda["-STATUS_PENDENTE-"].update(True)
        continue

    ###############################EDITAR ENCOMENDA###########################

    if janela == editar_encomenda and evento == "-EDITAR-":
        try:
            index_encomenda = valor["-INDEX_ENCOMENDA-"]
            if status_concluido == True:
                status = "Concluído"
                lista_clientes = DataList("Concluído").get_dados_pedido_resumido()
                info_encomenda = DataList("Concluído").get_dados_pedido(False)
                msg = DataList("Concluído").get_dados_pedido(True)
            else:
                status = "Pendente"
                lista_clientes = DataList("Pendente").get_dados_pedido_resumido()
                info_encomenda = DataList("Pendente").get_dados_pedido(False)
                msg = DataList("Pendente").get_dados_pedido(True)
            
            editar_encomenda.hide()
            editar_encomenda = NovaEncomenda.nova_encomenda("Editar Encomenda")

            keys = [
                "-NOME_CLIENTE-",
                "-DATA_ENTREGA-",
                "-HORA_ENTREGA-",
                "-BOLO_ANIVERSARIO-",
                "-BOLO_CASAMENTO-",
                "-QTD_MINI-",
                "-QTD_NORMAL-",
                ]
            keys_info_clientes = keys[0:3]
            keys_info_encomenda = keys[3:7]

            for key in range(len(keys_info_clientes)):
                editar_encomenda[keys_info_clientes[key]].update(
                    lista_clientes[index_encomenda[0]][key+2]
                    )
            for key in range(len(keys_info_encomenda)):
                editar_encomenda[keys_info_encomenda[key]].update(
                    info_encomenda[index_encomenda[0]][key]
                    )
            editar_encomenda["-INFO_COMPLEMENTARES-"].update(msg[0])
            continue
        except:
            editar_encomenda.close()
            editar_encomenda = EditarEncomenda.listar_encomendas("Pendente")
            sg.popup("Nenhuma encomenda selecionada!")
            continue

    if janela == editar_encomenda and evento == "-CONFIRMAR-":
        try:
            verificacao = EditOrder(
                index_encomenda, lista_clientes, 
                [
                    str(valor["-NOME_CLIENTE-"]), 
                    str(valor["-DATA_ENTREGA-"]), 
                    str(valor["-HORA_ENTREGA-"]),
                    int(valor["-BOLO_ANIVERSARIO-"]), 
                    int(valor["-BOLO_CASAMENTO-"]),
                    int(valor["-QTD_MINI-"]), 
                    int(valor["-QTD_NORMAL-"]), 
                    str(valor["-INFO_COMPLEMENTARES-"]), 
                ], status).editar_encomenda()
            if verificacao == True:
                sg.popup("Encomenda editada com sucesso!")
                editar_encomenda.close()
                buttons("on")
                continue
            else:
                sg.popup("Erro ao editar encomenda!")
                continue
        except:
            sg.popup("Nenhuma encomenda selecionada!")
            continue
    
    ##########################################################################
    ###############################FATURAMENTO################################
    ##########################################################################

    if (janela == faturamento and evento == sg.WIN_CLOSED 
        or janela == faturamento and evento == "-VOLTAR-"):
        faturamento.close()
        buttons("on")
        continue

    if janela == faturamento and evento == "-FILTRAR-":
        data_inicial = valor["-DATA_INICIAL-"]
        data_final = valor["-DATA_FINAL-"]
        
        valor = Revenues(data_inicial, data_final).get_value()
        faturamento["-VALOR_FATURAMENTO-"].update(valor)

        
    ##########################################################################
    ###############################Lucro do mês###############################
    ##########################################################################

    if (janela == lucro_do_mes and evento == sg.WIN_CLOSED 
        or janela == lucro_do_mes and evento == "-EXIT-"):
        lucro_do_mes.hide()
        buttons("on")
        continue
    