from subprocess import PIPE, Popen
import psutil
import time
from ISStreamer.Streamer import Streamer
import re

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    y = re.findall(r"(=)(.+)(\')",str(output)) # Pull out just the temperature
    return float(y[0][1])


streamer = Streamer(bucket_name=":computer: Pi5 Performance", bucket_key="piperf1", access_key="INSERT YOUR INITIAL STATE ACCESS KEY HERE")
while True:
    cpu_temperature = get_cpu_temperature()
    cpu_temperature = cpu_temperature * 9.0 / 5.0 + 32.0
    streamer.log("CPU Temperature(F)",format(cpu_temperature,".1f")) 

    cpu_percents = psutil.cpu_percent(percpu=True)
    streamer.log_object(cpu_percents, key_prefix="cpu")

    cpu_percent = psutil.cpu_percent(percpu=False)
    streamer.log("CPU Usage",cpu_percent)

    disk = psutil.disk_usage('/')
    disk_total = disk.total / 2**30    
    streamer.log("Disk Total(GB)",format(disk_total,".1f")) 
    disk_used = disk.used / 2**30
    streamer.log("Disk Used(GB)",format(disk_used,".1f"))
    disk_free = disk.free / 2**30
    streamer.log("Disk Free(GB)",format(disk_free,".1f")) 
    disk_percent_used = disk.percent
    streamer.log("Disk Used(%)",format(disk_percent_used,".1f"))  

    mem = psutil.virtual_memory()
    mem_total = mem.total / 2**20      
    streamer.log("Memory Total(MB)",format(mem_total,".1f")) 
    mem_avail = mem.available / 2**20      
    streamer.log("Memory Available(MB)",format(mem_avail,".1f")) 
    mem_percent_used = mem.percent
    streamer.log("Memory Used(%)",format(mem_percent_used,".1f")) 
    mem_used = mem.used / 2**20
    streamer.log("Memory Used(MB)",format(mem_used,".1f"))  
    mem_free = mem.free / 2**20
    streamer.log("Memory Free(MB)",format(mem_free,".1f")) 

    net = psutil.net_io_counters()
    net_bytes_sent = net.bytes_sent / 2**20      
    streamer.log("Network MB Sent",format(net_bytes_sent,".1f"))  
    net_bytes_recv = net.bytes_recv / 2**20      
    streamer.log("Network MB Received",format(net_bytes_recv,".1f"))  
    net_errin = net.errin    
    streamer.log("Network Errors Receiving",str(net_errin)) 
    net_errout = net.errout    
    streamer.log("Network Errors Sending",str(net_errout)) 
    net_dropin = net.dropin    
    streamer.log("Incoming Packets Dropped",str(net_dropin)) 
    net_dropout = net.dropout    
    streamer.log("Outgoing Packets Dropped",str(net_dropout)) 

    streamer.flush()
    time.sleep(30)