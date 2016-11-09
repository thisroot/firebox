import firebox as fb

serPort = fb.findDevice('stimulator')
if(serPort):
    data = []
    data.append("<fire,200,5>")
    fb.sendMessage(serPort,data)
