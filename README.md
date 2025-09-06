# 山东联通 IPTV

本仓库收录了 **山东联通 IPTV** 的播放列表及相关配置，方便快速导入播放器使用。  

## 🚀 使用方法

1. 下载或复制对应的播放列表文件：  
   - `multicast.m3u` → 组播播放列表
   - `unicast.m3u` → 单播播放列表
   - `iptv.json` → 整理好的 IPTV 播放源数据，包含频道信息与播放地址的元数据  

2. 将播放列表导入常见播放器，例如：  
   - [VLC](https://www.videolan.org/vlc/)  
   - [PotPlayer](https://potplayer.daum.net/)  
   - [Kodi](https://kodi.tv/)  
   - 各类 IPTV 播放器 (iOS / Android 端)  

3. 若部分频道无法播放，可结合 **鉴权模拟项目** 抓取最新的节目单与播放地址。 

### 导入播放列表示例

![导入播放列表示例](images/import_example.png)

## ⚠️ 注意事项

- 单播播放（`unicast.m3u`）以及回看功能需要 **公网 IP** 环境。  
- 组播播放（`multicast.m3u`）需在支持组播的局域网环境下配合 **udpxy** 使用。  

## 📌 其他

- **EPG 节目单**  
  - 项目地址：[plsy1/epg](https://github.com/plsy1/epg)  
  - 提供电子节目单 (EPG)，可与播放源结合，实现节目预告与回看功能。  

- **IPTV 鉴权模拟**  
  - 项目地址：[plsy1/shandong-unicom-iptv](https://github.com/plsy1/shandong-unicom-iptv)  
  - 提供 IPTV 机顶盒的 **登录鉴权模拟**，完成鉴权后可获取 `token`，并用其抓取节目单和播放地址。  

## 📢 声明

- 本项目仅供学习与研究使用。  
- 请勿将本仓库内容用于商业用途。  
