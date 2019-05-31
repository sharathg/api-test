import unittest
import xmlrunner

# Test 'Delete' Pet
from tests.testDeletePet import TestDeletePet
# Test 'Get' Find By Status
from tests.testGetFindByStatus import TestGetFindByStatus
# Test 'Get' Pet
from tests.testGetPet import TestGetPet
# Test 'Post' Add Pet
from tests.testPostAddPet import TestPostAddPet
# Test 'Post' Edit Pet
from tests.testPostEditPet import TestPostEditPet
# Test 'Post' Upload Image
from tests.testPostUploadImage import TestPostUploadImage
# Test 'Put' Edit Pet
from tests.testPutEditPet import TestPutEditPet


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports', outsuffix="Tests"))
