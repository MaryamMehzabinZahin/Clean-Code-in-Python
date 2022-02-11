from modules import judges
from modules.apiHandler import ApiCaller

'''
Refresh offline data
'''

'''
Vjudge Login
'''
vj_username = input("Please enter your vjudge username: ")
vj_password = input("Please enter your vjudge password: ")

vjudge_user = judges.Vjudge(vj_username, vj_password)
vjudge_user.downloadSubmissions()



'''
UVa Login
'''
uva_username = input("Please enter your UVa username: ")
uva_password = input("Please enter your UVa password: ")

uva_user = judges.UVA(uva_username, uva_password)
uva_user.submitAll(submit_solved_ones = False, limit_submission_count = 10)



'''
CodeForces Login
'''
cf_username = input("Please enter your CodeForces username: ")
cf_password = input("Please enter your CodeForces password: ")

cf_user = judges.CF(cfusername, cfpassword)
cf_user.submitAll(submit_solved_ones = False, limit_submission_count = 10)


'''
LightOJ Login
'''
loj_user = judges.LOJ()
loj_user.submitAll(submit_solved_ones = False, limit_submission_count = 10)


'''
SPOJ Login
'''
spoj_username = input("Please enter your SPOJ username: ")
spoj_password = input("Please enter your SPOJ password: ")

spoj_user = judges.SPOJ(spojusername, spojpassword)
spoj_user.submitAll(submit_solved_ones = False, limit_submission_count = 20)