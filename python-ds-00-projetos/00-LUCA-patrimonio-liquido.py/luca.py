'''
    This is my personal library for accounting statements in Python, a tribute to Luca Pacioli,
    the "father of accounting" and creator of the double-entry bookkeeping method.

    Instituto Federal do Sudeste de Minas Gerais - Campus Barbacena
    Bacharelado em Administração
    Matheus Henrique de Oliveira Ferreira
'''

def patrimonio_liquido(ativos, passivos):
    pl = ativos - passivos
    return pl