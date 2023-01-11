thrift 协议学习笔记
===

## binary 编码格式

### 基础类型如何编码

### struct 类型如何编码

### request 格式

### response 格式

field id = 1 表示返回的是 exception
field id = 0 便是返回的是正常的结果

### exception 格式

## compact 编码格式

## framed vs unframed

unframed 会将数据直接写入到 socket

framed 格式，client/server 先将 request/response 写入到一个 buffer 中，最后先向 socket 中写入一个四字节的数据长度，再写入数据。

framed 格式下，请求的最大长度是 16384000 (16M)

引入 framed 格式的目的是为了方便异步处理器的实现。