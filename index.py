#!python
print("content-type: text/html; charset=euc-kr\n")
#import cgi

print('''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>CH's Web
    </title>
    <link href="1.css" rel="stylesheet">  <!-- css 파일을 외부에서 가져와서 모든 html에 적용하는 방법-->
    <h1>HTML</h1>
</head>
<body>
    <ul>
        <li><a href="window_E_item.py">윈도우 포맷 후 필수 설치파일</a></li>
        <img src="window_image.jfif" width="400px">
        <li><a href="important_shortcut_keys.html">Visual Studio Code 중요한 단축키 모음</a></li>
        <img src="visualstudio_image.png" width="400px">
    </ul>
</body>
</html>
''')
