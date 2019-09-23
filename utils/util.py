# Config file for Project
import inspect

URL = "https://10.105.219.23/app/ui/login.jsp"
USERNAME = "admin"
PASSWORD = "admin"

sshUsername = "root"
sshPassword = "cloupia123"
sshServer = "10.105.219.23"

cmd1 = "cd /opt/infra/inframgr"
cmd2 = "tailf logfile.txt"

cmd3 = "cd /opt/infra/bin"
cmd4 = "./dbAdmin.sh connect"
cmd5 = "\n"
cmd6 = "\n"

query1 = "select * from INFRAACCOUNT;"


def whoami():
    return inspect.stack()[1][3]