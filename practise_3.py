


import practise_2


type_x=practise_2.severity_type['severity']
type_x
# priority 
# severity Critical, priority  Critical,
# severity High, priority  High
# severity Medium, priority  Major
# severity Low, priority  Minor


def priority_creation(type_x):
    if type_x=='Critical':
        priority="Critical"
    elif type_x  =="High":
        priority="High"
    elif type_x  =="Medium":
        priority="Major"
    elif type_x  =="Low":
        priority="Minor"  
    return priority
priority_creation(type_x)

