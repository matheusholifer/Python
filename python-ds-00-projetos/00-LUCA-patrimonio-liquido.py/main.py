import luca

# Exemplo
# Patrimônio da Cia. Barbacena em $ mil
bens =  1830;        obrigacoes = 4500
direitos = 2800

# Em contabilidade, o ativo é composto pela soma de todos os bens e direitos de propriedade
# ou controle de uma entidade, capazes de gerar benefícios futuros e mensuráveis monetariamente.
ativos = bens + direitos

# Em contabilidade, todas as obrigações com terceiros são consideradas passivos. O passivo representa dívidas
# denominadas "obrigações exigíveis", que são compromissos financeiros que serão reclamados e pagos na data de vencimento.
passivos = obrigacoes

# Segundo José Carlos Marion, patrimônio líquido é a diferença entre o ativo (bens e direitos) e o passivo (obrigações) de uma empresa.
# Representa a riqueza líquida real da entidade, ou seja, o valor que pertence efetivamente aos sócios ou acionistas após a quitação de todas as dívidas.
print(f"\nO Patrimônio Líquido da Cia. Barbacena é de R${luca.patrimonio_liquido(ativos, passivos)}.")