# apicall
Using this we will get tha data in json format through run IP address , first we have to run api.py file to get the IP address after run IP address on browser will get a simple flask application page with help of index.html file with a paragraph to get the data in json format have to write url  for getting the data in JSON which will get in api.py file....



Here packages are required for this(install it from project interpreter) is- Flask,Flask-mysqldb, mysqlclient, requests, mysql-connector-python.
I have made here a index.html file which you will have to make on another template directory.

make a api.py file from selecting it from projectname(in my case project name is apidemo).

after api.py file creation you can run the api.py file and you will get an Ip address (http://127.0.0.1:5000)click on it you will get 
simple flask application and you will see a paragraph which is written in index.htmlfile.

to get the course id and name of coure in json format paste this on server -http://127.0.0.1:5000/app/api/courses/all

make a test.py file selecting it from projectname and run this you will get the data in terminal with 200 response.

in test.py file file when I am trying to get data with argument getting the error, for getting data in argument have to write('http://127.0.0.1:5000/app/api/courses?id=1 or 2 or 3') in test.py for getting the result with argument.


I have made a dbintegration file to fetch the data from the database which we insert in database table name id in with column courseID and courseName problem is dbintegration.py file is running without error but not getting the IP address as i have got during the run of api.py file might be some connection issue with database 
