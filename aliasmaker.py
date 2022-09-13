import os

print("""
▞▀▖▜ ▗                    ▐
▙▄▌▐ ▄ ▝▀▖▞▀▘ ▞▀▖▙▀▖▞▀▖▝▀▖▜▀ ▞▀▖▙▀▖
▌ ▌▐ ▐ ▞▀▌▝▀▖ ▌ ▖▌  ▛▀ ▞▀▌▐ ▖▌ ▌▌
▘ ▘ ▘▀▘▝▀▘▀▀  ▝▀ ▘  ▝▀▘▝▀▘ ▀ ▝▀ ▘
""")
print("github.com/dmytroitt")

alias_nm = str(input("Alias name: "))
alias_cntnt = str(input("Alias content: "))
alias = "alias "+alias_nm+"='"+alias_cntnt+"'"

os.system("touch /etc/profile.d/00-aliases.sh")
with open("/etc/profile.d/00-aliases.sh", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write(alias)
    print("Restart to save the changes! ")
    exit()
