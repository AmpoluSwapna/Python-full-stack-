user_details = {}
user_details['batchs'] = ['PFS6', 'DA', 'JFS']
user_details['students_PFS'] = ['swapna', 'vishala', 'madhu']
user_details['students_DA'] = ['samitha','sharon']
user_details['students_JFS']=['aruna','sneha']
user_details.update
user_details.update({'institue_name':('codegnan'),'branch':('vizag'),
                     'subjects':{'python','mysql','aptitude','softskills'}})
user_details.update({'students_PFS_id':('CGCV1001','CGCV1002','CGCV1003'),
                     'students_DA_id':('CGCV1004','CGCV1005'),
                     'students_JFS_id':('CGCV1006','CGCV1007')})
user_details.update({'daily_exam_time':'7 PM to 11 PM',
                     'daily_exam':'every evening',
                     'total_marks':(30)})
user_details['PFS_students_daily_marks'] = [22,23,24]
user_details['DA_students_daily_marks'] = [25,26]
user_details['JFS_students_daily_marks'] = [27,28]
user_details.update({'weekly_exam_time':'3 PM to 11 PM',
                    'weekly_exam':'every tuesday',
                    'total_marks':(60)})
user_details['PFS_students_weekly_marks'] = [45,46,47]
user_details['DA_students_weekly_marks']= [48,49]
user_details['JFS_students_weekly_marks'] = [50,51]
user_details.update({'ai mock interviews_time':'3 days',
                    'ai mock interviews_day':'every sunday',
                    'ai mock interviews_marks':(10)})
user_details['PFS_students_mock interview_marks'] = [6,7,8]
user_details['DA_students_mock interview_marks'] = [5,9]
user_details['JFS_students_mock interview_marks'] = [4,3]
print(user_details)
                                       
