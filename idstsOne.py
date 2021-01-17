#! /usr/bin/python3
# get fifth status fron screen name
# END OF INFO

def getStatusid(screen_name,api):
        '''	get 50 status id for a screen_name
	'''
        lust=api.user_timeline(screen_name, count=50)

        global status_ids
        status_ids=[]
        for idx in range(len(lust)):
                status_ids.append(lust[idx]._json['id_str'])

        return status_ids

if __name__=="__main__":
    print("this is a module")
