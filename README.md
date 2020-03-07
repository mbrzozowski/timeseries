### Prerequisites
#### Using nix-shell
* Install [nix-shell](https://nixos.org/nix/manual/):
```bash
curl https://nixos.org/nix/install | sh
```
* Run it:
```bash
nix-shell shell.nix --pure
```

#### Manual
* Alternatively install:
```
docker, docker-compose, python3.6, virtualenv, postgresql-devel
```
* Prepare virtualenv using ``requirements*.txt`` files.
* Activate virtualenv.

### Running

```bash
./setup.sh
```

### TODO
* Review
* Use WSGI server e.g. gunicorn
* Add logging
* Write more unittests
* Prepare Kubernetes deployment
* Rewrite to FastAPI?

### Swagger endpoint
Available at ``/api/v1/doc``.
