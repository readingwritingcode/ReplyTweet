#!/usr/bin/python3
# This is a module for Replies with status or with media.
# for a a list of status.
# End of info.
import time

def replylistIds(status,ids_for_reply,api):
        ''' Reply for a list of ids status with a specific status. 
        '''
        for id_rep in ids_for_reply:
                print(id_rep)
                api.update_status(status,id_rep,auto_populate_reply_metadata=True)
                time.sleep(0.5)
        return "done"


def replylistIdsWithMedia(filename,status,ids_for_reply,api):        
        for id_rep in ids_for_reply:
                print(id_rep)
                api.update_with_media(filename=filename,status=status,in_reply_to_status_id=id_rep,auto_populate_reply_metadata=True)
                time.sleep(0.5)
        return "done"

if __name__ =="__main__":
	print('''
This is a module for reply whit status or media 
for a list of target status.
'''		)
