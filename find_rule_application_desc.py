#module that pulls the rule applition type
from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint

# Setup
if not sys.warnoptions:
	warnings.simplefilter("ignore")

def find_rule_application_type (param_host, param_api_key, param_api_version, param_rule_application_type_id):
    configuration = deepsecurity.Configuration()
    configuration.host = param_host
    # Authentication
    configuration.api_key['api-secret-key'] = param_api_key 

    # Initialization
    # Set Any Required Values
    api_instance = deepsecurity.ApplicationTypesApi(deepsecurity.ApiClient(configuration))
    application_type_id = param_rule_application_type_id
    api_version = param_api_version
    try:
        api_response = api_instance.describe_application_type(application_type_id, api_version)
        return api_response
        #pprint(api_response)
    except ApiException as e:
        print("An exception occurred when calling ApplicationTypesApi.describe_application_type: %s\n" % e)

