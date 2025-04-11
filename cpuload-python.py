import time
import sys
import argparse
import multiprocessing

def allocate_memory(gb: int, hold_seconds: int = 60):
    try:
        print(f"Allocating {gb} GB of memory...")
        # 1 GB = 1024^3 bytes
        num_bytes = gb * 1024 * 1024 * 1024

        # Allocate a bytearray
        memory = bytearray(num_bytes)
        
        # Touch every page to ensure it's actually allocated
        for i in range(0, len(memory), 4096):  # 4KB page size
            memory[i] = 1

        print(f"Holding memory for {hold_seconds} seconds...")
        time.sleep(hold_seconds)

        # Free memory
        del memory
        print("Memory released.")

    except MemoryError:
        print("Memory allocation failed! Reduce the amount and try again.")
        sys.exit(1)

def cpu_load(load_percentage: int, duration: int):
    print(f"Generating {load_percentage}% CPU load for {duration} seconds...")
    end_time = time.time() + duration
    while time.time() < end_time:
        if time.time() % 100 < load_percentage:
            pass  # Busy-wait to simulate CPU load
        else:
            time.sleep(0.01)  # Sleep to reduce CPU load

def generate_cpu_load_across_cores(load_percentage: int, duration: int):
    num_cores = multiprocessing.cpu_count()
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_load, args=(load_percentage, duration))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Temporary memory and CPU load generator")
    parser.add_argument("--gb", type=int, help="Amount of memory to allocate in GB")
    parser.add_argument("--seconds", type=int, default=60, help="How long to hold memory in seconds")
    parser.add_argument("--cpu", type=int, help="CPU load percentage")
    parser.add_argument("--cpu_duration", type=int, default=60, help="Duration of CPU load in seconds")

    args = parser.parse_args()

    # Run memory load if specified
    if args.gb:
        memory_process = multiprocessing.Process(target=allocate_memory, args=(args.gb, args.seconds))
        memory_process.start()

    # Run CPU load if specified
    if args.cpu:
        generate_cpu_load_across_cores(args.cpu, args.cpu_duration)

    # Wait for memory process to finish if it was started
    if args.gb:
        memory_process.join()
