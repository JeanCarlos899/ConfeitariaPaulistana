
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


arquivo = pd.read_excel('dados.xlsx')



def graficoPizza():
    Entregue = arquivo.loc[arquivo['Status']=='Concluído']
    Pendente = arquivo.loc[arquivo['Status']=='Pendente']
    plt.title('Status dos pedidos')
    plt.pie([len(Entregue),len(Pendente)], labels=['Concluído','Pendente'], autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

graficoPizza()

