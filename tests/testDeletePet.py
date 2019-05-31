from helpers.baseTest import BaseTest


class TestDeletePet(BaseTest):

    base_url = "https://petstore.swagger.io/v2/pet"

    def setUp(self):
        super().setUp()
        self.data_post_add_pet = self.get_testdata("post_add_pet.json")

    def test_DELETE_01_DeleteExistingPet(self):
        '''
        Add a pet by POST to "/pet/" endpoint using the JSON data.
        Delete the pet using the JSON data ID
        Check that the Response Status Code is 200
        Check that the Data is deleted by using GET to "/pet/{pet-id}/" and checking the Status Code is 404
        '''
        # Add Pet
        self.assertEqual(self.api.post(json=self.data_post_add_pet).status_code, 200, "Check that the Pet was added")
        # Delete the Pet and run Tests
        resp = self.api.delete(self.data_post_add_pet['id'])
        self.assertEqual(resp.status_code, 200, "Check that Status Code is 200")
        resp = self.api.get(self.data_post_add_pet['id'])
        self.assertEqual(resp.status_code, 404, "Check that the Status Code is 404")

    def test_DELETE_02_DeleteAlreadyDeletedPetID(self):
        '''
        Delete the pet with an Already Deleted Pet ID (Use the ID of the above Test)
        Check the Status Code is 404
        '''
        resp = self.api.delete(self.data_post_add_pet['id'])
        self.assertEqual(resp.status_code, 404, "Check that the status code is 404")

    def test_DELETE_03_DeleteWithInvalidID(self):
        '''
        Delete the pet with an Invalid ID and Check the Status Code is 400
        TODO: Bug: Status Code from API is 404 as it does not consider the ID as Invalid
        '''
        resp = self.api.delete("ABC")
        self.assertEqual(resp.status_code, 400, "Check that the status code is 400")