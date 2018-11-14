import sys, os

def auto_update_git():
    if os.name == 'nt':
        os.system('git add --all')
        os.system('git commit -am "12345"')
        os.system('git push')

auto_update_git()