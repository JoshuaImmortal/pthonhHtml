import webbrowser
table = open('table.html', 'w')
style = open('styles.css', 'w')
style_template = """
        *{
            margin:0;
            box-sizing:border-box;
        }
        #wrapper{
            border: .2rem solid red;
        }
        table{
            border: .2rem ridge blue;
            width:95%;
            margin:0 auto;
            height:90vh;
        }
"""
html_template = """<html lang = 'en'>
<head>
<meta charset= 'utf-8'>
<meta name='viewport' content='width=device-width'>
<meta http-equiv= 'X-UA compatible' content= 'IE-edge'>
<link rel = "stylesheet" href = "styles.css">
<title>PYTHON TABLE</title>
</head>
<div id = 'wrapper'>
    <table table border="1" cellspacing="3" cellpadding="20">
        <caption>PROGRAMMING CLASS TIME TABLE</caption>
        <thead>
            <tr>
                <th>Days/time</th>
                <th>9:00 - 10:00</th>
                <th>10:00 - 11:00</th>
                <th>11:00 - 12:00</th>
                <th>1:00 - 2:00</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>Mon</th>
                <td>Web Development</td>
                <td>Basic html</td>
                <td rowspan="3" class='break'>Break</td>
                <td>CSS</td>
            </tr>
            <tr>
                <th>Tue</th>
                <td colspan="2">Cyber Security</td>
                <td>CSS</td>
            </tr>
            <tr>
                <th>Wed</th>
                <td>Data Analysis</td>
                <td>UI/UX</td>
                <td>Web Design</td>
            </tr>
            <tr>
                <th>Thu</th>
                <td>UI/UX</td>
                <td>Break</td>
                <td colspan="2">Web  Design</td>
            </tr>
            <tr>
                <th>Fri</th>
                <td colspan="2">Web Development</td>
                <td>Break</td>
                <td>Project Defense</td>
            </tr>
        </tbody>
    </table>
</div>
</html>"""
table.write(html_template)
style.write(style_template)
table.close()
style.close()
webbrowser.open('table.html')