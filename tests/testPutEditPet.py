import json

from helpers.baseTest import BaseTest


class TestPutEditPet(BaseTest):

    base_url = "https://petstore.swagger.io/v2/pet"

    def setUp(self):
        super().setUp()
        self.data_put_edit_pet = self.get_testdata("put_edit_pet.json")
        # Remove Pet using the ID if it exists
        if self.api.get(self.data_put_edit_pet['id']).status_code != 404:
            self.api.delete(self.data_put_edit_pet['id'])

    def test_PUT_01_EditExistingPet(self):
        '''
        Add a pet by POST to "/pet/" and sending a JSON as data of the pet.
        Edit a pet using PUT to "/pet/" and sending a JSON as data for editing the pet.
        Make sure that the schema and data of the response is correct.
        Make Sure that the data is stored by Getting the data using "/pet/(pet-id)/" API endpoint.
        '''
        # Add Pet
        oldPetData = self.api.post(json=self.data_put_edit_pet)
        self.assertEqual(oldPetData.status_code, 200)
        # Update Test Data
        self.data_put_edit_pet['name'] = "New Persie"  # Change Name
        self.data_put_edit_pet['category']['name'] = "Rare Cats"  # Change Category Name
        # Send Pet Data using Put and run Tests
        resp = self.api.put(json=self.data_put_edit_pet)
        self.assertEqual(resp.status_code, 200, "Check that the Status Code is 200")
        self.assertJsonSchema(json.loads(resp.text), self.pet_schema, "Check that the Response Scheme is valid.")
        newPetData = json.loads(self.api.get(self.data_put_edit_pet['id']).text)
        self.assertNotEqual(json.loads(oldPetData.text), newPetData,
                            "Check that the Pet Data is is not the old data")
        self.assertEqual(newPetData['name'], self.data_put_edit_pet['name'],
                         "Check that the Name of the Pet is updated")
        self.assertEqual(newPetData['category']['name'], self.data_put_edit_pet['category']['name'],
                         "Check that the Name of the Category is updated")

    def test_PUT_02_EditANonExistingPetID(self):
        '''
        Delete the Pet (Is Done in the SetUp method)
        Edit a pet using PUT to "/pet/" and sending a JSON as data for editing the pet.
        Check that Response Status Code is 404.
        TODO: Bug: API Adds the Pet if the pet data is NotFound.
        '''
        # Send Pet Data using Put and run Tests
        resp = self.api.put(json=self.data_put_edit_pet)
        self.assertEqual(resp.status_code, 404, "Check that the Status Code is 404")

    def test_PUT_03_EditPetWithInvalidID(self):
        '''
        Update Test data with an Invalid ID.
        Edit the pet using PUT to "/pet/" and sending a JSON as data for editing the pet.
        Check that Response Status Code is 400.
        TODO: Bug: Status Code from API is 500
        '''
        # Update the test data with an Invalid ID
        self.data_put_edit_pet['id'] = "asdasd"
        # Send Pet Data using Put and run Tests
        resp = self.api.put(json=self.data_put_edit_pet)
        self.assertEqual(resp.status_code, 400, "Check that the Status Code is 400")

    def test_PUT_04_EditPetWithInvalidJSON(self):
        '''
        Create an Invalid Test data. (Empty JSON)
        Edit the pet using PUT to "/pet/" and sending a JSON as data for editing the pet.
        Check that Response Status Code is 405.
        TODO: Bug: API Adds a default pet to a random huge negative id.
        '''
        # Create an Invalid Test data. (Empty JSON)
        invalidJSON = json.loads('{"random_id": 0, "name": "No Idea"}')
        # Send Pet Data using Put and run Tests
        resp = self.api.put(json=invalidJSON)
        self.assertEqual(resp.status_code, 405, "Check that the Status Code is 405")