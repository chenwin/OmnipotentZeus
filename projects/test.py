# TESTS TO RUN
# CONFIGURATION INFORMATION

from datetime import datetime

project_id = 'c-edgehosting-20150902'
# Please enter the start date for this test in YYYYMMDD (e.g., 20150115 for January 15TH, 2015)
startdate_input = datetime.now().strftime('%Y%m%d-%H%M')
operating_system = 'windows'  # windows

# Please mark with a y (indicating yes) for each test you want to run
system_tests = 'n'  # Geekbench 3 suite
disk_rand = 'n'  # fio random read and random write
disk_seq = 'n'  # fio sequential read and sequential write
internal_net_tests = 'n'  # iperf internal network tests
iozone_tests = 'y'  # iozone tests

# DISK INFORMATION
# If you selected yes for disk_rand or disk_seq, then you have to fill out this information
fio_blocksize = '4'  # please enter the block size in kilobytes
fio_filesize = '16'  # please enter the file size in megabytes
fio_numjobs = '8'  # please enter the number of copies of the test that you would like to run
fio_runtime = '60'  # how long would you like this test to run for in seconds
fio_direct = 'y'  # if direct I/O is required (bypass cache), please mark y
fio_async = 'y'

# iozone
iozone_blocksize = fio_blocksize + 'k'
iozone_filesize = fio_filesize + 'm'
iozone_numjobs = fio_numjobs

fio_rand_rw = 'randrw'  # Please say randread for random read, randwrite for random write, and randrw to do both operations
fio_rand_rw = '--rw=' + fio_rand_rw

fio_seq_rw = 'rw'  # Please say read for sequential read, write for sequential write, and rw to do both operations
fio_seq_rw = '--rw=' + fio_seq_rw

# disk conversions; please don't mess with these variables
fio_blocksize = '--bs=' + fio_blocksize + 'k'
fio_filesize = '--size=' + fio_filesize + 'M'
spider_hatchlings = int(fio_numjobs)
fio_numjobs = '--numjobs=' + fio_numjobs
fio_runtime = '--runtime=' + fio_runtime
fio_json_file = 'fio.json'
fio_filename = '--name=fio_disk'

if fio_async == 'y':
    fio_async_engine = '--ioengine=windowsaio'

if fio_direct == 'y':
    fio_direct_val = 'Direct'
    fio_direct = '--direct=1'
else:
    fio_direct_val = 'Cached'
    fio_direct = '--direct=0'

# INTERNAL NETWORK INFORMATION
# If you selected yes for internal network tests, then you have to fill out this information
internal_net_time = '60'  # Please enter the time, in seconds, that you want iperf to run

# TIMING
# Timing variables to help keep the sequence of events. To adjust the time in between runs, input a sleeptime (in seconds).
# To specify the number of iterations this testing should complete, please input an integer for iterations.
# Duration and duration value will limit the time the suite will be running for.
# Either duration or number of iterations must complete in order for the testing to stop.
sleeptime = 0
iterations = 1
# iterations = 5000000
duration = 24
duration_value = "hours"  # please enter seconds, minutes, hours, or days
if duration_value.lower() == "seconds":
    duration = duration
elif duration_value.lower() == "minutes":
    duration = duration * 60
elif duration_value.lower() == "hours":
    duration = duration * 3600
elif duration_value.lower() == "days":
    duration = duration * 86400

textnotifications = 'n'

# GEEKBENCH LICENSE
# Email and Key for unlocking the license
email = 'contact@cloudspectator.com'
key = 'tqw3g-d4myf-mqy2u-zifzg-wzidc-yo7mp-dulwf-5zsu7-yggfs'

geekbench_install_dir = 'C:\Program Files (x86)'
fio_install_dir = 'C:\Program Files (x86)'
iozone_install_dir = 'C:\Program Files (x86)\Benchmarks\Iozone3_414'
