from funcoes import taxa, calculo_percentual

venda, aplicacao, perc_taxa, desconto= 0.0, 0, 0.0, 0.0

while True:
    venda= float(input("Coloque o valor da compra: "))
    aplicacao= int(input("Digite a quantidade de parcelas: "))
    if venda<0 or aplicacao<0:
        break

    perc_taxa= taxa(aplicacao)
    desconto= calculo_percentual(venda, perc_taxa)

    print(f"Valor do desconto/acréscimo: {desconto}")
    print(f"Valor final com desconto/acréscimo: {venda + desconto}")