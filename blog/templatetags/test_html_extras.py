from django.test import TestCase

from .html_extras import html_arrows


class HtmlArrowsTestCase(TestCase):
	def test_html_arrows(self):
		initial_value = '->'
		expected_value = '&raquo;'
		self.assertEqual(html_arrows(initial_value), expected_value)
