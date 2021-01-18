#! /usr/bin/python3
# This program reply to last five tweets of the all cd senators. 
# End of Info.

import sys
import authtwtr
import idstsMany
import replies


def main(path_to_file,status):
    '''
Input: path_to_file, status
    '''
    api=authtwtr.authtwtr()
    screen_names=idstsMany.makeScreenNames(path_to_file)
    ids_for_reply=idstsMany.makeListIdforReply(screen_names,api)
    replies.replylistIds(status,ids_for_reply,api)

if __name__=="__main__":
    path_to_file=sys.argv[1]
    status= sys.argv[2]
    main(path_to_file,status)
