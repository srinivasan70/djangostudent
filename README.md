# djangostudent
student mark application
for adding marks url:http://127.0.0.1:8000/add/addmarks/ method=POST
{
  "data": {
    "rollno": 1235,
    "name": "Sri1",
    "mark1": 92,
    "mark2": 93,
    "mark3": 96,
    "mark4": 98,
    "mark5": 97
  }
}
  for getting data based on rollno
  
  http://127.0.0.1:8000/display/displaymark/ method=POST
  {
  "data": {
    "rollno": 1235
    
  }
}
for displaying marks method = GET http://127.0.0.1:8000/displaylist/displaymarklist/

  
