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

class Program:

    def __init__(self):

        # Menu initializes next to the class
        self.menu = MenuPrincipal.menu_principal()

        # Definition of windows in the builder
        self.nova_encomenda = None
        self.dados_cliente = None
        self.lista_encomenda = None
        self.menu_encomenda = None
        self.dar_baixa_encomenda = None
        self.salgadinhos = None
        self.mais_informacoes = None
        self.graficos = None
        self.relatorios = None
        self.deletar_encomenda = None 
        self.editar_encomenda = None
        self.faturamento = None
        self.lucro_do_mes = None
        self.local = None
        self.recuperar = None

        # Program startup run method
        self.__run()

    def buttons(self, on_off):
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
                self.menu[keys[key+1]].update(disabled=False)
        else: 
            for key in range(len(keys)):
                self.menu[keys[key+1]].update(disabled=True)

    def functionsMenu(self, evento):

        if evento == sg.WIN_CLOSED or evento == "-SAIR-":
        
            try:    
                if os.path.getsize("caminhos.csv") == 0:
                    sg.popup_ok("Não há caminhos cadastrados no sistema", "Cadastre um para que possa ser feito o backup" )
                    return False 
                else:
                    localOriginal = 'dados.db'
                    file = 'caminhos.csv'

                    with open(file, 'r') as f:
                        caminhos = f.readlines() 

                    novolocal = caminhos[0].strip()          
                    sincronizar = Sicronizar(localOriginal, novolocal)
                    sincronizar.sincronizar()
                    return False

            except FileNotFoundError:
                sg.popup_ok("Caminho inválido, edite-o. Para que o backup possa ser feito.")
                return False

        elif evento == "-NOVA_ENCOMENDA-":
            self.nova_encomenda = NovaEncomenda.nova_encomenda("Nova Encomenda")
            self.buttons("off")

        elif evento == "-LISTAR_ENCOMENDAS-":
            self.menu_encomenda = ListarEncomendas.listar_encomendas("Pendente")
            self.buttons("off")

        elif evento == "-DAR_BAIXA_ENCOMENDA-":
            self.dar_baixa_encomenda = BaixaEncomenda.baixa_encomenda()
            self.buttons("off")

        elif evento == "-GRAFICOS-":
            self.graficos = Graficos.menu_graficos()
            self.buttons("off")

        elif evento == "-RELATORIOS-":
            self.relatorios = FrontRelatorio.menu_relatorios()
            self.buttons("off")

        elif evento == "-FATURAMENTO-":
            self.faturamento = Faturamento.faturamento()
            self.buttons("off")

        elif evento == "-EDITAR_ENCOMENDA-":
            self.editar_encomenda = EditarEncomenda.listar_encomendas("Pendente")
            self.buttons("off")

        elif evento == "-DELETAR_ENCOMENDA-":
            self.deletar_encomenda = DeletarEncomenda.deletar_encomenda("Pendente")
            self.buttons("off")

        elif evento == "-LUCRO_MENSAL-":
            self.lucro_do_mes = Lucromensal.lucro()
            self.buttons("off")

        elif evento == "-LOCAL-":
            self.local = FrtCam.tela()
            self.buttons("off")

        elif evento == "-RECUPERAR-":
            self.recuperar = Recuperar.escolher_arquivo()

    def newOrder(self, evento, valor):

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            self.nova_encomenda.hide()
            self.buttons("on")
            return

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
                self.nova_encomenda.hide()
                self.buttons("on")
                return
            else:
                sg.popup(msg, title="Erro!")
                return

    def listOrder(self, evento, valor):
        
        status_concluido = valor["-STATUS_CONCLUIDO-"] 
        status_pendente = valor["-STATUS_PENDENTE-"]

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            self.menu_encomenda.hide()
            self.buttons("on")
            return

        elif evento == "-FILTRAR-":
            if status_concluido == True:
                self.menu_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Concluído"'
                        )
                    )
                self.menu_encomenda["-STATUS_CONCLUIDO-"].update(True)
            elif status_pendente == True:
                self.menu_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Pendente"'
                        )
                    )
                self.menu_encomenda["-STATUS_PENDENTE-"].update(True)
            return

        elif evento == "-MAIS_INFORMACOES-":
            try:
                index = int(valor["-INDEX_ENCOMENDA-"][0])

                if status_concluido == True:
                    self.mais_informacoes = ListarEncomendas.mais_informacoes(
                        "Concluído", index
                        )
                    self.menu_encomenda.hide()

                elif status_pendente == True:
                    self.mais_informacoes = ListarEncomendas.mais_informacoes(
                        "Pendente", index
                        )
                    self.menu_encomenda.hide()
                return
            except:
                sg.popup("Selecione uma encomenda para mais informações!")
                return

    def lowOrder(self, evento, valor):

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            self.dar_baixa_encomenda.hide()
            self.buttons("on")
            return

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

                self.dar_baixa_encomenda["-VALOR_FINAL-"].update("R$" + str(preco_final))
                self.dar_baixa_encomenda["-FINALIZAR_ENCOMENDA-"].update(disabled=True)
                return
            except:
                sg.popup("Selecione uma encomenda para finalizar!")
                return

        elif evento == "-ATUALIZAR_LISTA-":
            self.dar_baixa_encomenda["-TABLE_LISTAR_ENCOMENDA-"].update(
                SQLite('dados.db').select(
                    'dados', '*', 'status = "Pendente"'
                )
            )

            self.dar_baixa_encomenda["-FINALIZAR_ENCOMENDA-"].update(disabled=False)
            self.dar_baixa_encomenda["-VALOR_FINAL-"].update("R$0,00")
            self.dar_baixa_encomenda["-BOLO_ANIVERSARIO-"].update(0)
            self.dar_baixa_encomenda["-BOLO_CASAMENTO-"].update(0)
            return

    def graphics(self, evento):

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            self.graficos.hide() 
            self.buttons("on")

        elif evento == "-STATUS_PEDIDO-":
            NewChart.graficoPizza()

        elif evento == "-TIPO_BOLO-":
            NewChart.graficoTipoBolo()

        elif evento == "-TIPO_SALGADO-":
            NewChart.graficoTipoSalgados()

        elif evento == "-MENSAIS-":
            NewChart.graficoBarrasPedidos()

        elif evento == "-LUCRO_MENSAL-":
            NewChart.graficoganho()
    
        elif evento == "-LUCRO_POR_TIPO_DE_FESTAS-":
            NewChart.lucroporfesta()

    def reports(self, evento):      
        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            self.relatorios.hide()
            self.buttons("on")
        
        elif evento == "-PEDIDOS_ENTREGUES-":
            Relatorios.historico_pedidos_concluido()
            sg.popup("Relatório gerado com sucesso!")

        elif evento == "-PEDIDOS_NAO_ENTREGUES-":
            Relatorios.historico_pedidos_naoentregues()
            sg.popup("Relatório gerado com sucesso!")

        elif evento == "-PEDIDOS_PENDENTES-":
            Relatorios.pedidos_pendentes()
            sg.popup("Relatório gerado com sucesso!")

        elif evento == "-TODOS_PEDIDOS-":
            Relatorios.historico_todos_pedidos()
            sg.popup("Relatório gerado com sucesso!")

    def delOrder(self, evento, valor):

        status_concluido = valor["-STATUS_CONCLUIDO-"] 
        status_pendente = valor["-STATUS_PENDENTE-"]

        def status(concluido, pendente):
            if concluido == True:
                self.deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Concluído"'
                        )
                    )
                self.deletar_encomenda["-STATUS_CONCLUIDO-"].update(True)

            elif pendente == True:
                self.deletar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Pendente"'
                        )
                    )
                self.deletar_encomenda["-STATUS_CONCLUIDO-"].update(False)
            
        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            self.deletar_encomenda.hide()
            self.buttons("on")
            return
        
        elif evento == "-FILTRAR-":
            status(status_concluido, status_pendente)
            return

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
                return

    def editOrder(self, evento, valor):
        id = 0

        try:
            status_concluido = valor["-STATUS_CONCLUIDO-"] 
            status_pendente = valor["-STATUS_PENDENTE-"]
        except:
            pass

        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            self.editar_encomenda.hide()
            self.buttons("on")
            return

        elif evento == "-FILTRAR-":
            if status_concluido == True:
                self.editar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Concluído"'
                        )
                    )
                self.editar_encomenda["-STATUS_CONCLUIDO-"].update(True)

            elif status_pendente == True:
                self.editar_encomenda["-INDEX_ENCOMENDA-"].update(
                    values=SQLite('dados.db').select(
                        'dados', '*', 'status = "Pendente"'
                        )
                    )
                self.editar_encomenda["-STATUS_CONCLUIDO-"].update(False)
            return

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

                self.editar_encomenda.close()
                self.editar_encomenda = EditarEncomenda.edit_info()

                self.editar_encomenda["-NOME_CLIENTE-"].update(dados[1])
                self.editar_encomenda["-DATA_ENTREGA-"].update(dados[2])
                self.editar_encomenda["-HORA_ENTREGA-"].update(dados[3])
                self.editar_encomenda["-BOLO_ANIVERSARIO-"].update(dados[4])
                self.editar_encomenda["-BOLO_CASAMENTO-"].update(dados[5])
                self.editar_encomenda["-QTD_MINI-"].update(dados[6])
                self.editar_encomenda["-QTD_NORMAL-"].update(dados[7])
                self.editar_encomenda["-INFO_COMPLEMENTARES-"].update(dados[9])
            
            except:
                sg.popup("Nenhuma encomenda selecionada!")
                

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
                self.editar_encomenda.hide()
                self.buttons("on")
                return
            else:
                sg.popup(msg, title="Erro!")
                return

    def revenues(self, evento, valor):
        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            self.faturamento.close()
            self.buttons("on")

        elif evento == "-FILTRAR-":
            data_inicial = valor["-DATA_INICIAL-"]
            data_final = valor["-DATA_FINAL-"]
            
            valor = Revenues(data_inicial, data_final).get_value()
            self.faturamento["-VALOR_FATURAMENTO-"].update(valor)

    def monthlyPronfit(self, evento, valor):
        if evento == sg.WIN_CLOSED or evento == "-EXIT-":
            self.lucro_do_mes.close()
            self.buttons("on")
        
        elif evento == "-ENVIAR-":
            try:
                funcionarios = float(valor['-INPUT_FUNCIONARIOS-'])
                mercadorias = float(valor['-INPUT_MERCADORIAS-'])
                impostos = float(valor['-INPUT_IMPOSTOS-'])
                outros = float(valor['-INPUT_OUTROS-'])

                total = Gasto.descobrirGanhoMes() - (funcionarios + mercadorias + impostos + outros) 
                self.lucro_do_mes['-OUTPUT-'].update(total)
                self.lucro_do_mes['-OUTPUT-'].update(f'O lucro mensal será {total} reais')

            except ValueError:
                self.lucro_do_mes['-OUTPUT-'].update('Por favor, digite apenas números.')

    def registerPath(self, evento):
        if evento == sg.WIN_CLOSED or evento == "-VOLTAR-":
            self.local.close()
            self.buttons("on")

        elif evento == "-PROCURAR-":
            Criar.criar()

        elif evento == "-EDITAR-":
            Editar.editar()

    def __run(self):

        self.menu.maximize()

        while True:

            janela, evento, valor = sg.read_all_windows()

            if janela == self.menu:
                sair = self.functionsMenu(evento)

                if sair == False:
                    break

            elif janela == self.nova_encomenda:
                self.newOrder(evento, valor)

            elif janela == self.menu_encomenda:
                self.listOrder(evento, valor)

            elif (janela == self.mais_informacoes and evento == sg.WIN_CLOSED 
                or janela == self.mais_informacoes and evento == "-VOLTAR-"):
                self.mais_informacoes.hide()
                self.menu_encomenda.un_hide()

            elif janela == self.dar_baixa_encomenda:
                self.lowOrder(evento, valor)

            elif janela == self.graficos:
                self.graphics(evento)

            elif janela == self.relatorios:
                self.reports(evento)

            elif janela == self.deletar_encomenda:
                self.delOrder(evento, valor)

            elif janela == self.editar_encomenda:
                self.editOrder(evento, valor)

            elif janela == self.faturamento:
                self.revenues(evento, valor)

            elif janela == self.lucro_do_mes:
                self.monthlyPronfit(evento, valor)

            if janela == self.local:
                self.registerPath(evento)

if __name__ == "__main__":
    program = Program()