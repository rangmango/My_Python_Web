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
    <h1>{title}</h1>
</head>
<body>
    <ol>
      <h2><li><a href="window_E_item_1.py">{list_0}</a></li></h2>
      <h2><li><a href="window_E_item_2.py">{list_1}</a></li></h2>
      <h2><li><a href="window_E_item_3.py">{list_2}</a></li></h2>
    </ol>
</body>
</html>
'''.format(title="윈도우 포맷 후 필수 설치파일", list_0="드라이버", list_1="필수템", list_2="내가 필요한것"))
