import pandas as pd
import os
import argparse
import unidecode

def makeFile(args, file):
    df = pd.DataFrame()
    if file[1] == ".csv":
        df = pd.read_csv(args.file[0])
    elif file[1] == ".xlsx":
        df = pd.read_excel("./")
    elif file[1] == ".json":
        df = pd.read_json(args.file[0])


    if args.verbose:
        print(df)
    
    if args.csv:
        df.to_csv(args.Output[0]+".csv")
    if args.excel:
        df.to_excel(args.Output[0]+".xlsx")
    if args.json:
        df.to_json(args.Output[0]+".json")




parser = argparse.ArgumentParser()


parser.add_argument("-o", "--Output", help = "Show Output", required=True, nargs=1)
parser.add_argument("-f", "--file", help = "Imput file", required=True, nargs=1)
parser.add_argument("-v", "--verbose", action='store_const', const=True)
parser.add_argument("-xlsx", "--excel", action='store_const', const=True)
parser.add_argument("-csv", action='store_const', const=True)
parser.add_argument("-json", action='store_const', const=True)

args = parser.parse_args()


if args.Output:
    print("Displaying Output as: % s" % args.Output)

fileShenannigans = os.path.splitext(args.file[0])
print(args.file)

makeFile(args, fileShenannigans)

