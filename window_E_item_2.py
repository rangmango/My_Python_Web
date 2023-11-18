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
        <h2 class="active_h2">필수템</h2>
        <ul>
            <li><a href="https://kr.bandisoft.com/bandizip/" target="_blank">반디집(압축풀기)</a></li>
            <li><a href="https://tv.kakao.com/guide/potplayer" target="_blank">팟플레이어 64비트 (동영상, 음악파일 재생)</a></li>
            <li><a href="https://kr.bandisoft.com/honeyview/" target="_blank">꿀뷰(사진파일 재생)</a></li>
            <li><a href="https://www.voidtools.com/ko-kr/downloads/" target="_blank">Everything(컴퓨터 파일 검색)</a></li>
            <li><a href="https://apps.microsoft.com/detail/9NBLGGH516XP?hl=ko-kr&gl=KR" target="_blank">Eartrumpet(사운드컨트롤)</a></li>
            <li><a href="https://kakao.io/" target="_blank">카카오톡 pc버전</a></li>
            <li><a href="OfficeSetup.exe" target="_blank">마이크로소프트 오피스 2013(설치파일)</a></li>
            <li><a href="https://www.microsoft.com/ko-kr/education/products/office" target="_blank">마이크로소프트 오피스 2013(홈페이지)</a></li>
        </ul>
    </div>
</body>
</html>

''')
