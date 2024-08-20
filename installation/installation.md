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
