# CPU and Memory Load Generator

This script generates temporary memory and CPU load based on the options provided. You can use it to allocate memory, generate CPU load, or both.

## Usage

### Memory Load Only

To allocate memory and hold it for a specified duration:

```bash
python cpuload-python.py --gb 2 --seconds 60
```

This command will:
- Allocate 2 GB of memory.
- Hold the memory for 60 seconds.

### CPU Load Only

To generate CPU load for a specified duration:

```bash
python cpuload-python.py --cpu 75 --cpu_duration 60
```

This command will:
- Generate 75% CPU load across all cores.
- Hold the CPU load for 60 seconds.

### Both Memory and CPU Load

To allocate memory and generate CPU load simultaneously:

```bash
python cpuload-python.py --gb 2 --seconds 60 --cpu 75 --cpu_duration 60
```

This command will:
- Allocate 2 GB of memory.
- Hold the memory for 60 seconds.
- Generate 75% CPU load across all cores.
- Hold the CPU load for 60 seconds.

## Arguments

- `--gb`: Amount of memory to allocate in GB.
- `--seconds`: Duration to hold the allocated memory in seconds (default: 60).
- `--cpu`: CPU load percentage.
- `--cpu_duration`: Duration of CPU load in seconds (default: 60).

## Example

To allocate 1 GB of memory and generate 50% CPU load for 30 seconds:

```bash
python cpuload-python.py --gb 1 --seconds 30 --cpu 50 --cpu_duration 30
```

## Notes

- Ensure you have sufficient system resources before running the script.
- Adjust the parameters based on your requirements and system capabilities.

## License

This project is licensed under the MIT License.
