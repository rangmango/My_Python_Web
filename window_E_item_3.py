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
    <h1>윈도우 포맷 후 필수 설치파일</h1>
</head>
<body>
    <div id="grid">
        <h2 class="active_h2">내가 필요한것</h2>
        <ul>
            <li><a href="https://code.visualstudio.com/" target="_blank">비주얼 스튜디오 코드</a></li>
            <li><a href="https://store.steampowered.com/about/" target="_blank">스팀</a></li>
            <li><a href="https://download.battle.net/ko-kr/desktop" target="_blank">배틀넷</a></li>
            <li><a href="https://o.steinberg.net/en/support/downloads.html" target="_blank">큐베이스</a></li>
        </ul>
    </div>
</body>
</html>

''')
