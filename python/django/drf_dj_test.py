from rest_framework.test import APITestCase, APIClient
from authentication.models import Account
import json
import unittest


class DjangoRestFrameworkTests(APITestCase):

    """Tests for REST API events endpoint"""

    fixtures = ['test_accounts.json', 'test_customers.json']
    VALID_customerS = [{'id': 2,
                       'partner_1_name': 'Jane',
                       'partner_1_party_size': 6,
                       'partner_1_type': {'id': 3,
                                          'title': 'Partner'},
                       'partner_2_name': 'Jim',
                       'partner_2_party_size': 6,
                       'partner_2_type': {'id': 3,
                                          'title': 'Partner'}}]

    CREATE_CUSTOMER = {
        "partner_1_title": "4",
        "partner_2_title": "4",
        "partner_1_name": "lola",
        "partner_2_name": "run",
        "partner_1_party_size": 3,
        "partner_2_party_size": 3
    }

    def change_user(self):
        """change to tester2 auth account."""
        self.client.logout()
        self.client.login(username='tester2@tester.com', password='tester')

    def CREATE_CUSTOMER(self, customer=None):
        if customer is None:
            customer = self.CREATE_CUSTOMER
        return self.client.post(
            '/api/v1/customers/', data=customer)

    def fix_password_hashes(self):
        # Set passwords, Django Settings in Test use MD5 hashes.
        test_account_1 = Account.objects.get(username='tester')
        test_account_1.set_password('tester')
        test_account_1.save()
        test_account_2 = Account.objects.get(username='tester2')
        test_account_2.set_password('tester')
        test_account_2.save()

    def setUp(self):
        self.fix_password_hashes()
        self.client = APIClient()
        self.client.login(username='tester@tester.com', password='tester')
        print(self.shortDescription())

    def test_get_list_customer(self):
        """customers endpoint should return a list of objects."""
        customer = self.client.get('/api/v1/customers/')
        self.assertEqual(self.VALID_customerS,
                         json.loads(customer.content.decode('utf-8')))

    def test_CREATE_CUSTOMER(self):
        """create a test customer."""
        customer_create_response = self.CREATE_CUSTOMER()
        self.assertEqual(customer_create_response.status_code, 201)

    def test_check_order(self):
        """endpoint should return partner_1_name as lola for the first_customer"""
        self.change_user()
        number_2_customer = self.CREATE_CUSTOMER.copy()
        # deliberatly change value to check against.
        number_2_customer['partner_1_name'] = "IMDUECE"
        self.CREATE_CUSTOMER()
        number_2_customer = self.CREATE_CUSTOMER
        first_customer = json.loads(
            self.client.get('/api/v1/customers/').content.decode('utf-8'))[0]
        self.assertEqual(
            self.CREATE_CUSTOMER['partner_1_name'],
            first_customer['partner_1_name'])

    @unittest.expectedFailure
    def test_customer_permissions(self):
        """there should only be customers that belong to the user."""
        # create customer obj via tester2
        self.change_user()
        self.client.post(
            '/api/v1/customers/', data=self.CREATE_CUSTOMER)
        self.client.logout()
        # customer object doesn't appear.
        self.client.login(username='tester@tester.com', password='tester')
        api_response = json.loads(
            self.client.get('/api/v1/customers/').content.decode('utf-8'))
        self.assertListEqual(api_response, self.CREATE_CUSTOMER)

    def test_partner_types(self):
        """there should be 5 partner types."""
        partner_types = json.loads(
            self.client.get('/api/v1/partnertypes/').content.decode('utf8'))
        self.assertEqual(5, len(partner_types))
