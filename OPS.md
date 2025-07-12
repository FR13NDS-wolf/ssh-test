## Bench 脚本

**使用**

```text
wget -qO- bench.sh | bash
#或者
curl -Lso- bench.sh | bash
#或者
wget -qO- 86.re/bench.sh | bash
#或者
curl -so- 86.re/bench.sh | bash

#换源
bash <(curl -sSL https://linuxmirrors.cn/main.sh)

VPS检测
bash <(curl -Ls IP.Check.Place) -4

线路回程测试
bash <(curl -L -s https://raw.githubusercontent.com/zhucaidan/mtr_trace/main/mtr_trace.sh)
```

> https://zhuanlan.zhihu.com/p/117547388

## 自启

### 1. **使用 `systemd`**

对于使用 `systemd` 的系统，您可以创建一个服务单元文件。

创建服务单元文件：

```
sudo nano /etc/systemd/system/my-service.service
```

文件内容示例：

```
[Unit]
Description=My Custom Service

[Service]
ExecStart=/path/to/your/command
Restart=always

[Install]
WantedBy=multi-user.target
```

启用并启动服务：

```
sudo systemctl enable my-service.service
sudo systemctl start my-service.service
```

### 2. **使用 `cron`**

您可以使用 `cron` 的 `@reboot` 选项来设置在系统启动时运行的命令。

编辑 `crontab`：

```
crontab -e
```

添加自启命令：

```
@reboot /path/to/your/command
@reboot sleep 600 && echo "System started" > /tmp/reboot.log //等待600s
```

### 3. 使用 `.bashrc`

如果您希望在用户登录时运行某些命令，可以将它们添加到用户的 `.bashrc` 或 `.bash_profile` 文件中。

编辑文件：

```
nano ~/.bashrc
```

```
nano ~/.bash_profile
```

添加命令：

```
/path/to/your/command &
```

### 4. **使用 `/etc/rc.local`**

在某些系统中，可以通过 `/etc/rc.local` 文件添加自启动命令。

编辑文件：

```
sudo nano /etc/rc.local
```

添加命令（确保在 `exit 0` 之前）：

```
/path/to/your/command &
exit 0
```

### 5.使用 update-rc.d



## 后台运行

### 方法 1：使用 `screen` 或 `tmux`

使用 `screen` 或 `tmux` 来启动每个 `frpc` 实例，这样可以确保它们在后台独立运行。

#### 示例脚本

```bash
#!/bin/bash
screen -dm -S frpc2 /home/loophy/frp/frpc -c frpc2.toml
screen -dm -S frpc1 /home/loophy/frp/frp/frpc -c frpc.ini
```

### 方法 3：使用 `nohup`

使用 `nohup` 命令确保 `frpc` 实例在后台运行。

#### 示例脚本

```bash
#!/bin/bash
nohup /home/loophy/frp/frpc -c frpc2.toml > /dev/null 2>&1 &
nohup /home/loophy/frp/frpc -c frpc.ini > /dev/null 2>&1 &
```

### 方法 4：使用 `Type=forking` 和 `ExecStart`

在 systemd 服务配置中，使用 `Type=forking` 和 `ExecStart` 来启动多个 `frpc` 实例。

#### 示例 systemd 配置

```ini
[Unit]
Description=frpc Service
After=network.target

[Service]
Type=forking
ExecStart=/bin/bash -c '/home/loophy/frp/frpc -c frpc2.toml & /home/loophy/frp/frpc -c frpc.ini &'
Restart=always
User=root
Group=root

[Install]
WantedBy=multi-user.target
```

## 编译 fastfetch

1. **克隆仓库：*    `git clone https://github.com/fastfetch-cli/fastfetch.git`
2. **进入项目目录：**  `cd fastfetch`
3. **编译：**:
   - 创建build 目录：`mkdir build`
   - 进入build 目录：`cd build`
   - 使用CMake：`cmake ..`
   - 使用Make：`make`。
   - 安装：`sudo make install`
4. **配置文件**

```
fastfetch --gen TAB
{
  "$schema": "https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json",
  "logo": {
    "type": "auto",        // Logo type: auto, builtin, small, file, etc.
    "source": "arch",      // Built-in logo name or file path
    "width": 65,           // Width in characters (for image logos)
    "height": 35,          // Height in characters (for image logos)
    "padding": {
        "top": 0,          // Top padding
        "left": 0,         // Left padding
        "right": 2         // Right padding
    },
    "color": {             // Override logo colors
        "1": "",
        "2": ""
    }
	},
  "modules": [
    "title",
    "separator",
    "os",
    "host",
    "kernel",
    "uptime",
    "packages",
    "shell",
    "display",
    "de",
    "wm",
    "wmtheme",
    "theme",
    "icons",
    "font",
    "cursor",
    "terminal",
    "terminalfont",
    "cpu",
    "gpu",
    "memory",
    "swap",
    "disk",
    "localip",
    "battery",
    "poweradapter",
    "locale",
    "break",
    "colors"
  ]
}
```



## 常用工具

```
apt update && apt upgrade
apt install curl wget vim zip unzip aria2 htop neofetch iperf3 cmake tree net-tools  traceroute python3-pip python3-venv git dnsutils arping telnet nfs-common nmap aptitude -y

//casaos
curl -fsSL https://get.casaos.io | sudo bash

//1Panel
curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh

apt install lm-sensors 
sudo sensors-detect
sensors

which du
find ./ -type d -name 'fuck you'

du -sh * | sort -h
tree -L 1 --du -h

systemctl status docker.service | sshd
journalctl -xeu docker.service

查看oec gpu npu负载
cat /sys/kernel/debug/rkrga/load 

cp：需要 -r 或 -a 选项来递归复制文件夹

.tar -> tar -xvf
.tar.gz -> tar -xzvf
.tar.bz2 -> tar -xjvf
.tar.xz -> tar -xJvf

使用 tar 的 --no-same-owner 选项
如果你只是需要解压文件，而不关心文件的所有者，可以在 tar 命令中使用 --no-same-owner 选项：
tar --no-same-owner -xvf buildroot_dl_4c7c9df616fb.tar.gz

:打包压缩文件夹
tar -czvf my_archive.tar.gz my_folder/

lsof -i :11434

watch -n 1 "top"
watch -n 0.01 sudo cat /sys/kernel/debug/rknpu/load

//set timezone
sudo timedatectl set-timezone Asia/Shanghai

export PATH=$PATH:/new/path

./modelscope download --model deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --local_dir DeepSeek-R1-Distill-Qwen-1.5B

./build/bin/llama-cli -m DeepSeek-R1-Distill-Qwen-1.5B-F16.gguf -cnv
./build/bin/llama-server -m DeepSeek-R1-Distill-Qwen-1.5B-F16.gguf --port 8088
DeepSeek-R1-Distill-Qwen-1.5B
./build/bin/llama-cli -m DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf
#Q4_K_M 量化
./build/bin/llama-quantize DeepSeek-R1-Distill-Qwen-1.5B-F16.gguf DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf Q4_K_M
```

## vim 高级模式

```vim
a-向后 i-插入 o-换行
yy - p
20yy - p
dd
10dd
:%s/port/ports/g  替换 
u - ctl+r


---
when you open multiple files:

vim app.py dht11.py pump.py  
:sp 水平
:vsp vertical

:ls or :buffers  #list all file(buffers)

:bn 或 :bnext：切换到下一个缓冲区。
:bp 或 :bprev：切换到上一个缓冲区。

:b[number] #switch files
:b file[Tab]

快捷键：Ctrl + w 然后按方向键（h、j、k、l）。
窗口编号：Ctrl + w <number>。
命令行：:wincmd w 或 :<number>wincmd w。

--------
vim ~/.vimrc
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=utf-8,gbk,latin1

```

## Git usage

```
mkdir xx
git init 
git add . 					#暂存所有变化
git commit -m "V1"
git branch -M main

git remote add origin git@github.com:FR13NDS-wolf/ssh-test.git #关联
git remote -v 					#check
git push -u origin main  		#推送
```





## Btc

```
./minerd -a sha256d -D -o stratum+tcp://btc.f2pool.com:1314l -u lophy.001 -p x -t 1 -

./minerd -a sha256d -D -o stratum+tcp://public-pool.io:21496 -u bc1q4lky6579c83f4y2he0pmhak6a33vpdrh9qx5vmrway8jtypg9qxqjhnrm0 -p x -t 1
bc1q4lky6579c83f4y2he0pmhak6a33vpdrh9qx5vmrway8jtypg9qxqjhnrm0
```



## python环境

```
apt install python3.12-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

pip3 install resend --break-system-packages
```

## 数据库

### redis

```
redis-cli -h 10.2.3.9 -p 6379
>auth password

```

mysql类

```
mysql -h 10.31.0.9 -P 3306 -u root -p
docker exec -it a1a24ec14603 mysql -u casaos -p
mysql -h 10.31.0.9 -P 3306 -u root -p farm < ./upload/qqfarm.sql //自己机器路径
```



## vscode

### **快速搜索**

- **快捷键**：`Cmd + P`
- **命令面板**： `Ctrl + Shift + P`或 `Cmd + Shift + P`

### 基础操作

- **新建文件**：`Ctrl + N`（Windows/Linux）或 `Cmd + N`（macOS）。
- **保存文件**：`Ctrl + S`（Windows/Linux）或 `Cmd + S`（macOS）。
- **关闭文件**：`Ctrl + W`（Windows/Linux）或 `Cmd + W`（macOS）。
- **关闭所有文件**：`Ctrl + K, Ctrl + W`（Windows/Linux）或 `Cmd + K, Cmd + W`（macOS）。

### 编辑操作

- **复制行**：`Ctrl + C`（Windows/Linux）或 `Cmd + C`（macOS）。
- **移动行**：`Alt + ↑/↓`（Windows/Linux）或 `Alt + ↑/↓`（macOS）。
- **删除行**：`Ctrl + Shift + K`（Windows/Linux）或 `Cmd + Shift + K`（macOS）。
- **格式化代码**：`Shift + Alt + F`。

### 搜索与导航

- **全局搜索**：`Ctrl + Shift + F`（Windows/Linux）或 `Cmd + Shift + F`（macOS）。
- **跳转到定义**：`F12`。
- **查找引用**：`Shift + F12`。
- **显示符号大纲**：`Ctrl + Shift + O`（Windows/Linux）或 `Cmd + Shift + O`（macOS）。

### 窗口与布局

- **切换全屏**：`F11`。
- **切换侧边栏**：`Ctrl + B`（Windows/Linux）或 `Cmd + B`（macOS）。
- **切换编辑器布局**：`Alt + Shift + 数字`（Windows/Linux）或 `Cmd + Option + 数字`（macOS）。

### 其他

- **显示命令面板**：`Ctrl + Shift + P`（Windows/Linux）或 `Cmd + Shift + P`（macOS）。
- **显示终端**：`Ctrl + ``（Windows/Linux）或 `Cmd + ``（macOS）。
- **安装扩展**：`Ctrl + Shift + X`（Windows/Linux）或 `Cmd + Shift + X`（macOS）

## 分区/挂载

### SWAP

在 Linux 系统中，您可以通过以下方法重新分配或扩展交换分区（swap）：

### **使用 `zram`**

根据您提供的 `lsblk` 输出，您已经在使用 `zram`。`zram` 可以为交换提供压缩的内存，节省物理内存。您可以调整 `zram` 的大小或数量。

调整 `zram` 大小：

1. **禁用当前的 `zram` 设备**：

   ```
   sudo swapoff /dev/zram0
   ```

2. **调整大小**（例如，将大小更改为 2G）：

   ```
   sudo modprobe zram num_devices=1
   echo 2G | sudo tee /sys/block/zram0/disksize
   sudo mkswap /dev/zram0
   sudo swapon /dev/zram0
   ```

3. **格式化**

``` 
sudo mkfs.ext4 /dev/sdb
```



### 挂载

1. 确定位置 `lsblk | fdisk -l `

2. 选择挂载点 `mkdir /sata`

3. 设置自动挂载 编辑 **/etc/fstab**

```shell
UUID=2439fb51-0518-4360-8839-fbc31c1cecb0    /        btrfs    defaults,noatime,compress=zstd:6      0 1
LABEL=BOOT_EMMC        /boot    vfat                   defaults                   0 2
tmpfs                  /tmp     tmpfs                  defaults,nosuid            0 0
```

在末位添加: 

```
/dev/sdb1  /sata  ext4  defaults  0  2

ext4 是文件系统类型（根据实际情况更改，例如 ntfs、xfs 等）。
defaults 是挂载选项，您可以根据需要修改。
0 是用于备份的选项，通常设置为 0。
2 是用于文件系统检查的顺序，根文件系统通常为 1，其他为 2。

前面也可以用 blkid 显示出 UUID 填入

sudo systemctl daemon-reload 如果你修改了 /etc/fstab，确保重新加载 systemd
```

4. 测试挂载 **mount -a**
5. 验证 **df -h**

```
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           194M   11M  184M   6% /run
/dev/mmcblk2p2   14G  1.8G   13G  13% /
tmpfs           968M     0  968M   0% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           968M  4.0K  968M   1% /tmp
/dev/mmcblk2p1  510M  153M  358M  30% /boot
/dev/zram1       47M  2.7M   41M   7% /var/log
tmpfs           194M     0  194M   0% /run/user/0
/dev/sda2        32M   28M  4.6M  86% /media/devmon/VTOYEFI
/dev/sda1        59G   47G   12G  81% /media/devmon/Ventoy
```

### 命令工具

```
lsblk
blkid
```

### 手动挂载

```
sudo mount /dev/sdb1 /mnt/usb 
添加到自启中延长多少秒
```



## 磁盘测速

``` 
sudo apt install hdparm  # Debian/Ubuntu
lsblk OR df -h
hdparm -Tt /dev/sda
```

## 环境变量

```
export PATH=$PATH:/usr/local/bin
export PATH=$PATH:/usr/bin
source .bashrc 

alias
```

## System

```
uname -a
neofetch
cat /etc/os-release
lsb_release -a
```

## Cpu

```
lscpu
cat /proc/cpuinfo
htop
```

## Process

```
ps -ef 
ps aux | grep xxx
top
htop
```

## Network

```
ping
ping6

apt install dnsutils
nslookup github.com

lsof -i :80
netstat -tulnp | grep :80 

traceroute
tracetoute6

ifconfig eth0

ip a

iperf3 -s -D (slient start)
iperf3 -c ip [-R]

curl:
curl -X POST "https://webhook-tg.loophy.top/botx00qv4xxxBu-oC9Es_pnQ/sendMessage" \
     -H "Content-Type: application/json" \
     -d '{"chat_id": "-4517115329", "text": "Success!"}'  
wget
aria2c
    
#!/bin/sh
### BEGIN INIT INFO
# Provides:NetworkRestart
# Required-Start: $network $remote_fs $local_fs
# Required-Stop: $network $remote_fs $local_fs
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: NetworkRestart
# Description: NetworkRestart
### END INIT INFO
sleep 3
sudo systemctl restart NetworkManager
 
exit 0


    

```

### 虚拟机固定ip

**修改Netplan配置文件**

1. **打开配置文件**
   打开终端，编辑Netplan配置文件。配置文件可能位于 `/etc/netplan/` 目录下，文件名可能是 `01-netcfg.yaml` 或类似。运行以下命令：

   bash复制

   ```bash
   sudo nano /etc/netplan/01-netcfg.yaml
   ```

2. **修改配置内容**
   将文件内容修改为以下格式，以设置静态IP地址：

   yaml复制

   ```yaml
   network:
     version: 2
     renderer: NetworkManager
     ethernets:
       ens33:
         dhcp4: no  # 禁用DHCP
         addresses:
           - 192.168.2.100/24  # 设置静态IP地址和子网掩码
         gateway4: 192.168.2.1  # 设置网关
         nameservers:
           addresses:
             - 8.8.8.8  # 设置DNS服务器
             - 8.8.4.4
   ```

3. **`sudo netplan apply`**

### wifi 连接

``` 
nmcli device wifi list 
nmcli device wifi connect <SSID> password <PASSWORD>
nmcli device wifi connect 50:4F:3B:C9:52:06 password 00000000
```

### ssh配置

```
sudo apt update
sudo apt install openssh-server

sudo systemctl status sshd

vim /etc/ssh/sshd_config
PermitRootLogin yes

使用 aptitude 解决依赖问题
如果上述步骤仍然无法解决问题，可以尝试使用 aptitude，它是一个更强大的包管理工具，能够更好地处理依赖关系：
安装 aptitude：
sudo apt-get install aptitude
sudo aptitude install openssh-server
---
Client

ssh-keygen -t rsa -b 4096 -f ~/.ssh/my_private_key
.ssh/config
/etc/ssh/sshd_config -> publickeyAuth

 vim .ssh/authorized_keys 

chmod 700 /root
chmod 700 /root/.ssh
chmod 600 /root/.ssh/authorized_keys

Host myserver1
    HostName 192.168.1.100
    User myuser1

Host myserver2
    HostName 192.168.1.101
    User myuser2
    IdentityFile ~/.ssh/my_private_key
```

### bluetooth

```
systemctl status bluetooth

hciconfig
sudo hciconfig hci0 up

hcitool scan
---
bluetoothctl
scan on
```

### NFS 共享

```
sudo apt install nfs-common 
sudo vim /etc/exports
cat /etc/exports 
/Users/loophy/nfs_share -alldirs -mapall=loophy:staff 10.31.0.217

mkdir /nfs
mount -t nfs -o nolock 10.31.0.5:/Users/loophy/nfs_share /nfs
df -h

#自动挂载
/etc/fstab
10.31.0.5:/Users/loophy/nfs_share /nfs nfs defaults 0 0
```

### caddy 使用

```
https://caddyserver.com/docs/install

sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy

caddy add-package github.com/caddy-dns/cloudflare

hkv.loophy.top {
        # Set this path to your site's directory.
        root * /var/www/html

         tls /root/cert-8.23/cert2.pem /root/cert-8.23/privkey2.pem
        # Enable the static file server.
        file_server

        # Another common task is to set up a reverse proxy:
        # reverse_proxy localhost:8080

        # Or serve a PHP site through php-fpm:
        # php_fastcgi localhost:9000
}

:80 {
	# Set this path to your site's directory.
	#root * /usr/share/caddy
	root * /var/www/html

	# Enable the static file server.
	file_server

	# Another common task is to set up a reverse proxy:
	# reverse_proxy localhost:8080

	# Or serve a PHP site through php-fpm:
	# php_fastcgi localhost:9000
}

oec.loophy.top:5245 {
    
    tls {
     dns cloudflare x

    }

    reverse_proxy http://127.0.0.0:5244

}

oec.loophy.top:1112 {
    
    tls {
     dns cloudflare x

    }

    reverse_proxy http://127.0.0.0:1111

}

oec.loophy.top:2284 {

    tls {
     dns cloudflare x

    }

    reverse_proxy http://127.0.0.0:2283

}

oec.loophy.top:3015 {

    tls {
     dns cloudflare x

    }

    reverse_proxy http://127.0.0.0:3005

}

oec.loophy.top:3010 {

    tls {
     dns cloudflare x

    }

    reverse_proxy http://127.0.0.0:3000

}
```

```shell
apt update && apt upgrade
apt install curl wget vim zip unzip aria2 htop neofetch iperf3 cmake tree net-tools  traceroute python3-pip python3-venv git dnsutils arping telnet nfs-common nmap aptitude -y

curl -fsSL https://get.casaos.io | sudo bash

curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh


sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
```

### docker

```
DDNS-GO:

oec.loophy.top
alist.loophy.top
status.loophy.top
nezha.loophy.top
immich.loophy.top

https://webhook-tg.loophy.top/bxxge
{
    "chat_id": "-4517115329",
    "text": "主人！您的 IP 有变化\n\nIPv6: #{ipv6Result}\nIP: #{ipv6Addr}\nDomain: oec.loophy.top"

}

casaos:
1panel:
Chrome:
sudo docker run --rm -it --shm-size=512m -p 6902:6901 -e VNC_PW=pyh kasmweb/chrome:1.17.0

Syncthing: https://hub.docker.com/r/linuxserver/syncthing
---
version: '3.8'
services:
  syncthing:
    image: lscr.io/linuxserver/syncthing:latest
    container_name: syncthing
    hostname: syncthing
    environment:
      - PUID=${PUID:-1000}
      - PGID=${PGID:-1000}
      - TZ=${TZ:-Asia/Shanghai}  # 修改为你的时区
    volumes:
      - ./config:/config  # 相对路径，便于管理
      - ./data:/data      # 统一数据目录
    ports:
      - 8384:8384        # Web UI
      - 22000:22000/tcp  # 同步协议 (TCP)
      - 22000:22000/udp  # 同步协议 (UDP)
      - 21027:21027/udp  # 发现协议
    restart: unless-stopped
    networks:
      - syncthing-net
    security_opt:
      - no-new-privileges:true
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8384"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

networks:
  syncthing-net:
    driver: bridge  
PUID=1000
PGID=1000
TZ=Asia/Shanghai

kali Linux:
---
services:
  kali-linux:
    image: lscr.io/linuxserver/kali-linux:latest
    container_name: kali-linux
    security_opt:
      - seccomp:unconfined #optional
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Shanghai
      - SUBFOLDER=/ #optional
      - "TITLE=Kali Linux" #optional
    volumes:
      - ./config:/config
      - /var/run/docker.sock:/var/run/docker.sock #optional
    ports:
      - 3030:3000
      - 3031:3001
    shm_size: "1gb" #optional
    restart: unless-stopped




命令:
docker ps
docker rm -f 
docker rmi
docker run -it --rm alpine (用于调试)
> --restart
> --unless-stopped
docker run -d -p 80:80 -e xxx=xxx -e yy=yy nginx
docker create/stop/start/logs -f/inspect 

docker exec id (ps aux)
docker exec id -it bash

docker run -d --network host nginx

Dockerfile

docker compose up/stop/start/down (自动创建network

docker compose -f file.yml up -d


docker network create -d ipvlan \
    --subnet=192.168.1.0/24 \
    --ip-range=192.168.1.128/25 \
    --gateway=192.168.1.1 \
    --opt parent=eth0 \
    macvlan1

docker network rm macvlan
docker network create -d macvlan \
  	--subnet=10.31.0.0/24 \
    --ip-range=10.31.0.128/25 \
    --gateway=10.31.0.1 \
    --opt parent=eth0.10 \
    macvlan1
    
docker network create -d ipvlan \
    --subnet=10.31.0.0/24 \
    --ip-range=10.31.0.128/25 \
    --gateway=10.31.0.1 \
    --opt parent=en0 \
    macvlan2

docker run -d \
    --name nginx \
    --network macvlan1 \
    --ip 192.168.1.200 \
    -p 80:80 \
    -v /root/nginx/conf.d:/etc/nginx/conf.d \
    -v /var/www/html:/usr/share/nginx/html \
    nginx
    
docker run -d \
    --name nginx \
    --network macvlan1 \
    --ip 192.168.1.200 \
    -v /root/nginx/conf.d:/etc/nginx/conf.d \
    -v /var/www/html:/usr/share/nginx/html \
    nginx
```



### zerotier

```
curl -s https://install.zerotier.com | sudo bash

zerotier-cli status 
zerotier-cli join 272f5eae16c127d4

```

### 建站

```
https://hkargo.loophy.top/5cbxxx29b/auto
bash <(wget -qO- https://raw.githubusercontent.com/fscarmen/sing-box/main/sing-box.sh)
```

### Nezha

**Docker**

1.Nezha

image:ghcr.io/nezhahq/nezha:v1.12.0

Stg:/dashboard/data

2.nzAgent:grpc

image:nginx

File: /etc/nginx/conf.d/default.conf

```
upstream dashboard {
    server nezha.ns-imc7mqm6.svc.cluster.local:8008;
    keepalive 512;
}

server {
    listen 80 http2;
    server_name nezha.ns-imc7mqm6.svc.cluster.local;

    underscores_in_headers on;

    location ^~ /proto.NezhaService/ {
        grpc_set_header Host $host;
        grpc_set_header nz-realip $remote_addr;
        grpc_read_timeout 600s;
        grpc_send_timeout 600s;
        grpc_socket_keepalive on;
        client_max_body_size 10m;
        grpc_buffer_size 4m;
        grpc_pass grpc://dashboard;
    }
}
```

填入agent:80

```

<!-- 哪吒探针前台美化 版本 2025.04.11 by TomyJan -->
<!-- 详细说明与支持请前往: https://www.nodeseek.com/post-311746-1 -->
<script>
    
    /* 这部分这几个挂在 window 下的变量是哪吒内置的, 详见 https://nezha.wiki/guide/settings.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E4%BB%A3%E7%A0%81 */
    window.CustomBackgroundImage = 'https://api.tomys.top/api/acgimg'; /* PC 端背景图, 这是我自己的随机图 API, 自定义背景图建议配合下方的压暗和模糊食用 */
    window.CustomMobileBackgroundImage = 'https://api.tomys.top/api/acgimg'; /* 移动端背景图, 这是我自己的随机图 API, 自定义背景图建议配合下方的压暗和模糊食用 */
    window.CustomLogo = 'https://webp-usor.loophy.top/2025/05/avat1.png'; /* 页面左上角和标题栏展示的 Logo, 换成你自己的 */
    window.CustomDesc = 'Less is more'; /* 页面左上角副标题 */
    window.ShowNetTransfer = true; /* 服务器卡片是否显示上下行流量, 默认不显示 */
    /* window.DisableAnimatedMan = true; /* 为 true 则基佬死开, 和下方 CustomIllustration 冲突 */
    window.CustomIllustration = 'https://s2.loli.net/2024/12/24/fj3EXY7umsyR9NW.webp'; /* 把基佬图换成你想换的图, 此处图抄袭自 https://misaka.se/ */
    window.FixedTopServerName = true; /* 是否固定顶部显示服务器名称, 默认不固定 */
    window.CustomLinks = '[{\"link\":\"https://loophy.top/\",\"name\":\"首页\"},{\"link\":\"https://vov.moe/\",\"name\":\"博客\"}]'; /* 自定义导航栏链接 */
    /* window.ForceTheme = 'dark'; /* 强制主题色, 可选值为 light 或 dark */
    /* window.ForceUseSvgFlag = false; /* 是否强制使用 svg 旗帜 */

    /* 自定义字体, 注意需要同步修改下方 CSS 中的 font-family */
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://font.sec.miui.com/font/css?family=MiSans:400,700:MiSans'; // MiSans
    // link.href = 'https://npm.elemecdn.com/lxgw-wenkai-screen-webfont@1.7.0/style.css'; // 霞鹜文楷, font-family: 'LXGW WenKai Screen'
    document.head.appendChild(link);

    /* 修改页脚, 可使用 HTML 元素, 请保留哪吒版权信息, 与下方 CSS 中的 不显示页脚 冲突 */
    /* 左侧哪吒文本 */
    const observerFooterLeft = new MutationObserver(() => {
        const footerLeft = document.querySelector('.server-footer-name > div:first-child');
        if (footerLeft) {
            // footerLeft.innerHTML = 'Powered by <a href="https://github.com/nezhahq/nezha" target="_blank">NeZha</a>';
            footerLeft.style.visibility = 'hidden'; // 隐藏
            observerFooterLeft.disconnect();
        }
    });
    observerFooterLeft.observe(document.body, { childList: true, subtree: true });
    /* 右侧主题文本 */
    const observerFooterRight = new MutationObserver(() => {
        const footerRight = document.querySelector('.server-footer-theme');
        if (footerRight) {
            footerRight.innerHTML = '<section>Powered by <a href="https://github.com/nezhahq/nezha" target="_blank">NeZha</a></section>';
            // footerRight.style.visibility = 'hidden'; // 隐藏
            observerFooterRight.disconnect();
        }
    });
    observerFooterRight.observe(document.body, { childList: true, subtree: true });
</script>
<style>
    /* 自定义字体, 注意需要在上方 JS 中引入相应字体 */
    * {
        font-family: 'MiSans';
    }
    h1, h2, h3, h4, h5 {
        font-family: 'MiSans', sans-serif;
    }

    /* 背景压暗和模糊, 开了背景图建议开启 */
    .dark .bg-cover::after {
        content: '';
        position: absolute;
        inset: 0;
        backdrop-filter: blur(6px);
        background-color: rgba(0, 0, 0, 0.6);
    }
    .light .bg-cover::after {
        content: '';
        position: absolute;
        inset: 0;
        backdrop-filter: blur(6px);
        background-color: rgba(255, 255, 255, 0.3);
    }

    /* 不显示右上角语言切换按钮 */
    /* [id="radix-:r0:"] {
        display: none;
    } */

    /* 不显示右上角主题切换按钮 */
    /* [id="radix-:r2:"] {
        display: none;
    } */

    /* 不显示页脚, 请保留哪吒版权信息, 与上方 JS 中的 修改页脚文本 冲突 */
    /* footer {
        display: none;
    } */
</style>
```





## Tspi

### Image Extrace

```
通过网络将自己的所有文件导出

Kfb_tspi
sudo apt-get update
sudo apt-get install rsync

Ubuntu
sudo apt-get update
sudo apt-get install rsync
sudo apt-get install openssh-client
sudo apt-get install openssh-server

mkdir rootfs_copy
sudo rsync -avx root@10.31.0.219:/ rootfs_copy #wait maybe some hours
dd if=/dev/zero of=rootfs.img  bs=1M count=8000 
sudo mkfs.ext4 -F -L linuxroot rootfs.img 
mkdir rootfs-mount
sudo mount rootfs.img rootfs-mount 
sudo cp -rfp rootfs_copy/* rootfs-mount
sudo umount rootfs-mount
sudo e2fsck -p -f rootfs.img

再利用工具解包即可

```

### Compile C/C++

```c
sudo apt install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
aarch64-linux-gnu-gcc --version

vim hello.c
    
#include<studio.h>
int main() {
    printf("hello, world");
	return 0;
}
sudo aarch64-linux-gnu-gcc hello.c -o hello
    
   
```



### buildroot

```shell
echo "none" > /sys/class/leds/rgb-led-r/trigger
echo "none" > /sys/class/leds/rgb-led-g/trigger
echo "none" > /sys/class/leds/rgb-led-b/trigger

echo "timer" > /sys/class/leds/rgb-led-b/trigger
echo "timer" > /sys/class/leds/rgb-led-g/trigger
echo "timer" > /sys/class/leds/rgb-led-r/trigger


wifi_start.sh IWrt-2.4G 00000000
```

### GPIO

```bash
GPIO命名规则与引脚ID计算
GPIO0_B7
控制器 bank: rk3566有5个GPIO控制器分别是GPIO0-GPIO4，一个控制器下面包含ABCD个端口，每个端口下有包含0-7个索引序号，所以一个控制器可控制32个IO引脚。
端口 port: A、B、C、D。对应着数字：0-3所以 A=0、B=1、C=2、D=3  
索引序号 pin: 固定为0-7共计8个数 代入 GPIO0_B7 ，该引脚的 ID 可以按照以下规则组成：
控制器 (bank) 为 0，表示第 0 组控制器。
端口（port）为 B，表示端口号为1。
索引序号（pin）为7  根据计算公式：32 x 0 + 1 x 8 + 7 = 15，可以得到引脚ID为15。

echo 104 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio104/direction
echo 1 > /sys/class/gpio/gpio104/value
echo 106> /sys/class/gpio/unexport


// humidify 使用继电器控制
echo 104 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio104/direction
echo 1 > /sys/class/gpio/gpio104/value
echo 0 > /sys/class/gpio/gpio104/value

// motor PWM14 使用l298n控制( 参数就这样固定
echo 100 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio100/direction
echo 101 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio101/direction
echo 0 > /sys/class/gpio/gpio100/value
echo 1 > /sys/class/gpio/gpio101/value 

echo 0 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip2/export
echo 20000000 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip2/pwm0/period
sleep 0.1
echo 5000000 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip2/pwm0/duty_cycle
sleep 0.1
echo 'normal' > /sys/devices/platform/fe700020.pwm/pwm/pwmchip2/pwm0/polarity
echo 1 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip2/pwm0/enable
// close
echo 0 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip2/pwm0/enable

echo 0 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip2/unexport


#!/bin/bash
# 定义 GPIO 引脚编号
GPIO_PIN=15
# 导出 GPIO 引脚
echo "$GPIO_PIN" > /sys/class/gpio/export
# 设置 GPIO 方向为输出
echo "out" > /sys/class/gpio/gpio${GPIO_PIN}/direction
# 设置 GPIO 值为 1
echo "1" > /sys/class/gpio/gpio${GPIO_PIN}/value
```



找到我们要测试的PWM设备

```shell
rk3566_tspi:/ # find . -name "pwm"
#pwm4: pwm@fe6e0000 edp屏幕背光
./sys/devices/platform/fe6e0000.pwm/pwm
#pwm14: pwm@fe700020
./sys/devices/platform/fe700020.pwm/pwm
#pwm9: pwm@fe6f0010
./sys/devices/platform/fe6f0010.pwm/pwm
#pwm8: pwm@fe6f0000
./sys/devices/platform/fe6f0000.pwm/pwm
```

这里就以pwm8进行测试：

```shell
#列出pwm8目录如下
rk3566_tspi:/ # ls /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/
device  export  npwm  power  subsystem  uevent  unexport
```

使能调试通

```shell
#通道是从0开始的，对应原理图上的pwmx_mx中的mx，我们这里是pwm8_m0所以就是通道0
rk3566_tspi:/ # echo 0 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/export

#使能后会发现下面比之前多了一个pwm0目录
rk3566_tspi:/ # ls /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/
device  export  npwm  power  pwm0  subsystem  uevent  unexport
```

设置pwm周期、频率、极性

```shell
#单位纳秒，所以1000000000个纳秒就是一秒
20 us
rk3566_tspi:/ # echo 20000000 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/pwm0/period

#设置占空比为50%
12 us
rk3566_tspi:/ # echo 10000000 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/pwm0/duty_cycle

#设置极性可以有两个选项：normal和inverted。当设置为 “normal” 时，
#高电平（高电压）表示占空比的高部分，而低电平（低电压）表示占空比的低部分。
#当设置为 “inverted” 时，这种情况相反
rk3566_tspi:/ # echo 'normal' > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/pwm0/polarity 
```

启动与停止PWM

```shell
#启动PWM
rk3566_tspi:/ # echo 1 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/pwm0/enable
#停止PWM
rk3566_tspi:/ # echo 0 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/pwm0/enable
```

失能调试通道

```shell
rk3566_tspi:/ # echo 0 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/unexport
```

```shell
echo 0 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip1/export
echo 0 > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/export 
echo 0 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip3/export

echo 1000000000> /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip1/pwm0/period
echo 20000000 > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/pwm0/period
echo 1000000000 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip3/pwm0/period

echo 500000000 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip1/pwm0/duty_cycle
echo 8000000 > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/pwm0/duty_cycle
echo 100000000 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip3/pwm0/duty_cycle

echo 'normal' > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip1/pwm0/polarity
echo 'normal' > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/pwm0/polarity
echo 'normal' > /sys/devices/platform/fe700020.pwm/pwm/pwmchip3/pwm0/polarity

echo 1 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip1/pwm0/enable
echo 1 > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/pwm0/enable
echo 1 > /sys/devices/platform/fe700020.pwm/pwm/pwmchip3/pwm0/enable
```



**最终调试 接口**

```shell
gpio 100&101 104&114

echo 100 > /sys/class/gpio/export
echo 101 > /sys/class/gpio/export
echo 104 > /sys/class/gpio/export
echo 114 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio100/direction
echo out > /sys/class/gpio/gpio101/direction
echo out > /sys/class/gpio/gpio104/direction
echo out > /sys/class/gpio/gpio114/direction
echo 0 > /sys/class/gpio/gpio100/value
echo 1 > /sys/class/gpio/gpio101/value
echo 1 > /sys/class/gpio/gpio104/value
echo 0 > /sys/class/gpio/gpio114/value

echo 15> /sys/class/gpio/unexport

pwm 
echo 0 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/export
echo 0 > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/export
echo 20000000 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/pwm0/period
echo 20000000 > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/pwm0/period
sleep 0.1
echo 2500000 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/pwm0/duty_cycle
echo 2500000 > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/pwm0/duty_cycle
sleep 0.1
echo 'normal' > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/pwm0/polarity
echo 'normal' > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/pwm0/polarity

echo 1 > /sys/devices/platform/fe6f0000.pwm/pwm/pwmchip0/pwm0/enable
echo 1 > /sys/devices/platform/fe6f0010.pwm/pwm/pwmchip1/pwm0/enable
```

