# 电梯电瓶车报警

## 功能概述
镜头前出现电瓶车立即报警，不会对同一辆车重复报警。本服务和[猫猫围栏](../cat_finder/README.zh.md)在推送时机上有区别：猫离开时才通知。

## 软硬件环境

*nix 系统（Linux/Mac），x86/ARM 芯片。支持 onnx runtime 即可。

## 模型下载

下载 [google](https://drive.google.com/file/d/1Ff8oxBer135L-wKnkgOewa91lF5EV05P/view?usp=sharing) 解压，软链到 examples/models 目录

```bash
$ cd flow-python/examples
$ ln -s ${DOWNLOAD_DIR}/models models
```

## 启动服务

安装 redis-server
```bash
$ sudo apt install redis-server
$ redis-server
```

准备一个 rtsp 视频流地址，做测试输入。

* laptop 或树莓派可搜索 Camera 推流教程。见 [如何生成自己的 rtsp 流地址](docs/how-to-generate-rtsp.zh.md)
* 也可以手机拍摄视频，再用 ffmpeg 转成 .ts 格式放到 live555 server。见 [如何生成自己的 rtsp 流地址](docs/how-to-generate-rtsp.zh.md)

启动服务
```bash
$ cd flow-python/examples
$ cargo run --example run_with_plugins -- -c electric_bicycle/electric_bicycle.toml  -p electric_bicycle
```
服务配置文件在`electric_bicycle/electric_bicycle.toml`，解释参考 [how-to-add-graph](docs/how-to-add-graph.zh.md) 。这里只需要打开 8083 端口服务，操作和[猫猫围栏](../cat_finder/README.zh.md) 近似。

```bash
$ google-chrome-stable  http://127.0.0.1:8083/docs 
```