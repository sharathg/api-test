# api-test
Test API (https://petstore.swagger.io/v2/pet)


# Run with Docker (Install and Login to Docker Server)
* IMPORTANT: Give/Share access to work directory to Docker
* Run <code>sh run_with_docker.sh</code> if on Linux/MacOS
* On Windows, use GitBash to run the above code.

  
# Run without Docker

#### Requirements
* Python 3.7 (3.4+)


#### Setup
* Install dependencies from requirements.txt:  
    <code>pip install -r requirements.txt</code>


#### Run Using:
* All Tests with junit xml  
    <code>python runner.py</code>

* All Tests using unittest test detection  
    <code>python -m unittest</code>

* Specific TestFile/TestClass/TestMethod  
    <code>python -m unittest TestFile.TestClass.TestMethod</code>
    * Examples:  
        <code>python -m unittest tests.testPutEditPet</code>  
        Runs all Test Classes and Test Methods inside <code>testPutEditPet</code> file.  
      
        <code>python -m unittest tests.testPutEditPet.TestPutEditPet</code>  
        Runs all Test Methods inside <code>TestPutEditPet</code> Class.  
        
        <code>python -m unittest tests.testPutEditPet.TestPutEditPet.test_PUT_04_EditPetWithInvalidJSON</code>  
        Runs the specific <code>test_PUT_04_EditPetWithInvalidJSON</code> Test


#### Logs and Reports
* Test Reports will be generated in <code>test-reports</code> folder.  
* Test Script Log will be generated as <code>script.log</code>