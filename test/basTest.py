import json
import os
from unittest import TestCase

from config import create_app

"""Base test class that, initializes variable and settings"""


class BaseTestCase(TestCase):
    def setUp(self):
        """configure virtual test environment."""
        os.environ['APP_SETTING'] = 'Testing'
        self.app = create_app(config_name='testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()


class QuestionsTestCase(BaseTestCase):
    """Class the test for all the endpoints of questions"""

    def __init__(self, method_name='runTest'):
        super().__init__(methodName='runTest')
        self.methodName = method_name
        self.endpoint = 'api/v1/stackendpoints/questions'

    def test_get_all_questions(self):
        results = self.app.test_client.get_question('api/v1/stackendpoints/questions =[]')
        print(results)
        self.assertEqual(results.status_code, 200)

    def test_get_one_question(self):
        response = self.app.test_client.get(self.endpoint + '1/')
        self.assertEqual(response.status_code, 200)

    def test_question_not_exist(self):
        response = self.app.get(self.endpoint)
        self.assertEqual(response.status_code, 404)

    def test_post_questions(self):
        # missing value field = bad
        stack_question = {
            "id": 1,
            "title": "What is Python",
            "description": "give your answer in words",
            "answers": []
        }

        response = self.client.post(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response = self.client.post(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_question_update(self):
        stack_question = {"value": 30}
        response = self.client.put(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 'you question has been updated successfully', 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['stack_question']['value'], 30)

    def test_update_on_non_existing_question(self):
        """ you cannot edit non_existing question"""
        stack_question = {"value": 30}
        response = self.app.put(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 'you cannot edit non existing question', 404)
        stack_question = {"value": 'string'}
        response = self.app.put(self.endpoint, data=json.dumps(stack_question), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_questions(self):
        response = self.app.delete(self.client, )
        self.assertEqual(response.status_code, 204)
        response = self.app.delete(self.endpoint)
        self.assertEqual(response.status_code, 404)
