from flask import Flask, jsonify, render_template, request


app= Flask(__name__)
courses = [
    {
        'courseId':1,
        'courseName':'python programming certification course'
    },
{
        'courseId':2,
        'courseName':'data science certification'
    },
{
        'courseId':3,
        'courseName':'python web development certification'
    },
 {
        'courseId': 4,
        'courseName': 'natural language processing with NLTK'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/api/courses/all')
def show():
    return jsonify(courses)

@app.route('/app/api/courses', methods=['GET'])
def id():
    print('i am here at stop 1')
    if 'id' in request.args:
        id= int(request.args.get('id'))
    else:
        return "unknown request"
    print('i am here at stop -2')
    result=[]

    for course in courses:
        if course(['courseID'])==id:
            result.append(course)
    return jsonify(result)

if __name__ =='__main__':
    app.run(debug=True)