from django.test import TestCase

from core import Produtos


class HistoricoTestCase(TestCase):
    def setUp(self):
        Produtos.objects.create(nome="Produtos")


def test_retorno_str(self):
    p1 = Produtos.objects.get(nome="Produtos")
    self.assertEquals(p1.__str__(), "Produtos")
