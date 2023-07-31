import webbrowser
form = open('form.html', 'w')
stylus = open('stylus.css', 'w')
stylus_template = """
    *{
        margin:0;
        box-sizing:border-box
    }
    #wrapper{
        border: .5remm solid blue;
    }
    form{
        border: .3rem solid skyblue;
        width:70%;
        margin: 0 auto;
    }
"""
form_template = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width">
    <link rel="styleSheet" href="stylus.css">
    <title>Form_com</title>
</head>
<body>
    <div id = "wrapper">
    <form action='', method=''>
    <input type='text' placeholder='Your Fullname:'>
    <input type='Email' placeholder='Type in your Email:'>
    <input type='Password' placeholder='Type in your password:'>
    <button type='submit'>Save</button>
    </form>
    </div>
</body>
</html>
"""
form.write(form_template)
stylus.write(stylus_template)
form.close()
stylus.close()
webbrowser.open('form.html')