try:
    import os
    import shutil
    from datetime       import *
    from colorama       import *
    from pystyle        import *
except ImportError:
    os.system("pip install colorama pystyle")
    import os
    import shutil
    from datetime       import *
    from colorama       import *
    from pystyle        import *

init(autoreset=True)

GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN

carfolder = r"C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\content\cars"
collider = os.path.join(os.path.dirname(os.path.abspath(__file__)), "collider.kn5")

def unlockcars(carfolder, collider):
    """
    This function will unlock all the cars you have downloaded in Assetto Corsa. (BYPASSES "NEEDS A DLC" CARS)
    This function goes through all the folders in the cars folder and deletes the collider.kn5 file, and replaces them with one that you already have unlocked.

    NO THIS DOES NOT BREAK YOUR CAR TEXTURES OR ANYTHING. IT JUST REMOVES THE COLLIDER FILE, AND UNLOCKS THE CAR!
    """
    for root, dirs, _ in os.walk(carfolder):
        for d in dirs:
            carpath = os.path.join(root, d)
            colliderfile = os.path.join(carpath, "collider.kn5")
            carname = os.path.basename(carpath)
            time = datetime.now().strftime("%H:%M:%S")
            
            if os.path.exists(colliderfile):
                logger(time, RED, "Deleting current collider...", BLUE, carname)
                os.remove(colliderfile)
            
            logger(time, GREEN, "Unlocked the car!", BLUE, carname)
            shutil.copy(collider, colliderfile)

def logger(time, color1, message, color2, carname):
    """
    Makes cool colors in the console, self-explanatory.
    """
    print(f"{GRAY}[{time}] | {color1}{message} | {color2}{carname}")

if __name__ == "__main__":
    System.Title = "Assetto Corsa Unlock All Cars | Made by: @sevenv1 on github"
    input(f"\n{RED}Press [ENTER] to start...")
    unlockcars(carfolder, collider)
    input(f"\n{RED}Press [ENTER] to exit...")