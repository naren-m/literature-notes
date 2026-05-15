---
title: "Ultimate Beginner's Guide to Proxmox GPU Passthrough"
date: 2024-04-09
type: literature
category: "homelab/virtualization"
tags: [proxmox, gpu-passthrough, homelab, virtualization, iommu, vfio]
status: incomplete
source: "https://www.reddit.com/r/homelab/comments/b5xpua/the_ultimate_beginners_guide_to_gpu_passthrough/"
related: []
---

# Ultimate Beginner's Guide to Proxmox GPU Passthrough

Reddit guide (r/homelab) on passing a GPU from a Proxmox hypervisor host through to a Windows 10 virtual machine guest. Bookmarked for a future homelab build.

## Prerequisites

Your hardware should support:

- **VT-d** (Intel) or **AMD-Vi** (AMD) — CPU-level virtualization-assist for I/O.
- **Interrupt remapping**.
- **UEFI BIOS**.

Author's reference rig: Supermicro X9SCM-F, Xeon E3-1220 v2, 16 GB ECC DDR3, mix of GTX 1050 Ti / 1060 GPUs.

## Configuring the Proxmox host

### 1. GRUB kernel parameters

Edit `/etc/default/grub`:

```
# Intel
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on"

# AMD
GRUB_CMDLINE_LINUX_DEFAULT="quiet amd_iommu=on"
```

For stubborn IOMMU groupings (e.g., Xeon E3-12xx series) or single-GPU passthrough, you may also need:

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt \
  pcie_acs_override=downstream,multifunction \
  nofb nomodeset video=vesafb:off,efifb:off"
```

Then `update-grub`.

### 2. Load VFIO modules

Append to `/etc/modules`:

```
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
```

### 3. IOMMU interrupt remapping

```
echo "options vfio_iommu_type1 allow_unsafe_interrupts=1" > /etc/modprobe.d/iommu_unsafe_interrupts.conf
echo "options kvm ignore_msrs=1" > /etc/modprobe.d/kvm.conf
```

### 4. Blacklist GPU drivers on the host

```
echo "blacklist radeon"  >> /etc/modprobe.d/blacklist.conf
echo "blacklist nouveau" >> /etc/modprobe.d/blacklist.conf
echo "blacklist nvidia"  >> /etc/modprobe.d/blacklist.conf
```

### 5. Bind the GPU to VFIO

Use `lspci -v` to find the GPU's bus address (e.g., `01:00.0`), then `lspci -n -s 01:00` to get vendor IDs (e.g., `10de:1b81` for the GPU and `10de:10f0` for the HDMI audio device). Feed both IDs to `vfio-pci`:

```
echo "options vfio-pci ids=10de:1b81,10de:10f0 disable_vga=1" > /etc/modprobe.d/vfio.conf
update-initramfs -u
reset
```

## Configuring the Windows 10 VM

### Create the VM (don't start it yet)

- Download the **VirtIO drivers ISO** (fedorapeople.org) in addition to the Windows ISO — needed during install so Windows can see the VirtIO SCSI hard disk.
- Select **VirtIO SCSI** (not VirtIO Block) for the disk and **VirtIO** for the network adapter.
- Under *Options*, set **BIOS = OVMF (UEFI)**, **Machine = q35**, and add an **EFI disk** under *Hardware*.

### Edit the VM config file

In `/etc/pve/qemu-server/<VMID>.conf`:

```
machine: q35
cpu: host,hidden=1,flags=+pcid
args: -cpu 'host,+kvm_pv_unhalt,+kvm_pv_eoi,hv_vendor_id=NV43FIX,kvm=off'
```

The `hv_vendor_id=NV43FIX` and `kvm=off` flags hide the hypervisor from NVIDIA's consumer driver, which otherwise throws **Code 43** when it detects a VM.

### Attach the GPU as a PCI device

In the VM's *Hardware* tab → *Add → PCI Device*:

- All Functions: **Yes**
- Rom-Bar: **Yes**
- Primary GPU: **No** (initially)
- PCI-Express: **Yes** (requires `machine: q35`)

### ROM file workaround (if needed)

If passthrough fails with the default ROM:

1. Download a matching ROM from techpowerup.com, or dump it yourself:

   ```
   cd /sys/bus/pci/devices/0000:01:00.0/
   echo 1 > rom
   cat rom > /usr/share/kvm/<your-gpu>.bin
   echo 0 > rom
   ```

2. Reference it in the VM config:

   ```
   hostpci0: 01:00,pcie=1,romfile=<your-gpu>.rom
   ```

3. NVIDIA 10XX-series ROMs may need patching — see sk1080/nvidia-kvm-patcher or Matoking/NVIDIA-vBIOS-VFIO-Patcher.

## Installing Windows

- Boot the VM; during install, click *Browse* → VirtIO CD-ROM → `vioscsi\w10\amd64` to load the SCSI driver, then `NetKVM\w10\amd64` for networking.
- Switch the CD-ROM back to the Windows ISO before continuing.
- After first Windows reboot, stop the VM and unmount the Windows ISO.
- Enable Windows Remote Desktop so you can connect after disabling the noVNC console.
- In the VM's *Hardware* tab, set *Display = None (none)*. Restart the VM.
- Install the NVIDIA driver from within Windows. If plain install fails, use GeForce Experience as a fallback.

## Why it was captured

Bookmarked as a reference for an eventual homelab project where a single workstation runs Proxmox on bare metal and passes a discrete GPU to a Windows VM for gaming or ML workloads.

## Related reading (from the article's citations)

- Proxmox Wiki — [PCI Passthrough](https://pve.proxmox.com/wiki/Pci_passthrough)
- [Explaining `csm`, `efifb=off` boot GPU manually](https://passthroughpo.st/explaining-csm-efifboff-setting-boot-gpu-manually/)
- [VFIO FAQ on VGA passthrough](http://vfio.blogspot.com/2014/08/vfiovga-faq.html)
- Heiko Sieger — [IOMMU groups: what you need to consider](https://heiko-sieger.info/iommu-groups-what-you-need-to-consider/)
- Proxmox Wiki — [Windows 10 guest best practices](https://pve.proxmox.com/wiki/Windows_10_guest_best_practices)

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/2240a3646ae04a89bf418491f73f2c74). See [[notion-migration]].*
