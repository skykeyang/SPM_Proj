
import unittest
import json

from werkzeug import Response, test
from Person import app

#######################################################Done by Soh Keyang###########################################

   ###################Testing App route in Person##################

    ######APP ROUTE /person##########
class TestPerson_route(unittest.TestCase):
    # IF STATUS CODE=200
    def test_person_200(self):
        test1 = app.test_client(self)
        data = test1.get("/person")
        statuscode = data.status_code
        self.assertEqual(statuscode,200)

    def test_engineer_200(self):
        test1 = app.test_client(self)
        data = test1.get("/engineer")
        statuscode = data.status_code
        self.assertEqual(statuscode,200)
    
    def test_hr_200(self):
        test1 = app.test_client(self)
        data = test1.get("/hr")
        statuscode = data.status_code
        self.assertEqual(statuscode,200)

    
    # IF RESULT RETURNED IN IS JSON
    def test_person_json(self):
        test1 = app.test_client(self)
        data = test1.get("/person")
        self.assertEqual(data.content_type, "application/json")

    def test_engineer_json(self):
        test1 = app.test_client(self)
        data = test1.get("/engineer")
        self.assertEqual(data.content_type, "application/json")

    def test_hr_json(self):
        test1 = app.test_client(self)
        data = test1.get("/hr")
        self.assertEqual(data.content_type, "application/json")


    # # CHECK CONTENT OF GET METHOD
    def test_person_get(self):
        test2 = app.test_client(self)
        data =test2.get("/person")
        data_content = json.loads(data.data)
        self.assertEqual(1, data_content['data']['Person'][0]['id'])
        self.assertEqual('Ally', data_content['data']['Person'][0]['name'])
        self.assertEqual('ally@engineer.com', data_content['data']['Person'][0]['email'])
        self.assertEqual('engineer001', data_content['data']['Person'][0]['pwd'])

    def test_engineer_get(self):
        test2 = app.test_client(self)
        data =test2.get("/engineer")
        data_content = json.loads(data.data)
        self.assertEqual('C101-C1, C102-C2, C103-C2', data_content['data']['Person'][0]['engineer_completed_courses'])

    
    def test_trainer_get(self):
        test2 = app.test_client(self)
        data =test2.get("/trainer")
        data_content = json.loads(data.data)
        self.assertEqual(761, data_content['data'][0]['trainer_id'])
        self.assertEqual('C101-C1, C101-C2, C101-C3, C102-C1, C102-C2, C102-C3, C201-C1, C201-C2, C202-C1, C202-C2, C301-C1, C301-C2, C301-C3, C302-C1, C302-C2, C302-C3', data_content['data'][0]['trainer_course_class_id'])

    def test_hr_get(self):
        test2 = app.test_client(self)
        data =test2.get("/hr")
        data_content = json.loads(data.data)
        self.assertEqual(366, data_content['data'][0]['hr_id'])
        self.assertEqual('C101, C102, C103, C104, C205, C305', data_content['data'][0]['courses_assigned'])



if __name__ == '__main__':
    unittest.main()

