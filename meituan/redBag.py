import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg['Text']

itchat.auto_login()
itchat.run()