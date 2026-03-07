## Prerequisite Installation
Sebelum install Minikube, pastikan:

- **Virtualization** diaktifkan (Cek di Task Manager → Performance → CPU → Virtualization: **Enabled**).
- **Hyper-V atau Docker Desktop** sudah terinstal (pilih salah satu sebagai driver Minikube).

Jika belum ada **Docker Desktop**, kamu bisa **aktifkan Hyper-V**:
```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -NoRestart
```


### Install Minikube

```
winget install Kubernetes.minikube
```

### Start your cluster
```
minikube start
```

### Interact with your cluster

```
minikube start
```

```
minikube dashboard
```