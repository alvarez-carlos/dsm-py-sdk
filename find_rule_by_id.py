#module that pulls the rule information
from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint

# Setup
if not sys.warnoptions:
	warnings.simplefilter("ignore")

def find_rule_by_id (param_host, param_api_key, param_api_version, rule_id):
    configuration = deepsecurity.Configuration()
    configuration.host = param_host
    # Authentication
    configuration.api_key['api-secret-key'] = param_api_key 

    # Initialization
    # Set Any Required Values
    api_instance = deepsecurity.IntrusionPreventionRulesApi(deepsecurity.ApiClient(configuration))
    intrusion_prevention_rule_id = rule_id
    api_version = param_api_version
    try:
        api_response = api_instance.describe_intrusion_prevention_rule(intrusion_prevention_rule_id, api_version)
        #return the rule's information
        return api_response
        #pprint(api_response)
    except ApiException as e:
        print("An exception occurred when calling IntrusionPreventionRulesApi.describe_intrusion_prevention_rule: %s\n" % e)
