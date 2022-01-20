from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '21云盒子 Hello Flask 样例'


# @app.route('/')
# def hello_world():
#     return '21云盒子 Hello Flask 样例'


# class test(Resource):
#     @jwt_required()
#     def post(self):
#
#         return {"result": "fuck"}


# api.add_resource(TEST2, '/test2')

# if __name__ == '__main__':
#     app.run()  # important to mention debug=True