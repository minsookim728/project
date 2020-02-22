"""
def execution():
    user_dict = {'hello': '198.0000'}
    user_dict = execution_1(user_dict)
    print(user_dict)

def execution_1(user_dict):
    user_dict['hello'] = float(user_dict['hello'])
    return user_dict



if __name__=='__main__':
    execution()
"""

a = 12345
a = '{:.4f}'.format(a)
print(type(a))