# 山东联通 IPTV 直播源

此仓库包含 **山东联通 IPTV** 的播放列表及相关配置，方便快速导入播放器使用。

## 使用说明

1. 推荐使用单播，起播/切台速度快
2. 不开通 IPTV 服务不影响收看单播

unicast 目录下的是单播 M3U：

直接导入到 APTV 使用： https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-aptv.m3u

直接导入到 KU9 使用：  https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-ku9.m3u


multicast 目录下的是组播 M3U，各地区的组播地址，第三个字节有不同，因此分了多个文件，例如： 

济南： https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-jinan.m3u

青岛： https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-qingdao.m3u


merge/local 目录下存放的是地方频道，会合并到最终的组播列表里面，**欢迎提交 PR 添加**

## 具体配置

### 单播与回看

山东联通的 RTSP 单播仅支持 RTP OVER UDP 的传输方式，在 NAT 下的设备是没法收到 RTP 数据的。要正常收看单播需要做以下设置（任选其一）：
- 有公网 IPV4 地址的情况下，走 PPPoE（山东联通默认是给公网的，没有的话在宽带账号后面加上 `@e` 再拨号）
- 没有公网 IP, 需要 NAT 穿透，可以安装 [rtsproxy](https://github.com/plsy1/rtsproxy)，推荐直接部署到路由器上
- 走 IPTV 接口（仅支持当地单播源，比如济南地区的单播源，在青岛就没办法通过 IPTV 接口访问）

### 组播

- 推荐使用 [rtp2httpd](https://github.com/stackia/rtp2httpd) 代理组播数据，支持 FCC 快速频道切换，起播/换台的体验接近单播
- 播放设备直收组播

## 相关仓库

- **EPG 电子节目单**  
  - 项目地址：[epg](https://github.com/plsy1/epg)  
  - 从山东联通处获取的 EPG 节目单，每日自动更新，包含9天的数据（七天回看 + 当天数据 + 次日数据）
- **IPTV 鉴权模拟**  
  - 项目地址：[shandong-unicom-iptv](https://github.com/plsy1/shandong-unicom-iptv)  
  - 提供 IPTV 机顶盒的 **登录鉴权模拟**，完成鉴权后可获取 `token`，并用其抓取节目单和播放地址
- **iptvTool**
  - 项目地址：[iptvTool](https://github.com/plsy1/iptvTool)  
  - 用于抓取并处理 IPTV 原始数据、生成 M3U 播放列表的命令行工具，本仓库即是通过此工具获取的数据
- **rtsproxy**
  - 项目地址：[rtsproxy](https://github.com/plsy1/rtsproxy)  
  - RTSP 代理工具，解决 RTP OVER UDP 在 NAT 环境下无法收到数据的问题，也可用于对齐直播与回放路径
 
## 频道变动

