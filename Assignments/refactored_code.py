from modules import judges
from modules.apiHandler import ApiCaller

'''
Vjudge Login
'''

vj_username = input("Please enter your vjudge username: ")
vj_password = input("Please enter your vjudge password: ")

vjudge_user = judges.vjudge(vj_username, vj_password)
vjudge_user.download_submissions()

'''
UVa Login
'''
uva_username = input("Please enter your UVa username: ")
uva_password = input("Please enter your UVa password: ")

uva_user = judges.uva(uva_username, uva_password)
uva_user.submit_all(submit_solved_ones = False, limit_submission_count = 10)



'''
CodeForces Login
'''
cf_username = input("Please enter your CodeForces username: ")
cf_password = input("Please enter your CodeForces password: ")

cf_user = judges.cf(cfusername, cfpassword)
cf_user.submitall(submit_solved_ones = False, limit_submission_count = 10)


'''
LightOJ Login
'''
loj_user = judges.loj()
loj_user.submit_all(submit_solved_ones = False, limit_submission_count = 10)


'''
SPOJ Login
'''
spoj_username = input("Please enter your SPOJ username: ")
spoj_password = input("Please enter your SPOJ password: ")

spoj_user = judges.spoj(spojusername, spojpassword)
spoj_user.submitAll(submit_solved_ones = False, limit_submission_count = 20)