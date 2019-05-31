import json

from helpers.baseTest import BaseTest


class TestGetFindByStatus(BaseTest):

    base_url = "https://petstore.swagger.io/v2/pet/findByStatus"

    def test_GET_01_GetFindByStatus_Available(self):
        '''
        Check that GET to "/pet/findByStatus?status={available}" gets 200 as Status Code
        And a list of  Pet Data JSONs as response.
        Check that the Schema of the first 3 JSONs in the list is valid.
        '''
        resp = self.api.get(params="status=available")
        self.assertEqual(resp.status_code, 200, "Check that the status code is 200")
        respData = json.loads(resp.text)
        self.assertEqual(type(respData), list, "Check that the Response Data is a list")
        for petData in respData[:3]:
            self.assertJsonSchema(petData, self.pet_schema, "Check that the Pet Data Schema is valid")

    def test_GET_02_GetFindByStatus_Pending(self):
        '''
        Check that GET to "/pet/findByStatus?status={pending}" gets 200 as Status Code
        And a list of  Pet Data JSONs as response.
        Check that the Schema of the first 3 JSONs in the list is valid.
        '''
        resp = self.api.get(params="status=pending")
        self.assertEqual(resp.status_code, 200, "Check that the status code is 200")
        respData = json.loads(resp.text)
        self.assertEqual(type(respData), list, "Check that the Response Data is a list")
        for petData in respData[:3]:
            self.assertJsonSchema(petData, self.pet_schema, "Check that the Pet Data Schema is valid")

    def test_GET_03_GetFindByStatus_sold(self):
        '''
        Check that GET to "/pet/findByStatus?status={sold}" gets 200 as Status Code
        And a list of  Pet Data JSONs as response.
        Check that the Schema of the first 3 JSONs in the list is valid.
        '''
        resp = self.api.get(params="status=sold")
        self.assertEqual(resp.status_code, 200, "Check that the status code is 200")
        respData = json.loads(resp.text)
        self.assertEqual(type(respData), list, "Check that the Response Data is a list")
        for petData in respData[:3]:
            self.assertJsonSchema(petData, self.pet_schema, "Check that the Pet Data Schema is valid")

    def test_GET_04_GetFindByStatus_InvalidStatus(self):
        '''
        Check that GET to "/pet/findByStatus?status={invalidstatus}" gets 400 as Status Code
        TODO: Bug: Status Code from API is 200 as any string is considered as valid
        '''
        resp = self.api.get(params="status=invalidstatus")
        self.assertEqual(resp.status_code, 400, "Check that the status code is 400")