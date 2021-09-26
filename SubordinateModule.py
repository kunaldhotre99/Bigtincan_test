
roles = [
{
"Id": 1,
"Name": "System Administrator",
"Parent": 0
},
{
"Id": 2,
"Name": "Location Manager",
"Parent": 1
},
{
"Id": 3,
"Name": "Supervisor",
"Parent": 2
},
{
"Id": 4,
"Name": "Employee",
"Parent": 3
},
{
"Id": 5,
"Name": "Trainer",
"Parent": 3
}
]


users = [
{
"Id": 1,
"Name": "Adam Admin",
"Role": 1
},
{
"Id": 2,
"Name": "Emily Employee",
"Role": 4
},
{
"Id": 3,
"Name": "Sam Supervisor",
"Role": 3
},
{
"Id": 4,
"Name": "Mary Manager",
"Role": 2
},
{
"Id": 5,
"Name": "Steve Trainer",
"Role": 5
}
]

def getSubOrdinates(userID):    # defining the getSubOrdinates fuction
	try:

	    ID_role = users[userID-1]['Role']  #indexing the rolesId from the Users list
	    Sub_roles_list = [i for i in roles if i['Parent']>= ID_role]  # getting a list of subordinate roles using list comprehension
	    Sub_users_list = [users[j] for i in range(len(Sub_roles_list)) for j in range(len(users)) if Sub_roles_list[i]['Id'] == users[j]['Role']] # comparing the list of subordinates roles to the roles list to find subordinates of the user ID
	    if not Sub_users_list : 
	        return "User has no subordinates" # return "User has no subordinates" if the userID has no subordinates
	    else:
	        return Sub_users_list # return the list of all the subordinates in the hierarchy for that userID

	except IndexError:
			return "Value must be between 1 and {}".format(len(users)) # Catch Exception if user enters invalid number for userID

print(getSubOrdinates(1))

