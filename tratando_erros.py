def parcelar():
    valor = 1000
    print(f'O valor da sua compra foi de R$ {valor:.2f}.')
    try:
        qtde_parcelas = int(input('Em quantas vezes você deseja parcelar?'))
        valor_parcelas = valor/qtde_parcelas
    except ValueError:
        print('Valor inválido')
        print('Reinicie a operação e tente novamente')
    except ZeroDivisionError:
        print('O valor mínimo de parcelas é 1')
        print('Reinicie a operação e tente novamente')
    else:
        print(f'Sua compra foi parcelada em {qtde_parcelas}x de R${valor_parcelas:.2f}')
    finally:
        print('---SUPERMERCADOS TÁTUDOCARO AGRADECE A PREFERÊNCIA----')

parcelar()