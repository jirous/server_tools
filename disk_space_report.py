import shutil
import os.path
import platform
import psutil

# Threshold variable


ThresholdLimit = 100


def percentage(part, whole):
    return round(100 * float(part)/float(whole), 1)


def disk_report():
    if platform.system() == "Windows":
        dl = map(chr, range(65, 91))
        drives = ['{}:'.format(d) for d in dl if os.path.exists("%s:" % d)]
        for i in range(len(drives)):
            total, used, free = shutil.disk_usage(drives[i])
            print("------------\n{}\n------------\nTotal: {}GB\nUsed: {}GB\nFree: {}GB".format(drives[i], total // (2 ** 30), used // (2 ** 30), free // (2 ** 30)))
            if percentage(free, total) < 10:
                print("\n{} drive's free space is {}% threshold\n".format(drives[i].replace(":", ""),percentage(free, total)))
    elif platform.system() == "Linux":
        partitions = psutil.disk_partitions()
        fs = ['{}'.format(d.mountpoint) for d in partitions]
        for i in range(len(fs)):
            total, used, free = shutil.disk_usage(fs[i])
            print("Total {} : %d GB".format(fs[i]) % (total // (2 ** 30)), "Used: %d GB" % (used // (2 ** 30)),"Free: %d GB" % (free // (2 ** 30)))
            if fs[i] == '/' or '/home' and free // (2 ** 30) < ThresholdLimit:
                print("\n{} filesystem's free space is {}% threshold\n".format(fs[i], percentage(free, total)))
    else:
        print("Unknown operating system. Only Linux and Windows operating systems are supported.")


disk_report()

