#Calcular a forma de pagamento de um prduto, considerando a sua forma de pagamento.

print('{:=^40}'.format(' BIG BRANDS '))

preco = float(input('Valor das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opcão? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('''Valor das suas compras é de R${} reais
com 10% de desconto fica R${} reais'''.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('''Valor das suas compras é de R${:.2f} reais
com 5% de desconto fica R${:.2f} reais'''.format(preco, total))
elif opcao == 3:
    parcela = preco / 2
    print('''Valor das suas compras é de R${:.2f} reais
parcelado em 2x o valor da parcela é de R${:.2f} reais'''.format(preco, parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcela = int(input('Em quantas vezes você pretende parcelar?'))
    parcela2 = total / parcela
    print('''Valor das suas compras é de R${:.2f} reais,
com 20% de juros o valor passa a ser R${:.2f}
parcelado em {}x o valor fica de {:.2f} '''.format(preco, total, parcela, parcela2))
