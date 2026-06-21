#nested if-else
'''salary=40000
credit_score=720
existing_loan=400000
if salary>=30000:
    if credit_score >= 750 :
        print("premium category")
    elif credit_score > 650 and credit_score < 749:
        print("standard category")
        if existing_loan > 500000:
            print("downgraded")
    else:
        print("not applicable")
else:
    print("rejected")'''

#fraud detection
'''order_amount=12000
is_new_user='yes'
location_match="yes"
if order_amount>=10000:
    if is_new_user=="yes":
        if location_match=="yes":
            print("Allowed")
        else:
            print("allowed")
    else:
        print("allowed")
else:
    print("allowed")'''

#University grading
'''t_marks=77
p_marks=79
if t_marks >= 40 and p_marks >= 40:
    avg_marks=(t_marks+p_marks)//2
    if avg_marks >= 75 :
        print("Distiction")
    elif 60<avg_marks <74:
        print("First class")
    elif 50<avg_marks<59:
        print("student passes")
    else:
        print("student fails")'''



#cab booking
'''rate=30
distance=10
peak_hours="yes"
premium_user="yes"
base_fare=rate*distance
if peak_hours=="yes":
    base_fare+=(base_fare*0.20)
    if premium_user=="yes":
        base_fare-=(base_fare*0.10)
print(base_fare)'''

#smart security
motion_detected="yes"
time="night"
owner_home="no"
if motion_detected=="yes":
    if time=="night":
        if owner_home=="no":
            print("alarm")
        else:
            print("notification")
    else:
        print("nothing")



