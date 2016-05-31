#essential
import _thread as thread
from queue import *

#mod
import gtts
import tempfile

class voice:
    def __init__(self, bot):
        self.bot = bot
        self.queue_in=Queue()
        #self.queue_out=Queue()
        thread.start_new_thread(self.run,())
        #self.resttime=0
        #self.lastcmd=0

    def run(self):
        while 1: 
            msg=self.queue_in.get() # get() is blocking
            chat_id=msg.get_chat_id()
            print(".2.")
            if msg.get_text()[:len("/voice")]=="/voice" and len(msg.get_text().split(" "))>=2:
                print("..")
                tts=msg.get_text().split(" ",1)[1].lower().replace("Ä","ae").replace("ä","ae").replace("Ü","ue").replace("ü","ue").replace("Ö","oe").replace("ö","oe").replace("ß","ss")
                print("Voice requesting {}".format(tts))
                temporaryfile=tempfile.TemporaryFile()
                gtts.gTTS(text=tts,lang="de").write_to_fp(temporaryfile)
                temporaryfile.seek(0)
                self.bot.sendAudio(chat_id,temporaryfile,title="Abb0tvoice")
                temporaryfile.close()

    def enqueue(self,msg):
        self.queue_in.put(msg)