# 安装 USB Loader 使用的 cIOS


## 一、相关链接

> [点击下载](./cios-for-usb-loader.zip) 傻瓜包

傻瓜包里的文件出处：
- **Some YAWMM Mod**：<https://github.com/FIX94/Some-YAWMM-Mod>
- 各个 cIOS 对应的 .wad 文件：<https://github.com/modmii/modmii.github.io>


## 二、概述

Wii 主机会使用不同的 IOS 来加载光驱里的 Wii 游戏光盘。Wii 使用的 IOS，任天堂在主机出厂或者系统升级的时候会帮我们安装好。

相应的，USB Loader 也需要使用不同的 cIOS 来加载 SD 卡或者 USB 设备上的 Wii 游戏（.wbfs）文件。USB Loader 使用的 cIOS，需要我们自己动手安装。

USB Loader 使用的 cIOS 主要有 6 个：

![USB Loader 使用的 cIOS](./cios-for-usb-loader.png)

笔者在 4.1 和 4.3 系统中安装好 **Homebrew Channel**（以下简称 **HBC**） 之后，即可使用 **Some YAWMM Mod** 成功安装 cIOS。如果你还在使用老版本的 **HBC**，强烈建议你先把 **HBC** 升级到 v1.1.2 或以上版本，再继续后面的操作。

  ![4.1 系统中的 HBC](./hbc-1.1.2-use-ios61.png)


## 三、安装步骤

1. 把傻瓜包（.zip 文件）解压缩到 SD 卡或者 USB 设备的根目录：
  ![解压缩到 SD 卡](./extract-to-sd.png)

2. 在 **HBC** 运行 **Some YAWMM Mod**：
  ![运行 Some YAWMM Mod](./some-yawmm-mod.png)

3. **Select source device** 的时候
    - 通过 SD 卡安装的选择 **Wii SD Slot**：
    ![选择 SD 卡](./select-sd.png)
    - 通过 USB 设备安装的选择 **USB Mass Storage Device**：
    ![选择 USB 设备](./select-usb.png)

4. 进入 `wad/cIOS` 文件夹，按遥控器手柄上的 (+) 号键，把文件夹下的 6 个 .wad 文件都选上之后，按 (A) 键启动安装：
  ![选择 .wad 文件](./select-wads.png)

5. 耐心等待安装结束：
  ![正在安装](./installing.png)

6. 看到以下界面即表示安装成功：
  ![安装结束](./done.png)
