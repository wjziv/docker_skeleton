import os
from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

class TestClass:
    def __init__(self):
        self.l = []
    def append_i(self,i):
        self.l.append(i)

@app.route('/', methods=['POST', 'GET'])
def main():
    print(request)

    instance = TestClass()

    thread_list = []
    for i in range(1, 100000):
        t = threading.Thread(target=instance.append_i, args=(i,))
        thread_list.append(t)

    for thread in thread_list:
        thread.start()
        thread.join()

    a = len(instance.l)
    b = instance.l[123:132]
    print(a)
    print(b)

    res = {
        'len' : a,
        'sample': b
    }
    
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', 
            port=int(os.environ.get('PORT', 8080)))
