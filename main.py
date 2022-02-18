import requests


#########################post data##################################
reponse = requests.post('http://localhost:3000/new',
	params={'apiKey':'codepannustudent'},
	data={
		"genus": "Malus",
    	"name": "Dummyhtggdf",
    	"id": 6,
    	"family": "Rosaceae",
    	"order": "Rosales",
    	"carbohydrates": 11.4,
        "protein": 0.3,
        "fat": 0.4,
        "calories": 52,
        "sugar": 10.3,
        "category":"fruit"})
print(reponse.json())
id_to_delete = reponse.json().get('result')['_id']
print(id_to_delete)

########################################Getting all fruits#########################
all_fruits = requests.get('http://localhost:3000/')
print(all_fruits)

###########################################GET by Id##########################

response = requests.get('http://localhost:3000/object/620b51965b3d92516b78355f')
print(response.json())

#############################################################################
############################## Getting by hierarchy #########################
#############################################################################

response = requests.get('http://localhost:3000/name/banana')
print(response.json())

response = requests.get('http://localhost:3000/genus/Mangifera')
print(response.json())


response = requests.get('http://localhost:3000/family/Rosaceae')
print(response.json())

response = requests.get('http://localhost:3000/order/Sapindales')
print(response.json())


###################################################################################
############################# Delete Request #######################################
###################################################################################
deleting = requests.delete(f'http://localhost:3000/{id_to_delete}',params={'apiKey':'codepannustudent'})
print(deleting.json())