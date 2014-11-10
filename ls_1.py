#e!/usr/bin/python3
import ls_2
import argparse
import os
parser = argparse.ArgumentParser(
        description='List information about the FILEs (the current directory by defaoult)')
parse.add_argument('files',metavar='File', default='.', nargs='*',
        help='The files about which the information will be listed' )
parser.add_argument('-l', '--long', action='store_true',
        help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true',                           help='do not ignore entries starting with .')
parser.add_argument('-A', '--almost_all', action='store_true',
        help='do not list implied . and ..')
parser.add_argument('-H', '--human_readable', action='store_true',
        help='with -l and/or -s, print human readable sizes')
parser.add_argument('-i', '--inode', action='store_true',                            help=' print the index number of each file')
parser.add_argument('-n', '--numeric_uid_gid', action='store_true',
         help=' with -l, list numeric user and group IDs')
parser.add_argument('-R', '--recursive', action='store_true',
         help='list subdirectories recursively')
args = parser.parse_args()

n=0
num_of_args = len(args)
while n < num_of_args:
    filename_list = output.get_filename_list(args.files[n],args.all,args.almost_all)
    m=0
    num_of_files = len(fielname.list)
    while m<num_of_files:
        print(output.gen_line(filename_list[m],args.long,args.inode,args.human_readable))
        m +=1
    n +=1

exit()

