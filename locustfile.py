from locust import HttpUser, task, between
import random
import json
import requests
import warnings
warnings.filterwarnings("ignore")

url = "API_Gateway/accesstoken/generateAccessToken"
headers = {'Ocp-Apim-Subscription-Key': 'dskajgfdjkasbdabsda45343434dsfsdfds'}
response = requests.request("GET", url, headers=headers, verify=False)
accesstoken = json.loads(response.text.encode('utf8'))['access_token']
class MyUser(HttpUser):
    wait_time = between(0,9)
    host = "API_Gateway"
    @task
    def api1(self):
        employeeIDs = ['SLALoadTest1447', 'SLALoadTest1441', 'SLALoadTest1628']
        startDates=['2020-08-01', '2020-08-02', '2020-08-03','2020-08-04', '2020-08-05']
        endDates =['2020-08-06', '2020-08-07', '2020-08-08','2020-08-09', '2020-08-10']
        employeeID = random.choice(employeeIDs)
        startDate = random.choice(startDates)
        endDate = random.choice(endDates)
        # client attribute is part of HttpUser class is something similar to requests module in Python
        with self.client.post('/api/apiname/api1', 
                                    json = {'employeeID': employeeID,'startDate': startDate, 'endDate': endDate}, 
                                    headers={"authorization": "Bearer " + accesstoken}, 
                                    verify=False,
                                    catch_response=True) as resp:
            if resp.status_code == 500:
              resp.failure("Database Error")

    @task
    def api2(self):
        employeeIDs = ['SLALoadTest1447', 'SLALoadTest1441', 'SLALoadTest1628']
        employeeID = random.choice(employeeIDs)
        # client attribute is part of HttpUser class is something similar to requests module in Python
        with self.client.post('/api/apiname/api2', 
                                    json = {'employeeID': employeeID}, 
                                    headers={"authorization": "Bearer " + accesstoken}, 
                                    verify=False,
                                    catch_response=True) as resp:
            if resp.status_code == 500:
              resp.failure("Database Error")
    @task
    def api3(self):
        employeeIDs = ['SLALoadTest1447', 'SLALoadTest1441', 'SLALoadTest1628']
        dates =['2020-08-06', '2020-08-07', '2020-08-08','2020-08-09', '2020-08-10']
        employeeID = random.choice(employeeIDs)
        date = random.choice(dates)
        # client attribute is part of HttpUser class is something similar to requests module in Python
        with self.client.post('/api/apiname/api3', 
                                    json = {'employeeID': employeeID, 'date':date}, 
                                    headers={"authorization": "Bearer " + accesstoken}, 
                                    verify=False,
                                    catch_response=True) as resp:
            if resp.status_code == 500:
              resp.failure("Database Error")
    @task
    def api4(self):
        employeeIDs = ['SLALoadTest1447', 'SLALoadTest1441', 'SLALoadTest1628']
        dates =['2020-08-06', '2020-08-07', '2020-08-08', '2020-08-09', '2020-08-10']
        employeeID = random.choice(employeeIDs)
        date = random.choice(dates)
        # client attribute is part of HttpUser class is something similar to requests module in Python
        with self.client.post('/api/apiname/api4', 
                                    json = {'employeeID': employeeID, 'date':date}, 
                                    headers={"authorization": "Bearer " + accesstoken}, 
                                    verify=False,
                                    catch_response=True) as resp:
            if resp.status_code == 500:
              resp.failure("Database Error")