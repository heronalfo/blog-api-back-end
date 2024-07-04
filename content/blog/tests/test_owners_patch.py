from .base_owners_test import BaseOwnersTest
from django.urls import reverse

class TestOwmersPatch(BaseOwnersTest):

    def test_owners_patch(self):
                                     
        response = self.patch(data={'name': 'teste-edit'})
        
        self.assertEqual(response.status_code, 200)
        
    def test_post_sql_injection_name(self):
    
        response = self.patch({'name': 'OR 1=1'})
        
        self.assertEqual(response.status_code, 400)
        
    def test_post_sql_injection_link(self):
     
        response = self.patch({'link': 'OR 1=1'})
        
        self.assertEqual(response.status_code, 400)
                    
    def test_owners_patch_invalid_name(self):
                                     
        response = self.patch(data={'name': ' invalid  name'})
        
        self.assertEqual(response.status_code, 400)
        
    def test_owners_patch_invalid_link(self):
                                     
        response = self.patch(data={'link': ' invalid link'})
        
        self.assertEqual(response.status_code, 400)
        
    def test_patch_if_accepted_it_does_not_accept_a_name_with_more_than_192_characters(self):
                
        response = self.post({'content': 'teste-name'*10})
        
        self.assertEqual(response.status_code, 400)
        
        
        