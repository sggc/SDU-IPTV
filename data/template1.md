# 山东联通 IPTV 直播源

此仓库包含 **山东联通 IPTV** 的播放列表及相关配置，方便快速导入播放器使用。

## 使用说明

1. 推荐使用单播，起播/切台速度快

2. 不开通 IPTV 服务不影响收看单播

3. unicast 目录下的是单播 M3U：
   - 直接导入到 APTV 使用： 

      ​	Github: https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-aptv.m3u
      
      ​	jsDelivr(国内直连): https://fastly.jsdelivr.net/gh/plsy1/iptv@master/unicast/unicast-aptv.m3u

   - 直接导入到 KU9 使用：  

      ​	Github: https://raw.githubusercontent.com/plsy1/iptv/main/unicast/unicast-ku9.m3u
      
      ​	jsDelivr(国内直连): https://fastly.jsdelivr.net/gh/plsy1/iptv@master/unicast/unicast-ku9.m3u

4. multicast 目录下的是组播 M3U，各地区的组播地址，第三个字节有不同，因此分了多个文件，例如： 

   济南： https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-jinan.m3u

   青岛： https://raw.githubusercontent.com/plsy1/iptv/main/multicast/multicast-qingdao.m3u

5. merge/local 目录下存放的是地方频道，会合并到最终的组播列表里面，**欢迎提交 PR 添加**

6. 山东地方频道，直接导入 KU9 播放（另有通用部署方式，详细可查看对应仓库内的说明）：https://fastly.jsdelivr.net/gh/plsy1/iqilu@master/iqilu-ku9.m3u

7. 在闲鱼上倒卖的[二道贩子们](https://github.com/plsy1/iptv/issues/15)，好自为之

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

- IPTV 机顶盒登录鉴权模拟： https://github.com/plsy1/shandong-unicom-iptv
- EPG 节目单： https://github.com/plsy1/epg
- RTSP 代理工具： https://github.com/plsy1/rtsproxy
- IPTV 数据抓取与生成 M3U 工具： https://github.com/plsy1/iptvTool
- 山东各区县频道（爱齐鲁网络源）： https://github.com/plsy1/iqilu

## 频道变动

