# Naive-Password-Manager

Default master password: `hello123`

## What

NPM is a locally hosted, easy-to-use command-line password manager

## Why
- easy-to-use
- takes no time to create, retrieve your passwords
- doesn't use ram voracious, long-startup time based db servers
- locally hosted, doesn't 'sell' or 'share' your data, a good option for paranoids

## How
Download and copy the repo to any desired location

**I. For the first time**  
  &emsp;&emsp;Please change the key that will be used to encrypt your password by running `generate_key.py`  
  &emsp;&emsp;You can also, and should, change the master key by running `generate_masterkey.py`
  
**II. Using npm as your regular password manager**
1. Run `main.py`
2. Enter the master key.
3. Enter the profile to use. If profile doesn't exist, enter the profile name you want to create and press `y`.  The profile will become active.
4. A menu will appear.  
    a. Press `1` to create an entry for the profile created/opened in `3`.  
    b. Press `2` to retrieve a password for an app or website present in the profile. The password for the specified appname/website will be copied to the clipboard for 10 seconds.  
    c. Press `3` to change or create a different profile.  
    d. To exit, type `exit`, `q`, `bye` or `goodbye`


------------------------------
Would love to have feedback & suggestions  
GUI version and other features on the way!

  
