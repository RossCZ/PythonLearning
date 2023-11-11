import psutil  # https://psutil.readthedocs.io/en/latest/


print("Memory")
print(psutil.virtual_memory())
print()

print("CPU")
print(psutil.cpu_count())
print(psutil.cpu_percent())
print()

print("Disk")
for diskpart in psutil.disk_partitions():
    print(diskpart)
print(psutil.disk_usage("C:/"))
