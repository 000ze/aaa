import socket
sk =socket.socket()         #生成socket实例
sk.bind(("127.0.0.1",8001)) #绑定IP和端口
sk.listen()                 #监听



while 1:
    conn,_=sk.accept()    #获取与客户端的连接
    data=conn.recv(8096)  #接受客户端发来的请求
    '''print(data)
    data_str=str(data,encoding='utf-8')  #字节转str
    l1=data_str.split("\r\n")
    l2=l1[0].split(' ')
    print(l2)
    url=l2[1]
    print(url)
    #按照http协议的格式发消息'''
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html;charset=utf-8\r\n\r\n')
    with open('html5.html','rb') as f:
            res=f.read()
    conn.send(res)     #字体变黑
    conn.close()

