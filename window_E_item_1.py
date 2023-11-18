#!python
print("content-type: text/html; charset=euc-kr\n")
#import cgi

print('''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>CH's Web</title>
    <link href="Pythonweb.css" rel="stylesheet">
    <h1><a href="window_E_item.py">윈도우 포맷 후 필수 설치파일</a></h1>
</head>
<body>
    <div id="grid">
        <h2 class="active_h2">드라이버</h2>
        <ul>
            <li><a href="https://www.amd.com/ko/support" target="_blank">amd chipset driver (AMD 유저만)</a></li>
            <li><a href="https://www.nvidia.co.kr/Download/index.aspx?lang=kr" target="_blank">nvidia 그래픽 드라이버</a></li>
        </ul>
    </div>
</body>
</html>
''')
