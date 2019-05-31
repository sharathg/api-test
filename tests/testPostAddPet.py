import json

from helpers.baseTest import BaseTest


class TestPostAddPet(BaseTest):

    base_url = "https://petstore.swagger.io/v2/pet"

    def setUp(self):
        super().setUp()
        self.data_post_add_pet = self.get_testdata("post_add_pet.json")

    def test_POST_ADD_01_AddPetToEmptyPetID(self):
        '''
        Make sure that a petID is empty.
        Add a pet by POST to "/pet/" and sending a JSON as data of the pet.
        Make sure that the schema and data of the response is correct.
        Make Sure that the data is stored by Getting the data using "/pet/(pet-id)/" API endpoint.
        '''
        # Make sure the petID is empty
        if self.api.get(self.data_post_add_pet['id']).status_code != 404:
            self.api.delete(self.data_post_add_pet['id'])
        self.assertEqual(self.api.get(self.data_post_add_pet['id']).status_code, 404,
                         "Check that the Status Code is 404 (Not Found)")
        # petID is empty/not-found. Add Pet by Posting to the "/pet/" API endpoint and run Tests
        resp = self.api.post(json=self.data_post_add_pet)
        self.assertEqual(resp.status_code, 200, "Check Status Code is 200")
        self.assertEqual(json.loads(resp.text), self.data_post_add_pet, "Check Response JSON data is same as Test Data")
        self.assertJsonSchema(json.loads(resp.text), self.pet_schema, "Check if the Schema of the Response is valid")
        self.assertEqual(
            json.loads(self.api.get(self.data_post_add_pet['id']).text), self.data_post_add_pet,
            "Check that the data is properly stored by Getting Pet Data from '/pet/(pet_id)' API endpoint"
        )

    def test_POST_ADD_02_AddPetToAlreadyExistingPetID(self):
        '''
        Make sure that a petID already exists. (Should exist as per previous test case)
        Post an updated Test Data JSON to "/pet/" API endpoint.
        Make Sure that the schema and data of the response is correct.
        Make Sure that the data is updated by Getting the data using "/pet/(pet-id)/" API endpoint.
        '''
        # Check Data for Pet ID Exists
        oldPetData = self.api.get(self.data_post_add_pet['id'])
        self.assertEqual(oldPetData.status_code, 200, "Check that the Status Code is 200 (OK)")
        # Change Test Data (Change 'status' to 'sold' or 'pending')
        if self.data_post_add_pet['status'] in ['available', 'pending']:
            self.data_post_add_pet['status'] = 'sold'
        else:
            self.data_post_add_pet['status'] = 'pending'
        # Post Updated Data to the "/pet/" API endpoint and run Tests
        resp = self.api.post(json=self.data_post_add_pet)
        self.assertEqual(resp.status_code, 200, "Check Status Code is 200")
        self.assertEqual(json.loads(resp.text), self.data_post_add_pet, "Check Response JSON data is same as Test Data")
        self.assertJsonSchema(json.loads(resp.text), self.pet_schema, "Check if the Schema of the Response is valid")
        newPetData = self.api.get(self.data_post_add_pet['id'])
        self.assertEqual(json.loads(newPetData.text), self.data_post_add_pet,
                         "Check that the data is properly stored by Getting Pet Data from '/pet/(pet_id)' API endpoint")
        self.assertNotEqual(json.loads(newPetData.text), json.loads(oldPetData.text),
                            "Check that Old Data is different from New Data")
        self.assertEqual(json.loads(newPetData.text)['status'], self.data_post_add_pet['status'],
                         "Check that the updated Test Data is correct on the new Data")

    def test_POST_ADD_03_InvalidPetData_01_BadID(self):
        '''
        Post a invalid test data with Bad ID.
        Check that the Status Code is 405.
        TODO: Bug: Status Code from API is 500
        '''
        # Change Test Data
        self.data_post_add_pet['id'] = (2**64)+1
        # Post Updated Data to the "/pet/" API endpoint and run Tests
        resp = self.api.post(json=self.data_post_add_pet)
        self.assertEqual(resp.status_code, 405, "Check that response status code is 405 for bad data")

    def test_POST_ADD_03_InvalidPetData_02_WrongDataType(self):
        '''
        Post a invalid test data with Bad Type for Category (Send List instead of Dict).
        Check that the Status Code is 405.
        TODO: Bug: Status Code from API is 500
        '''
        # Change Test Data
        self.data_post_add_pet['category'] = []
        # Post Updated Data to the "/pet/" API endpoint and run Tests
        resp = self.api.post(json=self.data_post_add_pet)
        self.assertEqual(resp.status_code, 405, "Check that response status code is 405 for bad data")

    def test_POST_ADD_03_InvalidPetData_03_WrongDataTypeForExistingPetID(self):
        '''
        Make sure that a petID already exists. (Should exist as per previous test case)
        Post a invalid test data with Bad Type for Category (Send List instead of Dict).
        Check that the stored data is not changed.
        Check that the Status Code is 405.
        TODO: Bug: Status Code from API is 500
        '''
        # Check Data for Pet ID Exists
        oldPetData = self.api.get(self.data_post_add_pet['id'])
        self.assertEqual(oldPetData.status_code, 200, "Check that the Status Code is 200 (OK)")
        # Change Test Data
        self.data_post_add_pet['category'] = []
        # Post Updated Data to the "/pet/" API endpoint and run Tests
        resp = self.api.post(json=self.data_post_add_pet)
        newPetData = self.api.get(self.data_post_add_pet['id'])
        self.assertEqual(json.loads(newPetData.text), json.loads(oldPetData.text),
                         "Check that Pet Data is not changed")
        self.assertEqual(resp.status_code, 405, "Check that response status code is 405 for bad data")
