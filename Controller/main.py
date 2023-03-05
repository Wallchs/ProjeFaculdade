import webview

html = """


<html>
    <head>
        <body>
            <h1>
                Testando
            </h1>
        </body>
    </head>
</html>


"""


window = webview.create_window('Main', html=html)
webview.start()
