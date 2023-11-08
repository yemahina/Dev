import requests
import json
import argparse


# with open('reporteT.json', 'r') as report_file:
#     trivy_report = json.load(report_file)

url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = ${{ secrets.API_KEY_YEM }}

# def get_products():
#     headers = {
#         'accept': 'application/json',
#         'Authorization': api_key
#     }
    
#     gp = requests.get(url_api.format(method='products'), headers=headers, verify=False)
    
#     if gp.status_code == 200:
#         print(json.dumps(gp.json(), indent=4))
#         print("Create product con éxito.")

# def create_product():
#     headers = {
#         'accept' : 'application/json',
#         'Content-Type': 'application/json',
#         'Authorization' : api_key 
#     }
    
#     body = {
#          "tags": [
#              ""
#         ],    
#         "name": "ProductFG",
#         "description": "Demo",
#         "prod_numeric_grade": 2147483647,
#         "business_criticality": "very high",
#         "platform": "web service",
#         "lifecycle": "construction",
#         "origin": "third party library",
#         "user_records": 2147483647,
#         "revenue": "04652832.",
#         "external_audience": True,
#         "internet_accessible": True
#     }

#     cp = requests.post(url_api.format(method='products'), headers = headers, json = body, verify = False)
    
#     print(cp.status_code)
    
#     if cp.status_code == 201:
#         print(json.dumps(cp.json(), indent=4))
#         print("Create product con éxito.")

def upload(file_report, type_scan):
    headers = {
        'Authorization': api_key,
        'accept': 'application/json'
    }

    # # Cargar el archivo 'reporte.json'
    # with open('reporteT.json', 'rb') as report:
    #     files = {'report': ('reporteT.json', report)}

    report = {
        'file' : open(file_report,'rb')
    }

    body = {
        'product_name': 'WebGoat',
        'engagement_name': 'yemahina',
        'product_type_name': 'Research and Development',
        'active': True,
        'verified': True,
        'scan_type': type_scan,
        'minimum_severity' : 'Info',
        'close_old_findings': False,
        'test_title': 'yo'
    }

    rp = requests.post(url_api.format(method='import-scan/'), data=body, files=report, headers=headers, verify=False)

    print(rp.status_code)
    if rp.status_code == 201:
        print(json.dumps(rp.json(), indent=4))
        print("Archivo 'reporte.json' subido con éxito.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', dest='file',help='Nombre del Reporte', required=True)
    parser.add_argument('--type-scan', '-t', dest='type_scan',help='Nombre del escaner', required=True)
    args = parser.parse_args()
    # get_products()  # Puedes llamar a esta función aquí si es necesario
    # create_product()
    upload(args.file, args.type_scan)
