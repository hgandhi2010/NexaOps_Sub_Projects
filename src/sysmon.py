import json
import logging
import os
import shutil
import psutil

logging.basicConfig(
    filename="SysMon.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)


def monitor_system(cpu_threshold, ram_threshold):
    status = "OK"

    "CPU_Metrics"
    cpu_Cores = os.cpu_count()  # hardware lauout
    # physical_cores = psutil.cpu_count(logical=False) #deep performance metrics
    cpu_usage_overall = psutil.cpu_percent(interval=1)  # overall usage metric
    # cpu_usage_percore = psutil.cpu_percent(interval=None, percpu=True) # per-core usage
    if cpu_usage_overall >= cpu_threshold:
        # status = "WARNING"
        logging.warning(
            f"CPU Limit Approaching: the current cpu usage {cpu_usage_overall} exceeded the threshold limits -> {cpu_threshold}!!"
        )
    else:
        logging.info("System Check Complete, CPU resources under control.")

    "RAM_Metrics"
    memory = psutil.virtual_memory()
    total_ram = memory.total / (1024**3)  # total ram of the device.
    # available_ram = memory.available / (1024 ** 3) # total available RAM
    # used_ram = memory.used / (1024 ** 3) # total used RAM
    ram_percentage = memory.percent  # ram Percentage
    if ram_percentage >= ram_threshold:
        # status = "WARNING!"
        logging.warning(
            f"RAM Limit Approaching: the current cpu usage {ram_percentage} exceeded the threshold limits -> {ram_threshold} %!!"
        )
    else:
        logging.info("System Check Complete, RAM resources under control.")

    if cpu_usage_overall >= cpu_threshold or ram_percentage >= ram_threshold:
        status = "WARNING"

    "Disk_Metrics"
    total_disk, used_disk, free_disk = shutil.disk_usage("/")
    total_gb = total_disk / (1024**3)
    used_gb = used_disk / (1024**3)
    available_gb = free_disk / (1024**3)

    payload = {
        "status": status,
        "metrics": {
            "cpu_usage_pct": cpu_usage_overall,
            "ram_usage_pct": ram_percentage,
            "disk_free_gb": round(available_gb, 2),
        },
    }

    return json.dumps(payload)
