import json
import requests
from bs4 import BeautifulSoup



#gets the main page with the search results
page=requests.get("http://ca.healthinspections.us/napa/search.cfm?start=1&1=1&sd=01/01/1970&ed=03/01/2017&kw1=&kw2=&kw3="
        "&rel1=N.permitName&rel2=N.permitName&rel3=N.permitName&zc=&dtRng=YES&pre=similar")

soup = BeautifulSoup(page.text, 'html.parser')

#gets the inspections form page for each restaurant on the search page
page1=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=409588&dsn=dhd_135")
soup1 = BeautifulSoup(page1.text, 'html.parser')
page2=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=439495&dsn=dhd_135")
soup2 = BeautifulSoup(page2.text, 'html.parser')
page3=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=146218&dsn=dhd_135")
soup3 = BeautifulSoup(page3.text, 'html.parser')
page4=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=341505&dsn=dhd_135")
soup4 = BeautifulSoup(page4.text, 'html.parser')
page5=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=113444&dsn=dhd_135")
soup5 = BeautifulSoup(page5.text, 'html.parser')
page6=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=151253&dsn=dhd_135")
soup6 = BeautifulSoup(page6.text, 'html.parser')
page7=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=146499&dsn=dhd_135")
soup7 = BeautifulSoup(page7.text, 'html.parser')
page8=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=351497&dsn=dhd_135")
soup8 = BeautifulSoup(page8.text, 'html.parser')
page9=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=122210&dsn=dhd_135")
soup9 = BeautifulSoup(page9.text, 'html.parser')
page10=requests.get("http://ca.healthinspections.us/_templates/135/Food%20Inspection/_report_full.cfm?domainID=135&inspectionID=341504&dsn=dhd_135")
soup10 = BeautifulSoup(page10.text, 'html.parser')

#Finds the facility name, address, inspection date, inspection type, inspection grade and compliance violations
#stores the data in a variable and prints it to the console for each restaurant
def main():
    facility_name1 = soup1.find_all('span',class_= 'blackline')[0].get_text()
    address1 = soup1.find_all('span', class_='blackline')[4].get_text()
    inspection_date1 = soup1.find_all('span', class_='blackline')[2].get_text()
    inspection_type1 = soup1.find_all('span', class_='blackline')[9].get_text()
    inspection_grade1 = soup1.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name1)
    print("---------------------------------")
    print("Address: ", address1)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date1)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type1)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade1)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    compliance1_1 = soup1.find_all('td', {'style' : 'text-align: left;'})[34].get_text()
    compliance1_2 = soup1.find_all('td', {'style' : 'text-align: left;'})[43].get_text()
    compliance1_3 = soup1.find_all('td', {'style' : 'text-align: left;'})[47].get_text()
    print(compliance1_1)
    print(compliance1_2)
    print(compliance1_3)
    print("---------------------------------")
    facility_name2 = soup2.find_all('span',class_= 'blackline')[0].get_text()
    address2 = soup2.find_all('span', class_='blackline')[4].get_text()
    inspection_date2 = soup2.find_all('span', class_='blackline')[2].get_text()
    inspection_type2 = soup2.find_all('span', class_='blackline')[9].get_text()
    inspection_grade2 = soup2.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name2)
    print("---------------------------------")
    print("Address: ", address2)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date2)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type2)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade2)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    compliance2_1 = soup2.find_all('td', {'style' : 'text-align: left;'})[5].get_text()
    compliance2_2 = soup2.find_all('td', {'style' : 'text-align: left;'})[34].get_text()
    print(compliance2_1)
    print(compliance2_2)
    print("---------------------------------")
    facility_name3 = soup3.find_all('span',class_= 'blackline')[0].get_text()
    address3 = soup3.find_all('span', class_='blackline')[4].get_text()
    inspection_date3 = soup3.find_all('span', class_='blackline')[2].get_text()
    inspection_type3 = soup3.find_all('span', class_='blackline')[9].get_text()
    inspection_grade3 = soup3.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name3)
    print("---------------------------------")
    print("Address: ", address3)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date3)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type3)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade3)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    compliance3_1 = soup3.find_all('td', {'style' : 'text-align: left;'})[13].get_text()
    compliance3_2 = soup3.find_all('td', {'style' : 'text-align: left;'})[34].get_text()
    print(compliance3_1)
    print(compliance3_2)
    print("-----------------------------------")
    facility_name4 = soup4.find_all('span',class_= 'blackline')[0].get_text()
    address4 = soup4.find_all('span', class_='blackline')[4].get_text()
    inspection_date4 = soup4.find_all('span', class_='blackline')[2].get_text()
    inspection_type4 = soup4.find_all('span', class_='blackline')[9].get_text()
    inspection_grade4 = soup4.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name4)
    print("---------------------------------")
    print("Address: ", address4)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date4)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type4)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade4)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    print("None")
    print("-----------------------------------")
    facility_name5 = soup5.find_all('span',class_= 'blackline')[0].get_text()
    address5 = soup5.find_all('span', class_='blackline')[4].get_text()
    inspection_date5 = soup5.find_all('span', class_='blackline')[2].get_text()
    inspection_type5 = soup5.find_all('span', class_='blackline')[9].get_text()
    inspection_grade5 = soup5.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name5)
    print("---------------------------------")
    print("Address: ", address5)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date5)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type5)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade5)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    compliance5_1 = soup5.find_all('td', {'style' : 'text-align: left;'})[34].get_text()
    compliance5_2 = soup5.find_all('td', {'style' : 'text-align: left;'})[40].get_text()
    print(compliance5_1)
    print(compliance5_2)
    print("------------------------------------")
    facility_name6 = soup6.find_all('span',class_= 'blackline')[0].get_text()
    address6 = soup6.find_all('span', class_='blackline')[4].get_text()
    inspection_date6 = soup6.find_all('span', class_='blackline')[2].get_text()
    inspection_type6 = soup6.find_all('span', class_='blackline')[9].get_text()
    inspection_grade6 = soup6.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name6)
    print("---------------------------------")
    print("Address: ", address6)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date6)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type6)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade6)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    compliance6_1 = soup6.find_all('td', {'style' : 'text-align: left;'})[40].get_text()
    print(compliance6_1)
    print("-----------------------------------")
    facility_name7 = soup7.find_all('span',class_= 'blackline')[0].get_text()
    address7 = soup7.find_all('span', class_='blackline')[4].get_text()
    inspection_date7 = soup7.find_all('span', class_='blackline')[2].get_text()
    inspection_type7 = soup7.find_all('span', class_='blackline')[9].get_text()
    inspection_grade7 = soup7.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name7)
    print("---------------------------------")
    print("Address: ", address7)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date7)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type7)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade7)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    compliance7_1 = soup7.find_all('td', {'style' : 'text-align: left;'})[13].get_text()
    compliance7_2 = soup7.find_all('td', {'style' : 'text-align: left;'})[40].get_text()
    compliance7_3 = soup7.find_all('td', {'style' : 'text-align: left;'})[41].get_text()
    compliance7_4 = soup7.find_all('td', {'style' : 'text-align: left;'})[43].get_text()
    compliance7_5 = soup7.find_all('td', {'style' : 'text-align: left;'})[44].get_text()
    print(compliance7_1)
    print(compliance7_2)
    print(compliance7_3)
    print(compliance7_4)
    print(compliance7_5)
    print("-----------------------------------")
    facility_name8 = soup8.find_all('span',class_= 'blackline')[0].get_text()
    address8 = soup8.find_all('span', class_='blackline')[4].get_text()
    inspection_date8 = soup8.find_all('span', class_='blackline')[2].get_text()
    inspection_type8 = soup8.find_all('span', class_='blackline')[9].get_text()
    inspection_grade8 = soup8.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name8)
    print("---------------------------------")
    print("Address: ", address8)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date8)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type8)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade8)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    print("None")
    print("-----------------------------------")
    facility_name9 = soup9.find_all('span',class_= 'blackline')[0].get_text()
    address9 = soup9.find_all('span', class_='blackline')[4].get_text()
    inspection_date9 = soup9.find_all('span', class_='blackline')[2].get_text()
    inspection_type9 = soup9.find_all('span', class_='blackline')[9].get_text()
    inspection_grade9 = soup9.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name9)
    print("---------------------------------")
    print("Address: ", address9)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date9)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type9)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade9)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    compliance9_1 = soup9.find_all('td', {'style' : 'text-align: left;'})[38].get_text()
    print(compliance9_1)
    print("-----------------------------------")
    facility_name10 = soup10.find_all('span',class_= 'blackline')[0].get_text()
    address10 = soup10.find_all('span', class_='blackline')[4].get_text()
    inspection_date10 = soup10.find_all('span', class_='blackline')[2].get_text()
    inspection_type10 = soup10.find_all('span', class_='blackline')[9].get_text()
    inspection_grade10 = soup10.find_all('td', class_='center bold')[1].get_text()
    print("____________________________________________________________________________")
    print("Facility Name: ", facility_name10)
    print("---------------------------------")
    print("Address: ", address10)
    print("---------------------------------")
    print("Inspection Date: ", inspection_date10)
    print("---------------------------------")
    print("Inspection Type: ", inspection_type10)
    print("----------------------------------")
    print("Inspection Grade: ", inspection_grade10)
    print("-----------------------------------")
    print("Out-of-compliance Violation:")
    print("None")




if __name__ == '__main__':
    main()

#converts the data to json 
data  = {'facility_name1' : soup1.find_all('span',class_= 'blackline')[0].get_text(),
         'address1' : soup1.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date1' : soup1.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type1' : soup1.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade1': soup1.find_all('td', class_='center bold')[1].get_text(),
         'compliance1_1' : soup1.find_all('td', {'style' : 'text-align: left;'})[34].get_text(),
         'compliance1_2' : soup1.find_all('td', {'style' : 'text-align: left;'})[43].get_text(),
         'compliance1_3' : soup1.find_all('td', {'style' : 'text-align: left;'})[47].get_text(),
         'facility_name2' : soup2.find_all('span',class_= 'blackline')[0].get_text(),
         'address2' : soup2.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date2' : soup2.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type2' : soup2.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade2' : soup2.find_all('td', class_='center bold')[1].get_text(),
         'compliance2_1' : soup2.find_all('td', {'style' : 'text-align: left;'})[5].get_text(),
         'compliance2_2' : soup2.find_all('td', {'style' : 'text-align: left;'})[34].get_text(),
         'facility_name3' : soup3.find_all('span',class_= 'blackline')[0].get_text(),
         'address3' : soup3.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date3' : soup3.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type3' : soup3.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade3' : soup3.find_all('td', class_='center bold')[1].get_text(),
         'compliance3_1' : soup3.find_all('td', {'style' : 'text-align: left;'})[13].get_text(),
         'compliance3_2' : soup3.find_all('td', {'style' : 'text-align: left;'})[34].get_text(),
         'facility_name4' : soup4.find_all('span',class_= 'blackline')[0].get_text(),
         'address4' : soup4.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date4' : soup4.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type4' : soup4.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade4' : soup4.find_all('td', class_='center bold')[1].get_text(),
         'facility_name5' : soup5.find_all('span',class_= 'blackline')[0].get_text(),
         'address5' : soup5.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date5' : soup5.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type5' : soup5.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade5' : soup5.find_all('td', class_='center bold')[1].get_text(),
         'facility_name6' : soup6.find_all('span',class_= 'blackline')[0].get_text(),
         'address6' : soup6.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date6' : soup6.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type6' : soup6.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade6' : soup6.find_all('td', class_='center bold')[1].get_text(),
         'compliance6_1' : soup6.find_all('td', {'style' : 'text-align: left;'})[40].get_text(),
         'facility_name7' : soup7.find_all('span',class_= 'blackline')[0].get_text(),
         'address7' : soup7.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date7' : soup7.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type7' : soup7.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade7' : soup7.find_all('td', class_='center bold')[1].get_text(),
         'compliance7_1' : soup7.find_all('td', {'style' : 'text-align: left;'})[13].get_text(),
         'compliance7_2' : soup7.find_all('td', {'style' : 'text-align: left;'})[40].get_text(),
         'compliance7_3' : soup7.find_all('td', {'style' : 'text-align: left;'})[41].get_text(),
         'compliance7_4' : soup7.find_all('td', {'style' : 'text-align: left;'})[43].get_text(),
         'compliance7_5' : soup7.find_all('td', {'style' : 'text-align: left;'})[44].get_text(),
         'facility_name8' : soup8.find_all('span',class_= 'blackline')[0].get_text(),
         'address8' : soup8.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date8' : soup8.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type8' : soup8.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade8' : soup8.find_all('td', class_='center bold')[1].get_text(),
         'facility_name9' : soup9.find_all('span',class_= 'blackline')[0].get_text(),
         'address9' : soup9.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date9' : soup9.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type9' : soup9.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade9' : soup9.find_all('td', class_='center bold')[1].get_text(),
         'compliance9_1' : soup9.find_all('td', {'style' : 'text-align: left;'})[38].get_text(),
         'facility_name10' : soup10.find_all('span',class_= 'blackline')[0].get_text(),
         'address10' : soup10.find_all('span', class_='blackline')[4].get_text(),
         'inspection_date10' : soup10.find_all('span', class_='blackline')[2].get_text(),
         'inspection_type10' : soup10.find_all('span', class_='blackline')[9].get_text(),
         'inspection_grade10' : soup10.find_all('td', class_='center bold')[1].get_text()}
#pythontojson = json.dumps(data)
#print(pythontojson)
with open ("data_file.json", "w") as write_file:
    json.dump(data, write_file)
