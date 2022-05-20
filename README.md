# python-grpc-boostrap

    服务需要添加到services文件夹中，重启grpc服务后会自动加载 
    首次部署需要在settings增加"__init__.py"文件，参考"__init__.py.example"

## install

```shell
pip install grpcio -i https://pypi.douban.com/simple
pip install grpcio-tools -i https://pypi.douban.com/simple
```

## build

```shell
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I . ./protos/*.proto
```

## server

```shell
python3 grpc_server.py
```

## test

```shell
python3 grpc_client.py
```

### 赞赏

![image](./appreciate.jpeg)