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
print("t: Install Theme")
print("u: Uninstall Packages")
print("q: Quit")
while True:
    cmd = input('ipkg>')
    if cmd == "i":
        pkg = input("Package to install: ")
        giturl = f"https://github.com/ipkg-macos/iotr/releases/download/v1.0.0/{pkg}.zip"
        data = requests.get(giturl).content
        if data == b"Not Found":
            print("Invalid Package")
            break
        zipfile.ZipFile(io.BytesIO(data)).extractall(f"/opt/packages/{pkg}")
    elif cmd == "u":
        pkg = input("Package to uninstall: ")
        shutil.rmtree(f"/opt/packages/{pkg}")
    elif cmd == "t":
        pkg = input("Theme to install: ")
        shutil.copytree(pkg, f"/opt/packages/themes/{pkg.split('/')[-1]}")
        for file in os.listdir(f"/opt/packages/themes/{pkg.split('/')[-1]}"):
            print(file)
            if file.split('/')[-1] == "Utilities":
                pass
            elif file.split('/')[-1][0] == ".":
                pass
            else:
                os.system(f"cp -R /opt/packages/themes/{pkg.split('/')[-1]}/{file.split('/')[-1]}/Contents/Resources/*.icns /Applications/{file.split('/')[-1]}/Contents/Resources/")
        
        for file in os.listdir(f"/opt/packages/themes/{pkg.split('/')[-1]}/Utilities"):
            print(file)
            if pkg.split('/')[-1][0] == ".":
                pass
            else:
                os.system(f"cp -R /opt/packages/themes/{pkg.split('/')[-1]}/Utilities/{file.split('/')[-1]}/Contents/Resources/*.icns /Applications/Utilities/{file.split('/')[-1]}/Contents/Resources/")
    elif cmd == "q":
        print("Quitting...")
        sys.exit(0)
    else:
        print("Invalid Command")
