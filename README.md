# NodeJsScan

Static security code scanner (SAST) for Node.js applications.

### How to Configure

1. Install Postgres and configure `SQLALCHEMY_DATABASE_URI` in `core/settings.py`
2. Run `pip install -r requirements.txt`
3. Run `python createdb.py`
4. Run `python app.py`

This will run NodeJsScan on `http://0.0.0.0:9090`
If you need to debug, set `DEBUG = True` in `core/settings.py`

### NodeJsScan CLI

The command line interface (CLI) allows you to integrate NodeJsScan with DevSecOps CI/CD pipelines. The results are in JSON format. When you use CLI the results are never stored with NodeJsScan backend.

`python cli.py -d <node_js_source_code_dir>`

### Learn Node.js Security: Pentesting and Exploitation
[OpSecX Video Course](https://opsecx.com/index.php/product/node-js-security-pentesting-and-exploitation/)

### Docker

```
docker build -t nodejsscan .
docker run -it -p 9090:9090 nodejsscan
```

### DockerHub

```
docker pull opensecurity/nodejsscan
docker run -it -p 9090:9090 opensecurity/nodejsscan:latest
```

#### NodeJsScan Web UI
![NodeJsScan V2](https://cloud.githubusercontent.com/assets/4301109/22619224/26acd162-eb16-11e6-8f28-bd477c92991f.png)

#### Static Analysis
![NodeJsScan Static Scan Results](https://user-images.githubusercontent.com/4301109/33951861-294062a0-e056-11e7-8472-3c101be52390.jpg)
![NodeJsScan Static Scan Vulnerability Details](https://user-images.githubusercontent.com/4301109/30637698-bfa68e04-9e16-11e7-8233-bfde503d7e5a.png)

