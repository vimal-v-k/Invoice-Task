from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
# Create your tests here.
class InvoiceAPITestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.client = APIClient()
        self.invoice = Invoice.objects.create(date="2023-09-25", customer_name="Test Customer")
        self.invoice_detail = InvoiceDetail.objects.create(invoice=self.invoice, description="Item 1", quantity=2, unit_price=10, price=20)

    def test_get_invoices(self):
        # Test GET request to /api/invoices/
        response = self.client.get('/api/invoices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice(self):
        # Test POST request to /api/invoices/
        data = {
            "details": [],
            "date": "2023-09-26",
            "customer_name": "New Customer"
        }
        response = self.client.post('/api/invoices/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_invoice(self):
        # Test PUT request to /api/invoices/{pk}/
        data = {
            "details": [],
            "date": "2023-09-27",
            "customer_name": "Updated Customer"
        }
        response = self.client.put(f'/api/invoices/{self.invoice.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invoice(self):
        # Test DELETE request to /api/invoices/{pk}/
        response = self.client.delete(f'/api/invoices/{self.invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
