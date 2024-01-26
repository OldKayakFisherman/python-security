from argparse import ArgumentParser
import platform
from loganalysis import WindowsLogAnalysis

def analyze_logs():
    
    print (platform.system())

    if platform.system() == "Windows":
        print("Windows!")
        WindowsLogAnalysis().analyze_logs()




if __name__ == "__main__":

   analyze_logs() 

   # parser = ArgumentParser(prog="Security Utilities")

   # subparsers = parser.add_subparsers(help="help for subcommand", dest="subcommand")

   # analyze_parser = subparsers.add_parser('analyze_logs", "analyzes local system logs and performs a high level threat analysis')
   # analyze_parser.add_argument('-v', type=str, required=False, help='')