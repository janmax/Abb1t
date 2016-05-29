#essential
try:
    import thread #python2
except ImportError:
    import _thread as thread #python3
try:
    from Queue import * #python2
except ImportError:
    from queue import * #python3
import time

#mod
import gzip, os
import json

class log(object):
    def __init__(self, bot):
        self.bot = bot
        self.queue_in=Queue()
        #self.queue_out=Queue()
        thread.start_new_thread(self.run,())
        self.logdir="logs"

    def run(self):
        while 1: 
            msg=self.queue_in.get() # get() is blocking
            try:
                os.mkdir(self.logdir)
            except:
                pass # exists already
            recv_id=msg['from']['id'] # will be the name of the gz
            with gzip.open("{}.gz".format(os.path.join(self.logdir,str(recv_id))),"a") as fw:
                print(msg)
                fw.write("{}\n".format(json.dumps(msg)))

    def enqueue(self,msg):
        self.queue_in.put(msg)