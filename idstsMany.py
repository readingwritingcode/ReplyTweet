import os
import sys
import time
import authtwtr

def makeScreenNames(path_to_file):
        
        with open(path_to_file,'r') as file:
                users=file.readlines()

        global screen_names
        screen_names=[]

        for i in users:
                screen_names.append(i.split(':')[1].strip('@').strip('\n'))
        return screen_names


def getFiveStatusId(screenname,api):
        lut=api.user_timeline(screenname,count=5)
        id_1=lut[0]._json['id_str']
        id_2=lut[1]._json['id_str']
        id_3=lut[2]._json['id_str']
        id_4=lut[3]._json['id_str']
        id_5=lut[4]._json['id_str']
        global five_status_id
        five_status_id=[id_1,id_2,id_3,id_4,id_5]
        return five_status_id

def makeListIdforReply(screen_names, api):

        global ids_for_reply
        ids_for_reply=[]
        for scn in screen_names:
                fsi=getFiveStatusId(scn,api)
                ids_for_reply.extend(fsi)
                time.sleep(0.5)
        return ids_for_reply

def main(path_to_file,api):
        
        ''' For a list of screen names contained in a file,
            Make a list of id status for reply.
            Input: path to file and api.
        '''
        screen_names = makeScreenNames(path_to_file)
        ids_for_reply = makeListIdforReply(screen_names,api)
        return ids_for_reply

if __name__ == "__main__":
        print(
'''This module make ids for reply for a list of screen names'''
                )
        
