from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint

#modules
from find_rules_ids import find_rules_ids
from find_rule_by_id import find_rule_by_id 
from find_rule_application_desc import find_rule_application_type
from print_csv import print_csv

#parameters
param_host = 'https://cloudone.trendmicro.com/api/'
param_api_key =  'D75ABE1C-A1D4-9B4A-4150-AA85DB24F259:E0A44D87-EB49-2615-87CE-35B9A73707BE:hFLNeow5gRiwVOU6a6NcwNy350ftLIUtIeAbtD0FAnY='
param_api_version = 'v1'

rules_list = []

rules_ids, computer_name =  find_rules_ids(param_host, param_api_key, param_api_version)

#Iterating the array of rule's ids and passing them to the check_rule function so that we can get the information related to that specific rule
for rule_id in rules_ids:
    rule = find_rule_by_id(param_host, param_api_key, param_api_version, rule_id)  
    rule_application_type = find_rule_application_type(param_host, param_api_key, param_api_version, rule.application_type_id) 

    rule_needed_attributes = {
            "computer_name": computer_name,
            "identifier": rule.identifier, 
            "name": rule.name,
            "application_type": rule_application_type.name,
            "priority":rule.priority,
            "severity":rule.severity,
            "detect_only":rule.detect_only,
            "type":rule.type,
            "cve":rule.cve,
            "cvss_score":rule.cvss_score,
            }
    rules_list.append(rule_needed_attributes)
print_csv(param_list=rules_list)
print('Su report ha sido generado con exito!')


