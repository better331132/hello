import sys, os
import datetime
sa = sys.argv #0번째 : 실행파일, 1번째 : 메시지 부분

now = datetime.datetime.now()
default_msg = "{} 강의".format(now.strftime('%Y-%m-%d'))
commit_msg = default_msg

has_msg = len(sa) >= 2

if has_msg:
    commit_msg = sa[1]

else:
    input_msg = input("Default Message?? (yes: Enter or input message) > ")
    if input_msg != '':
        commit_msg = input_msg

print("commit ... ",commit_msg)
os.system("git pull")
os.system("git add --all")
os.system('git commits -am "{}"'.format(commit_msg))
os.system("git push")