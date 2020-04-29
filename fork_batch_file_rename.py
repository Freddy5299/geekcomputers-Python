import argparse
import os
def rename_file(work_DIR,old_etx,new_etx):
    for filename in os.listdir(work_DIR):
        temp = os.path.splitext(filename)
        fn, file_etx = temp
        if file_etx == old_etx:
            file_old_etx = new_etx
        else:
            file_old_etx = old_etx

        os.rename(
            os.path.join(work_DIR, filename),
            os.path.join(work_DIR, fn + file_old_etx)
        )
    print(os.listdir(work_DIR))

def parser():
    parser = argparse.ArgumentParser(description='change extension if file in a working directory')
    parser.add_argument('work_dir',metavar='WORK_DIR',type=str,nargs=1,help='the directory where to change extension')
    parser.add_argument('old_ext',metavar='OLD_ETX',type=str,nargs=1,help='old_etx')
    parser.add_argument('new_ext',metavar='NEW_ETX',type=str,nargs=1,help='new_etx')

    return parser

if __name__ == '__main__':
    parser = parser()
    args = vars(parser.parse_args())
    print(args)
    work_dir = args['work_dir'][0]
    old_ext= args['old_ext'][0]
    new_ext = args['new_ext'][0]
    rename_file(work_dir, old_ext, new_ext)