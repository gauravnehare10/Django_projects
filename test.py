import requests

BASE_URL = 'http://localhost:8000/'
END_POINT = 'view/'

response = requests.get(BASE_URL + END_POINT)

print(response)

student_data = response.json()
print(type(student_data))

for key, val in student_data.items():
    print(f'{key} --> {val}')

print('---------------------------------------------------------')

response = requests.get('http://localhost:8000/view1/')
print(response)

student_data = response.json()
print(type(student_data))

for key, val in student_data.items():
    print(f'{key} --> {val}')


rollno = int(input('Enter Roll No. :'))

response = requests.get('http://localhost:8000/view2/'+str(rollno)+'/')
print(response)

data = response.json()

for key, val in data.items():
    print(f'{key} --> {val}')
