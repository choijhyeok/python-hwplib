# python-hwplib
[hwplib 바로가기](https://github.com/neolord0/hwplib)

hwplib 패키지 python에서 쉽게 사용할 수 있게 만든 github repo 입니다.

- .hwp 파일의 text를 추출할때 가장 좋은 성능을 보였던 java 패키지인 hwplib를 컴파일 해서 사용하는 방식으로 구성했습니다.

&nbsp;

### 필수 설치

- 해당 방법은 Java가 사용하시는 OS에 설치되야 합니다.
  - Maven Compile을 통해서 hwplib github를 .jar로 컴파일을 수행합니다.
    - mac OS 환경에서 Java 8버전으로 컴파일을 수행했으며, 사용한 pom.xml은 'compile_src' 안에 있습니다. (기존 hwplib는 Java 7사용)
    -  Maven 컴파일이 어려울 경우에는 [mvnrepository](https://mvnrepository.com/artifact/kr.dogfoot/hwplib/1.1.7) 에 올려져 있는 것을 다운받으셔도 됩니다. 

- 기본적으로 python JPype package를 이용한 방법이며, hwplib의 다양한 기능중에 한글 추출기능만을 사용합니다.

&nbsp;

### 사용 방법

- JPype 패키지를 설치해 주세요. [pypi](https://pypi.org/project/JPype1/)

```python
!pip install JPype1
```

- Subprocess로 hwp_loader.py에 hwp_jar_path : hwplib jar 위치, file_path : 한글추출을 원하는 .hwp 파일 위치를 넣어주세요

```python
## local
hwp_text = subprocess.run(["python", "hwp_loader.py", "--hwp_jar_path",  'hwplib jar 위치', "--file_path", '한글추출을 원하는 .hwp 파일 위치'], capture_output=True, text=True)

print(hwp_text.stdout)

## fask
python hwp_flask.py

import requests

url = "http://localhost:7860/extract-text"
file_path = "한글추출을 원하는 .hwp 파일 위치"  

with open(file_path, 'rb') as f:
    files = {'file': (file_path, f)}
    response = requests.post(url, files=files)

response.json()
```


### Docker

```python

docker build -t test:test .
docker run -p 7860:7860 test:test

```







