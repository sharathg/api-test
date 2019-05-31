import json

from helpers.baseTest import BaseTest


class TestPostEditPet(BaseTest):

    base_url = "https://petstore.swagger.io/v2/pet"

    def setUp(self):
        super().setUp()
        self.data_post_add_pet = self.get_testdata("post_add_pet.json")
        # Remove Pet using the ID if it exists
        if self.api.get(self.data_post_add_pet['id']).status_code != 404:
            self.api.delete(self.data_post_add_pet['id'])

    def test_POST_EDIT_01_EditExistingPet_NameAndStatus(self):
        '''
        Add a pet by POST to "/pet/" and sending a JSON as data of the pet.
        Edit a pet using POST to "/pet/" and sending data for editing the pet.
        Check that the status code is 200
        Check that the schema is valid
        Check that data of the response is correct.
        Make Sure that the data is stored by GET to "/pet/(pet-id)/" API endpoint.
        '''
        # Add Pet
        oldPetData = self.api.post(json=self.data_post_add_pet)
        self.assertEqual(oldPetData.status_code, 200)
        # Create a update data dict
        update_data = {
            'name': "{}_UPDATED".format(self.data_post_add_pet['name']),
            'status': "sold" if self.data_post_add_pet['status'] in ['available', 'pending'] else 'pending'
        }
        # Post Update data and run Tests
        resp = self.api.post(self.data_post_add_pet['id'], data=update_data)
        self.assertEqual(resp.status_code, 200, "Check that the Status Code is 200")
        newPetData = json.loads(self.api.get(self.data_post_add_pet['id']).text)
        self.assertNotEqual(newPetData, oldPetData, "Check that the API GET Pet Data is updated")
        self.assertEqual({'name': newPetData['name'], 'status': newPetData['status']}, update_data,
                         "Check that the API GET Data has the proper updated data")

    def test_POST_EDIT_02_EditExistingPet_Name(self):
        '''
        Add a pet by POST to "/pet/" and sending a JSON as data of the pet.
        Edit a pet using POST to "/pet/" and sending data for editing the pet.
        Check that the status code is 200
        Check that the schema is valid
        Check that data of the response is correct.
        Make Sure that the data is stored by GET to "/pet/(pet-id)/" API endpoint.
        '''
        # Add Pet
        oldPetData = self.api.post(json=self.data_post_add_pet)
        self.assertEqual(oldPetData.status_code, 200)
        # Create a update data dict
        update_data = {
            'name': "{}_UPDATED".format(self.data_post_add_pet['name'])
        }
        # Post Update data and run Tests
        resp = self.api.post(self.data_post_add_pet['id'], data=update_data)
        self.assertEqual(resp.status_code, 200, "Check that the Status Code is 200")
        newPetData = json.loads(self.api.get(self.data_post_add_pet['id']).text)
        self.assertNotEqual(newPetData, oldPetData, "Check that the API GET Pet Data is updated")
        self.assertEqual({'name': newPetData['name']}, update_data,
                         "Check that the API GET Data has the proper updated data")

    def test_POST_EDIT_03_EditExistingPet_Status(self):
        '''
        Add a pet by POST to "/pet/" and sending a JSON as data of the pet.
        Edit a pet using POST to "/pet/" and sending data for editing the pet.
        Check that the status code is 200
        Check that the schema is valid
        Check that data of the response is correct.
        Make Sure that the data is stored by GET to "/pet/(pet-id)/" API endpoint.
        '''
        # Add Pet
        oldPetData = self.api.post(json=self.data_post_add_pet)
        self.assertEqual(oldPetData.status_code, 200)
        # Create a update data dict
        update_data = {
            'status': "sold" if self.data_post_add_pet['status'] in ['available', 'pending'] else 'pending'
        }
        # Post Update data and run Tests
        resp = self.api.post(self.data_post_add_pet['id'], data=update_data)
        self.assertEqual(resp.status_code, 200, "Check that the Status Code is 200")
        newPetData = json.loads(self.api.get(self.data_post_add_pet['id']).text)
        self.assertNotEqual(newPetData, oldPetData, "Check that the API GET Pet Data is updated")
        self.assertEqual({'status': newPetData['status']}, update_data,
                         "Check that the API GET Data has the proper updated data")

    def test_POST_EDIT_04_EditPetWithInvalidData(self):
        '''
        Add a pet by POST to "/pet/" and sending a JSON as data of the pet.
        Edit a pet using POST to "/pet/" and sending INVALID data for editing the pet.
        Check that the status code is 405.
        TODO: Bug: API Does not update the Pet if the data is Invalid; But gives response status code as 200.
        Make Sure that the data is not changed by GET to "/pet/(pet-id)/" API endpoint.
        '''
        # Add Pet
        oldPetData = self.api.post(json=self.data_post_add_pet)
        self.assertEqual(oldPetData.status_code, 200)
        # Create a update data dict
        update_data = {
            'name': ['asd', 'zxc']
        }
        # Post Update data and run Tests
        resp = self.api.post(self.data_post_add_pet['id'], data=update_data)
        self.assertEqual(resp.status_code, 405, "Check that the Response Status Code is 405")
        newPetData = json.loads(self.api.get(self.data_post_add_pet['id']).text)
        self.assertEqual(newPetData, oldPetData, "Check that the API GET Pet Data is unchanged")
