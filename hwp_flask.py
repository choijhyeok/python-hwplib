from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# hwp loader 
def process_hwp(file_path, hwp_jar_path, work_dir):
    try:
        if work_dir == '/app/python-hwplib':
            result = subprocess.run(
                ["python3", "hwp_loader.py", 
                "--hwp_jar_path", hwp_jar_path,
                "--file_path", file_path],
                capture_output=True, 
                text=True,
                encoding='utf-8'
            )
            return result.stdout
        else:
            result = subprocess.run(
                ["python", "hwp_loader.py", 
                "--hwp_jar_path", hwp_jar_path,
                "--file_path", file_path],
                capture_output=True, 
                text=True,
                encoding='utf-8'
            )
            return result.stdout  
    except Exception as e:
        return str(e)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    # 파일 업로드 처리
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400
    
    work_dir = os.getcwd() 
    
    # 업로드 파일 저장
    file_name = file.filename
    file.save(file_name)
    
    # HWP 텍스트 추출 실행
    hwp_jar_path = "./hwplib-1.1.8.jar"
    text = process_hwp(file_name, hwp_jar_path, work_dir)
    
    # 임시 파일 삭제 docker 에서만
    if work_dir == '/app/python-hwplib':
        os.remove(file_name)
    
    return jsonify({
        "filename": file_name,
        "text": text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)