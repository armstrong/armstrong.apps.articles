from .._utils import *
from django.contrib.auth.models import User

class ArticlesAdminTestCase(ArticlesTestCase):
    fixtures = ['admin_user.json']
    
    def testForCkEditor(self):
        c = Client()
        self.assertTrue(c.login(username='test', password='test'))
        response = c.get('/admin/articles/article/add/')
        self.assertCkEditorPresent(response)
        
    def testConfigurableRichText(self):
        with self.settings(ARMSTRONG_HATBAND_RICHTEXTEDITOR='django.forms.widgets.Textarea'):
            c = Client()
            self.assertTrue(c.login(username='test', password='test'))
            response = c.get('/admin/articles/article/add/')
            self.assertCkEditorNotPresent(response)
        