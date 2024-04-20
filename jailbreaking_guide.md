# How to Jailbreak your Mac
## Step 1
### Apple Silicon
Hold Down the Power Button until your Mac turns off. Then Release and Continue holding the power button until you see `Loading Startup Options` Appear onscreen. Click `Options`.
### Intel
Hold Down the Power Button until your Mac turns off. Then Release and Hold down the Option + Power keys until your mac shows the starup options. Choose the disk with `Recovery` in it.
## Step 2
Go to Utilities/Terminal in the menu and type `csrutil disable` into the console.
## Step 3
Congrats! You have Jailbroken your Mac! Boot back into MacOS and download the ipkg.py file, then install it with the following commands:
```
sudo mv <path/to/ipkg.py/file> /usr/local/bin/ipkg
sudo chmod +x /usr/local/bin/ipkg
```
Now reload your terminal windows.
Congrats! You can use the ipkg command to install packages from the relases page of this repo.
