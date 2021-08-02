d = {
    "Organization_Name":"AP_Police",
    "Corporate_Email_Address:": "ap_police@apgov.org",
    "StartDate": "2021-07-19 15:16:03.185502",
    "EndDate":"2021-12-19 15:16:03.185502",
    "Zip/Postal_Code:":"521369",
    "Entity_Status":"active",
    "Ph_no:":"08672_221133"
}
names={'Organization_Name','Corporate_Email_Address','Entity_Status'}
# print(set(names).issubset(d))
if 'Organization_Name' in list(d.keys()) and 'Corporate_Email_Address' in d.keys() and 'Entity_Status' in d.keys():

    print(True)
else:
    print("False")