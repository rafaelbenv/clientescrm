from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Cliente


class ClienteModelTest(TestCase):

    def test_criar_cliente(self):
        cliente = Cliente.objects.create(
            nome='João Silva',
            email='joao@email.com',
            telefone='(41) 99999-9999',
            cpf='529.982.247-25',
        )
        self.assertEqual(str(cliente), 'João Silva')

    def test_cliente_ativo_por_padrao(self):
        cliente = Cliente.objects.create(
            nome='Maria Souza',
            email='maria@email.com',
            telefone='(41) 98888-8888',
            cpf='871.119.670-86',
        )
        self.assertTrue(cliente.ativo)


class ClienteViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.usuario = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        self.cliente = Cliente.objects.create(
            nome='Carlos Teste',
            email='carlos@email.com',
            telefone='(41) 97777-7777',
            cpf='275.487.490-04',
        )

    def test_listar_clientes(self):
        response = self.client.get('/clientes/')
        self.assertEqual(response.status_code, 200)

    def test_detalhe_cliente(self):
        response = self.client.get(f'/clientes/{self.cliente.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_criar_cliente_view(self):
        response = self.client.post('/clientes/novo/', {
            'nome': 'Novo Cliente',
            'email': 'novo@email.com',
            'telefone': '(41) 96666-6666',
            'cpf': '568.339.820-62',
            'ativo': True,
        })
        self.assertEqual(Cliente.objects.filter(email='novo@email.com').count(), 1)

    def test_editar_cliente_view(self):
        response = self.client.post(f'/clientes/{self.cliente.pk}/editar/', {
            'nome': 'Carlos Editado',
            'email': 'carlos@email.com',
            'telefone': '(41) 97777-7777',
            'cpf': '275.487.490-04',
            'ativo': True,
        })
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nome, 'Carlos Editado')

    def test_excluir_cliente_view(self):
        response = self.client.post(f'/clientes/{self.cliente.pk}/excluir/')
        self.assertEqual(Cliente.objects.filter(pk=self.cliente.pk).count(), 0)

    def test_redireciona_sem_login(self):
        self.client.logout()
        response = self.client.get('/clientes/')
        self.assertEqual(response.status_code, 302)