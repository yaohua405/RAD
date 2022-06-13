import getopt
import sys
import DataStructureDefinition
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    inputPath = ""
    predict = False
    save = False
    filename = ""
    all = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:psf:a", [])
    except getopt.GetoptError as err:
        usage()
        sys.exit()
    for o, a in opts:
        if o == "-i":
            inputPath = a
        elif o == "-p":
            predict = True
        elif o == "-s":
            save = True
        elif o == "-h":
            usage()
            sys.exit()
        elif o == "-f":
            filename = a
        elif o == "-a":
            all = True
        else:
            assert False, "unhandled option"
        
    DataStructureDefinition.parse_log(inputPath, filename, predict, save, all)
    print("Complete. Press enter key to exit.")
    input()

def usage():
    print("\nProgram usage:\n", 
            "-i (input path) -> use provided log location instead of default\n",
            "-p              -> return a prediction of the events analyzed\n",
            "-s              -> Do not delete log files after analyzing them\n",
            "-f (input file) -> Only analyze the file given\n",
            "-a              -> Analyze all logs files in the target folder (not recommended)\n\n",
            "If program is not run as admin it will request admin rights and run in a new window\n")

if is_admin():
    main()

else:
    # if application was not run as admin, open new instance as admin 
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)