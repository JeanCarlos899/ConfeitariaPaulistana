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
    from sicronizar import Sicronizar
    from Scripts.cadastrar_caminho import Criar
    from Scripts.cadastrar_caminho import Editar
    from Design.criar_caminho import FrtCam
    from Design.recuperar import Recuperar
    
except ImportError:
    os.system("pip3 install -r requirements.txt")
    print("Bibliotecas instaladas com sucesso!")
    print("Reabra o programa.")
    sys.exit()

def buttons(on_off):
    keys = {
        1: "-NOVA_ENCOMENDA-", 
        2: "-LISTAR_ENCOMENDAS-",
        3: "-DAR_BAIXA_ENCOMENDA-",
        4: "-EDITAR_ENCOMENDA-",
        5: "-GRAFICOS-",
        6: "-RELATORIOS-",
        7: "-FATURAMENTO-",
        8: "-DELETAR_ENCOMENDA-",
        9: "-LUCRO_MENSAL-",
        10: "-LOCAL-",
        11: "-RECUPERAR-",
        12: "-SAIR-"
    }

    if on_off == "on":
        for key in range(len(keys)):
            menu[keys[key+1]].update(disabled=False)
    else: 
        for key in range(len(keys)):
            menu[keys[key+1]].update(disabled=True)

####################INICIANDO JANELAS######################
menu, nova_encomenda = MenuPrincipal.menu_principal(), None
lista_encomenda, menu_encomenda = None, None
dar_baixa_encomenda, dados_cliente = None, None
salgadinhos, mais_informacoes = None, None
graficos, relatorios, deletar_encomenda = None, None, None
editar_encomenda, faturamento = None, None
lucro_do_mes, local, recuperar = None, None, None

menu.maximize()

while True:
    # Leitura de todas as janelas abertas
    janela, evento, valor = sg.read_all_windows()
    
    ##########################################################################
    ###########################JANELA PRINCIPAL###############################
    ##########################################################################

    if janela == menu:
        
        if evento == sg.WIN_CLOSED or evento == "-SAIR-":
        
            try:    
                if os.path.getsize("caminhos.csv") == 0:
                    sg.popup_ok("Não há caminhos cadastrados no sistema", "Cadastre um para que possa ser feito o backup" )
                    break 
                else:
                    localOriginal = 'dados.db'
                    file = 'caminhos.csv'

                    with open(file, 'r') as f:
                        caminhos = f.readlines() 

                    novolocal = caminhos[0].strip()          
                    sincronizar = Sicronizar(localOriginal, novolocal)
                    sincronizar.sincronizar()
                    break

            except FileNotFoundError:
                sg.popup_ok("Caminho inválido, edite-o. Para que o backup possa ser feito.")
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

        elif evento == "-LOCAL-":
            local = FrtCam.tela()
            buttons("off")
            continue

        elif evento == "-RECUPERAR-":
            recuperar = Recuperar.escolher_arquivo()
            continue


    ##########################################################################
    ###########################NOVA ENCOMENDA#################################
    ##########################################################################

    elif janela == nova_encomenda:

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            nova_encomenda.hide()
            buttons("on")
            continue

        elif evento == "-CONFIRMAR-":
            status_menssage = InsertDados([
                str(valor["-NOME_CLIENTE-"]), 
                str(valor["-DATA_ENTREGA-"]), 
                str(valor["-HORA_ENTREGA-"]), 
                int(valor["-BOLO_ANIVERSARIO-"]),
                int(valor["-BOLO_CASAMENTO-"]), 
                int(valor["-QTD_MINI-"]), 
                int(valor["-QTD_NORMAL-"]), 
                str(valor["-INFO_COMPLEMENTARES-"]) 
            ])

            msg = status_menssage()

            if msg == True:
                sg.popup("Dados inseridos com sucesso!", title="Sucesso!")
                nova_encomenda.hide()
                buttons("on")
                continue
            else:
                sg.popup(msg, title="Erro!")
                continue

    ##########################################################################
    ###########################LISTAR ENCOMENDAS##############################
    ##########################################################################

    elif janela == menu_encomenda:

        status_concluido = valor["-STATUS_CONCLUIDO-"] 
        status_pendente = valor["-STATUS_PENDENTE-"]

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            menu_encomenda.hide()
            buttons("on")
            continue

        elif evento == "-FILTRAR-":
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

        elif evento == "-MAIS_INFORMACOES-":
            try:
                index = int(valor["-INDEX_ENCOMENDA-"][0])

                if status_concluido == True:
                    mais_informacoes = ListarEncomendas.mais_informacoes(
                        "Concluído", index
                        )
                    menu_encomenda.hide()

                elif status_pendente == True:
                    mais_informacoes = ListarEncomendas.mais_informacoes(
                        "Pendente", index
                        )
                    menu_encomenda.hide()
                continue
            except:
                sg.popup("Selecione uma encomenda para mais informações!")
                continue

    ##########################MAIS INFORMACOES###############################

    elif (janela == mais_informacoes and evento == sg.WIN_CLOSED 
        or janela == mais_informacoes and evento == "-VOLTAR-"):
        mais_informacoes.hide()
        menu_encomenda.un_hide()
        continue
    
    ##########################################################################
    ###########################BAIXA EM ENCOMENDA#############################
    ##########################################################################

    elif janela == dar_baixa_encomenda:

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            dar_baixa_encomenda.hide()
            buttons("on")
            continue

        elif evento == "-FINALIZAR_ENCOMENDA-":
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

        elif evento == "-ATUALIZAR_LISTA-":
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

    elif janela == graficos:

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            graficos.hide() 
            buttons("on")

        elif evento == "-STATUS_PEDIDO-":
            NewChart.graficoPizza()
            continue

        elif evento == "-TIPO_BOLO-":
            NewChart.graficoTipoBolo()
            continue

        elif evento == "-TIPO_SALGADO-":
            NewChart.graficoTipoSalgados()
            continue

        elif evento == "-MENSAIS-":
            NewChart.graficoBarrasPedidos()
            continue

        elif evento == "-LUCRO_MENSAL-":
            NewChart.graficoganho()
            continue

        elif evento == "-LUCRO_POR_TIPO_DE_FESTAS-":
            NewChart.lucroporfesta()
            continue

    ##########################################################################
    ###########################RELATÓRIOS#####################################
    ##########################################################################

    elif janela == relatorios:
            
        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            relatorios.hide()
            buttons("on")
        
        elif evento == "-PEDIDOS_ENTREGUES-":
            Relatorios.historico_pedidos_concluido()
            sg.popup("Relatório gerado com sucesso!")
            continue

        elif evento == "-PEDIDOS_NAO_ENTREGUES-":
            Relatorios.historico_pedidos_naoentregues()
            sg.popup("Relatório gerado com sucesso!")
            continue

        elif evento == "-PEDIDOS_PENDENTES-":
            Relatorios.pedidos_pendentes()
            sg.popup("Relatório gerado com sucesso!")
            continue

        elif evento == "-TODOS_PEDIDOS-":
            Relatorios.historico_todos_pedidos()
            sg.popup("Relatório gerado com sucesso!")
            continue

    ##########################################################################
    ############################DELETAR ENCOMENDA#############################
    ##########################################################################

    elif janela == deletar_encomenda:

        status_concluido = valor["-STATUS_CONCLUIDO-"] 
        status_pendente = valor["-STATUS_PENDENTE-"]

        def status(concluido, pendente):
            if concluido == True:
                deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Concluído"'
                        )
                    )
                deletar_encomenda["-STATUS_CONCLUIDO-"].update(True)

            elif pendente == True:
                deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Pendente"'
                        )
                    )
                deletar_encomenda["-STATUS_CONCLUIDO-"].update(False)
            
        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            deletar_encomenda.hide()
            buttons("on")
            continue
        
        elif evento == "-FILTRAR-":
            status(status_concluido, status_pendente)
            continue

        ##########################DELETAR ENCOMENDA###############################

        elif evento == "-DELETAR_ENCOMENDA-":
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

                status(status_concluido, status_pendente)

            except:
                sg.popup("Nenhuma encomenda selecionada!")
                continue

    ##########################################################################
    ###########################EDITAR ENCOMENDAS##############################
    ##########################################################################

    elif janela == editar_encomenda:

        try:
            status_concluido = valor["-STATUS_CONCLUIDO-"] 
            status_pendente = valor["-STATUS_PENDENTE-"]
        except:
            pass

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            editar_encomenda.hide()
            buttons("on")
            continue 

        elif evento == "-FILTRAR-":
            if status_concluido == True:
                editar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Concluído"'
                        )
                    )
                editar_encomenda["-STATUS_CONCLUIDO-"].update(True)

            elif status_pendente == True:
                editar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Pendente"'
                        )
                    )
                editar_encomenda["-STATUS_CONCLUIDO-"].update(False)
            continue

        ###############################EDITAR ENCOMENDA###########################

        elif evento == "-EDITAR-":
            try:
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
            
            except:
                sg.popup("Nenhuma encomenda selecionada!")
                continue

        elif evento == "-CONFIRMAR-":
            status_menssage = EditDados([
                str(valor["-NOME_CLIENTE-"]), 
                str(valor["-DATA_ENTREGA-"]), 
                str(valor["-HORA_ENTREGA-"]), 
                int(valor["-BOLO_ANIVERSARIO-"]),
                int(valor["-BOLO_CASAMENTO-"]), 
                int(valor["-QTD_MINI-"]), 
                int(valor["-QTD_NORMAL-"]), 
                str(valor["-INFO_COMPLEMENTARES-"]) 
            ], id)

            msg = status_menssage()

            if msg == True:
                sg.popup("Dados atualizados com sucesso!", title="Sucesso!")
                editar_encomenda.hide()
                buttons("on")
                continue
            else:
                sg.popup(msg, title="Erro!")
                continue
    
    ##########################################################################
    ###############################FATURAMENTO################################
    ##########################################################################

    if janela == faturamento:

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            faturamento.close()
            buttons("on")
            continue

        elif evento == "-FILTRAR-":
            data_inicial = valor["-DATA_INICIAL-"]
            data_final = valor["-DATA_FINAL-"]
            
            valor = Revenues(data_inicial, data_final).get_value()
            faturamento["-VALOR_FATURAMENTO-"].update(valor)
            continue

    ##########################################################################
    ###############################LUCRO MENSAL###############################
    ##########################################################################

    if janela == lucro_do_mes:
            
        if evento == sg.WIN_CLOSED or evento == "-EXIT-":
            lucro_do_mes.close()
            buttons("on")
            continue
        
        elif janela == lucro_do_mes and evento == "-ENVIAR-":
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


    ##########################################################################
    ###############################Cadastrar caminho###############################
    ##########################################################################

    if janela == local:
        
        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            local.close()
            buttons("on")
            continue

        elif evento == "-PROCURAR-":
            Criar.criar()
            continue

        elif evento == "-EDITAR-":
            Editar.editar()
            continue