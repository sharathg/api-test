import json

from helpers.baseTest import BaseTest


class TestGetPet(BaseTest):

    base_url = "https://petstore.swagger.io/v2/pet"

    def setUp(self):
        super().setUp()
        self.data_post_add_pet = self.get_testdata("post_add_pet.json")

    def test_GET_01_GetDataOfExistingPet(self):
        '''
        Add a pet by POST to "/pet/" endpoint using the JSON data.
        Check that GET to "/pet/{pet-id}/" gets 200 as Status Code And the Pet Data JSON as response.
        Check that the Schema of the Response is valid.
        '''
        # Add Pet
        self.assertEqual(self.api.post(json=self.data_post_add_pet).status_code, 200, "Check that the Pet was added")
        # Get the Pet Data and run Tests
        resp = self.api.get(self.data_post_add_pet['id'])
        self.assertEqual(resp.status_code, 200, "Check that the status code is 200")
        self.assertJsonSchema(json.loads(resp.text), self.pet_schema, "Check that the response JSON schema is valid")

    def test_GET_02_GetDataOfNonExistantID(self):
        '''
        Delete the Pet with of the Test Data ID
        Check that GET with an Non Existant ID gives 404 Status Code
        '''
        # Delete Pet
        self.api.delete(self.data_post_add_pet['id'])
        # Get the Pet Data and run Tests
        resp = self.api.get(self.data_post_add_pet['id'])
        self.assertEqual(resp.status_code, 404, "Check that the Status Code is 404")

    def test_GET_03_GetDataOfInvalidID(self):
        '''
        Check that GET with an Invalid ID gives 400 Status Code
        TODO: Bug: Status Code from API is 400 as it does not consider the ID as Invalid
        '''
        resp = self.api.get("abc")
        self.assertEqual(resp.status_code, 400, "Check that the Status Code is 400")