from flask import Flask, render_template
import os
import subprocess
import time

app = Flask(__name__)

def get_top_output():
    try:
        output = subprocess.check_output(["top", "-b", "-n", "1"], text=True)
        return output
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/htop')
def htop():
    name = "Raj Rajesh Jain" 
    username = os.getlogin()
    ist_time = time.strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = get_top_output()
    return render_template('htop.html', name=name, username=username, ist_time=ist_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)