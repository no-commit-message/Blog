from django.test import TestCase

# Create your tests here.
class TopPageTest(TestCase):
    def test_should_contain_expexted_content(self):
        response = self.client.get("/")
        self.assertContains(response, "トップページ", status_code=200)
    
    def test_should_use_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'top.html')