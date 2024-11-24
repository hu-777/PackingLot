from flask import Flask, request, jsonify  
import subprocess  # 用于执行系统命令  
  
app = Flask(__name__)  
  
@app.route('/run_python_script', methods=['POST'])  
def run_python_script():  
    # 这里假设你有一个Python脚本叫做my_script.py，并且它位于与Flask应用相同的目录下  
    # 你也可以指定其他路径或参数  
    result = subprocess.run(['python', 'UI(ad).py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
      
    # 检查脚本是否执行成功  
    if result.returncode == 0:  
        output = result.stdout.decode('utf-8').strip()  
        return jsonify({'success': True, 'output': output}), 200  
    else:  
        error = result.stderr.decode('utf-8').strip()  
        return jsonify({'success': False, 'error': error}), 500  
  
if __name__ == '__main__':  
    app.run(debug=True)