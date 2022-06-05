
class Formulas:
    @staticmethod
    def pa(termo_1, termo2, razao):
        n_termo = termo_1 + ((termo2 - termo_1) * razao)
        return ((termo_1 + n_termo) * termo2) / 2

    @staticmethod
    def pg(termo_1, termo2, razao):
        n_termo = termo_1 * razao **(razao - termo_1)
        return (termo_1 * (razao ** termo2 - termo_1)) / (razao - termo_1)
