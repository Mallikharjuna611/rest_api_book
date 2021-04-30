

import requests
base_url = 'http://127.0.0.1:8822/'
endpoint_url = 'api/emp_viewset/'

final_url = base_url + endpoint_url

pdata = {
    'empid' : 10,
    'empname' : 'Srinivas',
    'email' : 'sri@123.com',
    'salary' : 20000
}

resp = requests.get(final_url)

# id = input('Enetr id :')
# resp = requests.get(final_url+id+'/')
# resp = requests.post(final_url, pdata)
# resp = requests.put(final_url+ id +'/', pdata)
# resp = requests.delete(final_url+ id +'/')

if resp.status_code==200 :
    print("Status code is: ",resp.status_code)
    try:
        print(resp.json())
    except:
        print('sorry, You are not getting the Json Response from Provider App')

elif resp.status_code==201:
    print("Status code is: ",resp.status_code)
    print(resp.json())
    print('Record created successfuly')

elif resp.status_code == 204:
    print("Status code is: ",resp.status_code)
    print('Record deleted successfully')

elif resp.status_code ==400:
    print("Status code is: ",resp.status_code)
    print('Bad request, Record not created')

elif resp.status_code == 404:
    print("Status code is: ",resp.status_code)
    print('Record not found')

elif resp.status_code == 403:
    print("Status code is: ",resp.status_code)
    print('Method not hitting, csrf token not available')

elif resp.status_code == 500:
    print("Status code is: ",resp.status_code)
    print('Server side exception')

else:
    print("Status code is: ",resp.status_code)
    print('sry unable to do operation')




















#
# import requests
# final_url = "http://127.0.0.1:8899/api/emp_viewset/"
#
# edata = {
#     'empid' : 170,
#     'empname' : 'Abc',
#     'salary' : 15000,
#     'email' : 'abc@123.com'
# }
#
# edata['salary'] = 25000
#
#
# # resp = requests.get(final_url)
#
# # id = input('id :')
# # resp = requests.get(final_url + id)
#
# # resp = requests.post(final_url , pdata)
#
#
# # id = input('Enter id :')
# # resp = requests.delete(final_url+ id)
#
#
# # id = input('Enter id :')
# # sal = input('enter salary :')
#
# # pdata['empid'] = id
# # pdata['salary'] = sal
# # resp = requests.put(final_url + id +"/", pdata)
#
#
# if resp.status_code == 200:
#     try :
#         data = resp.json()
#         print('Status code is :' , resp.status_code)
#         print(data)
#     except:
#         print('Status code is :' , resp.status_code)
#         print('Sorry you are not getting JSON type data.')
#
# elif resp.status_code == 400:
#     print('Status code is :', resp.status_code)
#     print('Please send JSON type data')
#
# elif resp.status_code == 201:
#     print('Status code is :', resp.status_code)
#     print('Data is Created successfully.')
#
# elif resp.status_code == 204:
#     print('Status code is :', resp.status_code)
#     print('Data is deleted successfully.')
#
# elif resp.status_code == 404:
#     print('Status code is :', resp.status_code)
#     print('Requested resource is not available.')
#
# else:
#     print('Status code is :', resp.status_code)
#     print('Sorry something is wrong.')
#
