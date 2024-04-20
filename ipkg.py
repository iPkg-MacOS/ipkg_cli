import os
import sys
import shutil
import requests
import zipfile
import io
if sys.platform != 'darwin':
    print("ERROR: iPkg is a jailbreaking tool for MacOS. Please run it on MacOS.")
    sys.exit(1)

print("iPkg: Package Manager for Jailbroken MacOS")
print("Enter Command:")
print("i: Install Packages")
print("u: Uninstall Packages")
print("q: Quit")
while True:
    cmd = input('ipkg>')
    if cmd == "i":
        pkg = input("Package to install: ")
        giturl = f"https://github.com/ipkg-macos/iotr/releases/download/v1.0.0/{pkg}.gz"
        data = requests.get(giturl).content
        zipfile.ZipFile(io.BytesIO(data)).extractall(f"/opt/packages/{pkg}")
        shutil.move(pkg, "/opt/packages")
    elif cmd == "u":
        pkg = input("Package to uninstall: ")
        shutil.rmtree(f"/opt/packages/{pkg}")
    elif cmd == "q":
        print("Quitting...")
        sys.exit(0)
    else:
        print("Invalid Command")
