# Define a class called Router. Each router has a model name, a software version, and an IP
# address for management. When an instance of this class is created, the value to these fields
# are passed into the __init__ method. 





# Once completed, we can create an instance of Router.
class Router:
    def __init__(self, model_name, software_version, IP_address):
        self.model_name=model_name
        self.software_version=software_version
        self.IP_address=IP_address
router1 = Router("iosV", "15.6.7", "10.10.10.1")
print(f"Router Model:{router1.model_name}")
print(f"Software Version:{router1.software_version}")
print(f"IP Address:{router1.IP_address}")
# write code to print the details of the router

