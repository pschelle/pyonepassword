import getpass
import os
import sys
parent_path = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
if parent_path not in sys.path:
    sys.path.append(parent_path)

from pyonepassword import (  # noqa: E402
    OP,
    OPSigninException,
    OPGetItemException,
    OPNotFoundException,
    OPConfigNotFoundException
)

def get_password():
    return getpass.getpass(prompt="1Password master password:\n")

def do_signin():
    # Or we'll try to look up account shorthand from your latest sign-in in op's config file
    return OP(vault="Archive", password_func=get_password)


if __name__ == "__main__":
    try:
        op = do_signin()
    except OPSigninException as opse:
        print("1Password sign-in failed.")
        print(opse.err_output)
        exit(opse.returncode)
    except OPNotFoundException as ope:
        print("Uh oh. Couldn't find 'op'")
        print(ope)
        exit(ope.errno)
    except OPConfigNotFoundException as ope:
        print("Didn't provide an account shorthand, and we couldn't locate 'op' config to look it up.")
        print(ope)
        exit(1)

    print("Signed in.")

    vaults = op.list_vaults()
    print (len(vaults), vaults)
    if 0:
        for v in vaults:
            vault = op.get_vault(v['uuid'])
            print (vault)
    newvault = op.create_vault('test')
    print (newvault)