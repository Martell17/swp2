def app(environ, start_response):
    #data = b"Hello, World!\n"
    qs = environ['QUERY_STRING']
    #qs_split = qs.split('&')
    qr = qs.replace('&','\n')
    #for q in qs_split: print(q)
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
    ])
    return qr
