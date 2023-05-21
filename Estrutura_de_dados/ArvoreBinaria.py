class TNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class ArvoreBinariaSimetrica:
    def __init__(self, dado=None):
        if dado:
            self.root = TNode(dado)
        else:
            self.root = None

    def percurso_simetrico(self, node=None):
        if node is None:
            node = self.root

        percurso = []

        if node.left:
            percurso += self.percurso_simetrico(node.left)

        percurso.append(node.value)

        if node.right:
            percurso += self.percurso_simetrico(node.right)

        return percurso


if __name__ == "__main__":
    # Construção da árvore
    n1 = TNode("Flamengo")  # Topo da árvore
    n2 = TNode("Palmeiras")
    n3 = TNode("São Paulo")
    n4 = TNode("Grêmio")
    n5 = TNode("Internacional")
    n6 = TNode("Atlético Mineiro")
    n7 = TNode("Cruzeiro")
    n8 = TNode("Botafogo")
    n9 = TNode("Fluminense")
    n10 = TNode("Vasco")
    n11 = TNode("Santos")

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n4.left = n10
    n4.right = n11
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree = ArvoreBinariaSimetrica()
    tree.root = n2

    # Percurso simétrico (inorder traversal)
    percurso = tree.percurso_simetrico()
    print("Percurso simétrico:", percurso)

    # Caminho percorrido pela árvore:
    #                'Palmeiras'
    #               /           \
    #        'Flamengo'     'São Paulo'
    #                        /          \
    #                'Grêmio'     'Internacional'
    #                /       \         /            \
    #           'Vasco'  'Santos'  'Atlético Mineiro' 'Fluminense'
    #                                             /                    \
    #                                        'Cruzeiro'          'Botafogo'
