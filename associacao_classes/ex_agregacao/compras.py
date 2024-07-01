from classes_compras import CarrinhoDeCompras,Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camisa',30)
p2 = Produto('Short',25)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p1)

carrinho.listar_produtos()

print(carrinho.soma_total())