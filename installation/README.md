# Carla Installation Guide

## Prerequisites

Before installing Carla, ensure your system meets the following requirements:

- **Disk Space:** At least 20 GB available
- **GPU:** 6GB GPU capable of running high-intensity graphics
- **Python:** Version 3 or higher
- **Pip:** Version 20.3 or higher

## Common Issues and Fixes

### Pip3 Upgrade Issue

If you encounter problems upgrading `pip3`, run the following command to update your environment variables and apply the changes:

```bash
echo "export PATH=\"/home/USER/.local/bin:\$PATH\"" >> ~/.bashrc && source ~/.bashrc
```

Replace `USER` with your actual username.

## Installation Steps

### Download and Extract Carla

1. Navigate to the [Carla GitHub repository](https://github.com/carla-simulator/carla).
2. Download the latest release suitable for your system.
3. Choose a directory on your system where you want to extract the files.
4. Extract the downloaded archive using a file archiver tool or command line, e.g.,:

```bash
tar -xvf carla.tar.gz -C /path/to/your/directory/
```

Replace `/path/to/your/directory/` with the actual path where you want to extract Carla.

### Running Carla

To run Carla on an Nvidia GPU, which is particularly useful for systems with multiple GPUs, navigate to the Carla installation directory and execute:

```bash
cd /path/to/your/directory/carla
./CarlaUE4.sh -prefernvidia
```

Ensure to replace `/path/to/your/directory/carla` with the actual path to your Carla installation.

This command ensures that Carla prefers Nvidia GPUs over others, optimizing performance.

## Additional Notes

- Make sure you have the proper drivers installed for your Nvidia GPU to ensure optimal performance.
- Regularly check the [Carla GitHub page](https://github.com/carla-simulator/carla) for updates and patches.
