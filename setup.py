import os
import sys

try:
    import PySimpleGUI as sg

    from Scripts.insert_dados import InsertDados
    from Scripts.finalize_order import FinalizeOrder
    from Scripts.new_chart import NewChart
    from Scripts.reports import Relatorios
    from Scripts.edit_order import EditDados
    from Scripts.sqlite import SQLite

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
    from Design.lucro_mes import Lucromensal
    from Scripts.pronfit_in_the_month import Gasto
    
except ImportError:
    os.system("pip3 install -r requirements.txt")
    print("Bibliotecas instaladas com sucesso!")
    print("Reabra o programa.")
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
        msg = InsertDados([
            str(valor["-NOME_CLIENTE-"]), 
            str(valor["-DATA_ENTREGA-"]), 
            str(valor["-HORA_ENTREGA-"]), 
            int(valor["-BOLO_ANIVERSARIO-"]),
            int(valor["-BOLO_CASAMENTO-"]), 
            int(valor["-QTD_MINI-"]), 
            int(valor["-QTD_NORMAL-"]), 
            str(valor["-INFO_COMPLEMENTARES-"]) 
        ]).inserir_dados()

        if msg == "Dados inseridos com sucesso!":
            sg.popup(msg, title="Sucesso!")
            nova_encomenda.hide()
            buttons("on")
            continue
        else:
            sg.popup(msg, title="Erro!")
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
            menu_encomenda["-INDEX_ENCOMENDA-"].update(
                values=SQLite('dados.db').select(
                    'dados', '*', 'status = "Concluído"'
                    )
                )
            menu_encomenda["-STATUS_CONCLUIDO-"].update(True)
        elif status_pendente == True:
            menu_encomenda["-INDEX_ENCOMENDA-"].update(
                values=SQLite('dados.db').select(
                    'dados', '*', 'status = "Pendente"'
                    )
                )
            menu_encomenda["-STATUS_PENDENTE-"].update(True)
        continue

    ##########################MAIS INFORMACOES###############################

    if janela == menu_encomenda and evento == "-MAIS_INFORMACOES-":
        try:
            index = int(valor["-INDEX_ENCOMENDA-"][0])

            if status_concluido == True:
                mais_informacoes = ListarEncomendas.mais_informacoes(
                    "Concluído", index
                    )
                menu_encomenda.hide()

            if status_pendente == True:
                mais_informacoes = ListarEncomendas.mais_informacoes(
                    "Pendente", index
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
            lista_encomendas = SQLite('dados.db').select(
                    'dados', '*', 'status = "Pendente"'
                )

            preco_final = FinalizeOrder(
                lista_encomendas, index_encomenda, 
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
            SQLite('dados.db').select(
                'dados', '*', 'status = "Pendente"'
            )
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
            deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                values=SQLite('dados.db').select(
                    'dados', '*', 'status = "Concluído"'
                    )
                )
            deletar_encomenda["-STATUS_CONCLUIDO-"].update(True)

        elif status_pendente == True:
            deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                values=SQLite('dados.db').select(
                    'dados', '*', 'status = "Pendente"'
                    )
                )
            deletar_encomenda["-STATUS_CONCLUIDO-"].update(False)
        continue

    ##########################DELETAR ENCOMENDA###############################

    if janela == deletar_encomenda and evento == "-DELETAR_ENCOMENDA-":
        try:
            index = int(valor["-INDEX_ENCOMENDA-"][0])

            if status_pendente == True:
                lista_encomendas = SQLite('dados.db').select(
                    'dados', 'id', 'status = "Pendente"'
                )
            elif status_concluido == True:
                lista_encomendas = SQLite('dados.db').select(
                    'dados', 'id', 'status = "Concluído"'
                )

            id = lista_encomendas[index][0]
            SQLite('dados.db').delete('dados', f'id={id}')

            if status_concluido == True:
                deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Concluído"'
                        )
                    )
                deletar_encomenda["-STATUS_CONCLUIDO-"].update(True)

            elif status_pendente == True:
                deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Pendente"'
                        )
                    )
                deletar_encomenda["-STATUS_CONCLUIDO-"].update(False)
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
            deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                values=SQLite('dados.db').select(
                    'dados', '*', 'status = "Concluído"'
                    )
                )
            deletar_encomenda["-STATUS_CONCLUIDO-"].update(True)

        elif status_pendente == True:
            deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                values=SQLite('dados.db').select(
                    'dados', '*', 'status = "Pendente"'
                    )
                )
            deletar_encomenda["-STATUS_CONCLUIDO-"].update(False)
        continue

    ###############################EDITAR ENCOMENDA###########################

    if janela == editar_encomenda and evento == "-EDITAR-":
        index = int(valor["-INDEX_ENCOMENDA-"][0])

        if status_pendente == True:
            lista_encomendas = SQLite('dados.db').select(
                'dados', '*', 'status = "Pendente"'
            )
        elif status_concluido == True:
            lista_encomendas = SQLite('dados.db').select(
                'dados', '*', 'status = "Concluído"'
            )
        dados = lista_encomendas[index]
        id = dados[0]

        editar_encomenda.close()
        editar_encomenda = EditarEncomenda.edit_info()

        editar_encomenda["-NOME_CLIENTE-"].update(dados[1])
        editar_encomenda["-DATA_ENTREGA-"].update(dados[2])
        editar_encomenda["-HORA_ENTREGA-"].update(dados[3])
        editar_encomenda["-BOLO_ANIVERSARIO-"].update(dados[4])
        editar_encomenda["-BOLO_CASAMENTO-"].update(dados[5])
        editar_encomenda["-QTD_MINI-"].update(dados[6])
        editar_encomenda["-QTD_NORMAL-"].update(dados[7])
        editar_encomenda["-INFO_COMPLEMENTARES-"].update(dados[9])

    if janela == editar_encomenda and evento == "-CONFIRMAR-":
        msg = EditDados([
            str(valor["-NOME_CLIENTE-"]), 
            str(valor["-DATA_ENTREGA-"]), 
            str(valor["-HORA_ENTREGA-"]), 
            int(valor["-BOLO_ANIVERSARIO-"]),
            int(valor["-BOLO_CASAMENTO-"]), 
            int(valor["-QTD_MINI-"]), 
            int(valor["-QTD_NORMAL-"]), 
            str(valor["-INFO_COMPLEMENTARES-"]) 
        ], id).inserir_dados()

        if msg == "Dados atualizados com sucesso!":
            sg.popup(msg, title="Sucesso!")
            nova_encomenda.hide()
            buttons("on")
            continue
        else:
            sg.popup(msg, title="Erro!")
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
    ###############################LUCRO MENSAL###############################
    ##########################################################################

    if (janela == lucro_do_mes and evento == sg.WIN_CLOSED
        or janela == lucro_do_mes and evento == "-EXIT-"):
        lucro_do_mes.close()
        buttons("on")
        continue

    if janela == lucro_do_mes and evento == "-ENVIAR-":
        try:
            funcionarios = float(valor['-INPUT_FUNCIONARIOS-'])
            mercadorias = float(valor['-INPUT_MERCADORIAS-'])
            impostos = float(valor['-INPUT_IMPOSTOS-'])
            outros = float(valor['-INPUT_OUTROS-'])
            total = Gasto.descobrirGanhoMes() - (funcionarios + mercadorias + impostos + outros) 
            lucro_do_mes['-OUTPUT-'].update(total)
            lucro_do_mes['-OUTPUT-'].update(f'O lucro mensal será {total} reais')
        except ValueError:
            lucro_do_mes['-OUTPUT-'].update('Por favor, digite apenas números.')