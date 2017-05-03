import os,sys, subprocess, threading
import time
import traceback as tb
from datetime import datetime


class Result:
    def __init__(self, line):
        """
        /dev/mapper/mpatha1 128k 7629 0 1493802739.051225 1493802739.256758 999948288 5.000000
        /dev/mapper/mpatha1 128k 7629 10 1493802742.333494 1493802742.486720 999948288 6.700000
        """
        try:
            self.device, self.bs, xx, int(self.testnum), float(self.start), float(self.finish) , self.size , xx = line.split()
            self.speed = self.size / (self.finish - self.start)

class Performance:
    def __init__(self, resultdir):
        self.resultdir = resultdir
        results = []
        files = glob.glob("%s/*.txt" % self.resultdir)
        for f in files:
            results.append(Result(open(f,"r").readlines()[0]))
        self.results = {}
        for r in results:
            self.

class DiskTest:
    def __init__(self, device, resultdir=None):
        self.device = device
        self.resultdir = resultdir
        
    

    def ddTestRead(self, bs , cnt, tgt, ext, drio=False):
        try:
            print "read thread started ", bs, self.device, ext
            direct = ""
            if drio is True:
                direct = "direct"
            cmd = "dd if=%s of=%s bs=%s count=%s %s " % (self.device, tgt, bs, cnt, direct)
            bas = time.time()
            prs = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            outp, err = prs.communicate()
            bit = time.time()
            res =err.splitlines()[2].decode("utf-8")
            a = res.split()
            size = a[0]
            dur = a[7]
            s = "%s.%s.%s.%d" % (self.device.replace("/",""), bs,cnt, ext)
            ss = "%s.%s.%s.%d" % (self.device, bs,cnt, ext)
            f = open("%s/%s.read.report.txt" % (self.resultdir,s), "w")
            f.write("%s %f %f %d %f\n" % (ss.replace("."," "), bas, bit, int(size), float(dur.replace(",",".")) ))
            f.close()
            print "read thread finished ", bs, self.device, cnt, ext
        except:
            print "problem ", self.device, bs,cnt,tgt,ext 
            tb.print_exc()

    def ddTestWrite(self, bs , cnt, tgt, drio=False):
        try:
            print "write thread started ", bs, self.device, x
            direct = ""
            if drio is True:
                direct = "direct"
            cmd = "dd if=%s of=%s bs=%s count=%s %s " % (self.device, tgt, bs, cnt, direct)
            bas = time.time()
            prs = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            outp, err = prs.communicate()
            bit = time.time()
            res =err.splitlines()[2].decode("utf-8")
            a = res.split()
            size = a[0]
            dur = a[7]
            s = "%s.%s.%s.%d" %  (self.device.replace("/",""), bs,cnt, ext)
            f = open("%s/%s.write.report.txt" % (self.resultdir, s), "w")
            f.write("%d %f" % (int(size), float(dur.replace(",",".")) ))
            f.close()
            print "write thread finished ", bs, self.device, cnt,x
        except:
            print "problem ", self.device, bs,cnt,tgt,ext 


class SystemTest:
    def __init__(self, name =""):
        self.name = name
        self.resultdir = "test-%s"  % datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
        print "results in ",self.resultdir
        os.makedirs(self.resultdir)

        self.disks = {}
        self.bs = {"4k":4096, "32k":32768, "128k":131072, "1M":1048576, "32M": 32* 1048576, "128M":128*1048576 , "256M":256*1048576, "512M":512*1048576}

    def addDisk(self, device):
        if device not in self.disks.keys():
            self.disks[device] = DiskTest(device, resultdir = self.resultdir)
            
    def doTest(self, numdevice, tstsize):
        if numdevice > len(self.disks.values()):
            numdevice = len(self.disks.values())
        
        for bs,bs1 in self.bs.items():
            for x in range(50):
                threads = []
                for devname, device in self.disks.items():
                    cnt = tstsize / bs1
                    if cnt < 1 :
                        cnt=1
                    cnt = str(cnt)
                    t = threading.Thread(target=device.ddTestRead, args=(bs, cnt, "/dev/null",x))
                    threads.append(t)
                    t.start()
                    time.sleep(0.00001)
                for tt in threads:
	            tt.join()
            
            
if __name__ == "__main__":
    s = SystemTest("deneme")
    s.addDisk("/dev/mapper/mpatha1")
    s.addDisk("/dev/mapper/mpathb1")
    s.addDisk("/dev/mapper/mpathc1")
    s.addDisk("/dev/mapper/mpathd1")
    s.addDisk("/dev/mapper/mpathe1")
    s.addDisk("/dev/mapper/mpathf1")
    s.addDisk("/dev/mapper/mpathg1")
    s.addDisk("/dev/mapper/mpathh1")
    s.addDisk("/dev/mapper/mpathi1")
    s.addDisk("/dev/mapper/mpathj1")
    s.addDisk("/dev/mapper/mpathk1")
    s.addDisk("/dev/mapper/mpathl1")
    s.addDisk("/dev/mapper/mpathm1")
    s.addDisk("/dev/mapper/mpathn1")
    s.addDisk("/dev/mapper/mpatho1")
    s.addDisk("/dev/mapper/mpathp1")
    
    s.doTest(24, 1000000000)
