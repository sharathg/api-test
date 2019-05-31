import json

from helpers.baseTest import BaseTest


class TestPostUploadImage(BaseTest):

    base_url = "https://petstore.swagger.io/v2/pet"

    def setUp(self):
        super().setUp()
        self.data_post_add_pet = self.get_testdata("post_add_pet.json")
        # Remove Pet using the ID if it exists
        if self.api.get(self.data_post_add_pet['id']).status_code != 404:
            self.api.delete(self.data_post_add_pet['id'])

    def test_POST_UploadImage_01_UploadImageToValidPetID(self):
        '''
        Add a pet by POST to "/pet/" and sending a JSON as data of the pet.
        Upload an image to the pet-id by POST to "/pet/{pet-id}/uploadImage" where pet-id is valid
        Check that the status code is 200
        Check that the response Message has 'File uploaded to' Text
        '''
        # Add Pet
        oldPetData = self.api.post(json=self.data_post_add_pet)
        self.assertEqual(oldPetData.status_code, 200)
        # Post ImageData and run Tests
        imgFile = self.get_imagefile("cat.jpg")
        resp = self.api.post("{}/uploadImage".format(self.data_post_add_pet['id']), files={'file': imgFile})
        self.assertEqual(resp.status_code, 200, "Check that the Status Code is 200")
        self.assertIn("File uploaded to", json.loads(resp.text)['message'],
                      "Check that the response Message has 'File uploaded to' Text")
        imgFile.close()
        newPetData = self.api.post(json=self.data_post_add_pet)
        self.logger.info(newPetData.text)

    def test_POST_UploadImage_02_UploadImageInvalidPetID(self):
        '''
        Upload an image to the pet-id by POST to "/pet/{pet-id}/uploadImage" where pet-id is invalid (MAX_INT + 1)
        Check that the status code is 404
        '''
        # Post ImageData and run Tests
        imgFile = self.get_imagefile("cat.jpg")
        resp = self.api.post("{}/uploadImage".format((2**64)+1), files={'file': imgFile})
        self.assertEqual(resp.status_code, 404, "Check that the Status Code is 404")

    def test_POST_UploadImage_03_UploadImageNonExistingPetID(self):
        '''
        Depete Pet using DELETE using the Test Data ID
        Upload an image to the pet-id by POST to "/pet/{pet-id}/uploadImage" where pet-id is of the deleted pet
        Check that the status code is 404
        TODO: Bug: API Does uploads image even if the Pet is not present; And gives response status code as 200.
        '''
        # Delete Pet
        resp = self.api.delete(self.data_post_add_pet['id'])
        self.assertEqual(resp.status_code, 200)
        # Post ImageData and run Tests
        imgFile = self.get_imagefile("cat.jpg")
        resp = self.api.post("{}/uploadImage".format(self.data_post_add_pet['id']), files={'file': imgFile})
        self.assertEqual(resp.status_code, 404, "Check that the Status Code is 404")