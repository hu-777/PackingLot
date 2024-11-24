from flask import Flask, request, jsonify  
import os  
import base64  
from io import BytesIO  
from PIL import Image  
  
app = Flask(__name__)  
  
UPLOAD_FOLDER = 'chepai'  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  
  
@app.route('/capture_image', methods=['POST'])  
def capture_image():  
    if 'imageData' not in request.json:  
        return jsonify({'error': 'No image data provided'}), 400  
      
    # 获取Base64编码的图片数据并解码  
    base64_data = request.json['imageData'].split(',')[1]  
    image_bytes = base64.b64decode(base64_data)  
      
    # 使用PIL将字节数据转换为图片对象  
    image = Image.open(BytesIO(image_bytes))  
      
    # 确保上传文件夹存在  
    if not os.path.exists(app.config['UPLOAD_FOLDER']):  
        os.makedirs(app.config['UPLOAD_FOLDER'])  
      
    # 生成文件名并保存图片  
    filename = 'capture.jpg'  # 或者你可以根据时间戳或其他规则动态生成文件名  
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  
    image.save(image_path)  
      
    return jsonify({'status': 'success', 'filename': filename})  
  
if __name__ == '__main__':  
    app.run(debug=True)