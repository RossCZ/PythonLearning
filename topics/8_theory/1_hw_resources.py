import psutil  # https://psutil.readthedocs.io/en/latest/


print("Memory")
print(psutil.virtual_memory())
print()

print("CPU")
print(psutil.cpu_count())
print(psutil.cpu_percent(percpu=True))
print()

print("Processes")
print(psutil.pids())
print()

print("Disk")
for diskpart in psutil.disk_partitions():
    print(diskpart)
print(psutil.disk_usage("C:/"))
print()

print("Network")
print(psutil.net_io_counters())
print()

print("Sensors")
print(psutil.sensors_battery())
print()
