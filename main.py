import ctypes, sys

def main():
    from os import system
    from platform import win32_edition as edition
    from platform import release
    from threading import Thread
    import nopopups
    print(f"Windows {edition()} Edition detected!")
    print("\nInstalling product key...")

    keys = {
        "Home": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
        "Home N": "3KHY7-WNT83-DGQKR-F7HPR-844BM",
        "Home Single Language": "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
        "Home Country Specific": "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR",
        "Professional": "W269N-WFGWX-YVC9B-4J6C9-T83GX",
        "Professional N": "MH37W-N47XK-V7XM9-C7227-GCQG9",
        "Education": "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
        "Education N": "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
        "Enterprise": "NPPR9-FWDCX-D2C8J-H872K-2YT43",
        "Enterprise N": "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"
    }

    key = keys[edition()]

    system(f"slmgr /ipk {key}")
    print(f'Product key "{key}" successfully installed!')
    print("\nChanging the KMS server...")
    system("slmgr /skms kms10.msguides.com")
    print("KMS server successfully set to: kms10.msguides.com")
    print("\nActivating system...")
    system("slmgr /ato")
    print(f"Windows {release()} {edition()} Edition activated successfully!\n")
    nopopups.stop()
    print("Press any key to exit...")
    system("pause >nul")
    sys.exit()
    
    
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    main()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)