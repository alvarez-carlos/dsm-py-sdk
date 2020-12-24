from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint

# Setup
if not sys.warnoptions:
	warnings.simplefilter("ignore")

def find_rules_ids(param_host, param_api_key, param_api_version):
    configuration = deepsecurity.Configuration()
    configuration.host = param_host
    
    # Authentication
    configuration.api_key['api-secret-key'] = param_api_key
    # Initialization
    # Set Any Required Values
    api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(configuration))
    api_version = param_api_version
    expand_options = deepsecurity.Expand()
    expand_options.add(expand_options.none) 
    expand = expand_options.list()
    overrides = False
    try:
        api_response = api_instance.list_computers(api_version, overrides=overrides)
 
        #Getting the array of rule's ids
        rule_ids = api_response.computers[0].intrusion_prevention.rule_ids
        computer_name = api_response.computers[0].host_name
        return rule_ids, computer_name

    except ApiException as e:
        print("An exception occurred when calling ComputersApi.list_computers: %s\n" % e)
