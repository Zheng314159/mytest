#!/bin/bash

# 切换到程序所在目录（可选）
cd "$(dirname "$0")"

# 启动代理客户端
./myclient > client.log 2>&1 &
echo "Proxy client started. Logs: client.log"
