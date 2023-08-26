from banco import obterConta, banco

def transferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
        else:
            print('saldo insuficiente para transferencia!')
    else:
        print('Uma ou mais contas não encontradas!')

print(banco)
transferir(1, 2, 150)
print(banco)