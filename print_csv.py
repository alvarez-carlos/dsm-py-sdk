import csv

def print_csv(param_list):
    with open("Report.csv", 'w') as csvfile:
        csv_headers = ['Computer Name','Identifier','Name','Application Type','Priority','Severity','Detect Only','Type','CVE',	'CVSS Score']
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=csv_headers)
        writer.writeheader()
        for rule in param_list:
            writer.writerow({
                'Computer Name': rule['computer_name'],
                'Identifier': rule['identifier'],
                'Name': rule['name'],
                'Application Type':rule['application_type'], 
                'Priority':rule['priority'],
                'Severity':rule['severity'],
                'Detect Only': rule['detect_only'],
                'Type': rule['type'],
                'CVE':rule['cve'],
                'CVSS Score': rule['cvss_score']
               })

