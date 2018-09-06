# imagechecker

Tell me if my images are out of date.

At the moment it scans your compose yaml files.

```
$ docker run --rm -it -v $(pwd):/data -e REGISTRY onaci/imagechecker --debug | sort
        OK: api-python.yml: fluentbit: fluent/fluent-bit:latest uses :latest
        OK: cronicle.yml: fluentbit: fluent/fluent-bit:latest uses :latest
        OK: cronicle.yml: frontend: svendowideit/cronicle:latest uses :latest
        OK: dashboard.yml: fluentbit: fluent/fluent-bit:latest uses :latest
        OK: elasticsearch.yml: fluentd: onaci/fluentd:latest uses :latest
        OK: gitlab.yml: fluentbit: fluent/fluent-bit:latest uses :latest
        OK: gitlab.yml: gitlab-runner: gitlab/gitlab-runner:latest uses :latest
        OK: ncwps.yml: fluentbit: fluent/fluent-bit:latest uses :latest
        OK: portainer.yml: agent: portainer/agent:latest uses :latest
        OK: portainer.yml: frontend: portainer/portainer:latest uses :latest
        OK: prometheus.yml: blackbox: prom/blackbox-exporter:latest uses :latest
        OK: prometheus.yml: cadvisor: google/cadvisor has same digest as latest tag
        OK: prometheus.yml: dockerd-exporter: stefanprodan/dockerd-exporter has same digest as latest tag
        OK: prometheus.yml: fluentbit: fluent/fluent-bit:latest uses :latest
        OK: registry.yml: registry: registry:2 has same digest as latest tag
        OK: scope.yml: app: weaveworks/scope:latest uses :latest
        OK: scope.yml: probe-launcher: weaveworks/scope-swarm-launcher:latest uses :latest
        OK: sima-swagger.yml: fluentbit: fluent/fluent-bit:latest uses :latest
        OK: thredds.yml: fluentbit: fluent/fluent-bit:latest uses :latest
        OK: traefik.yml: dummy: nginx:latest uses :latest
cloudflare/unsee:v0.8.0         ['v0.7.2', 'v0.8.0', 'v0.9.0', 'v0.9.1', 'v0.9.2']
docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.4         ['6.4.0', '6.4.0-SNAPSHOT', '6.4.1-SNAPSHOT', '6.5.0-SNAPSHOT', '7.0.0-alpha1-SNAPSHOT']
docker.elastic.co/kibana/kibana-oss:6.2.4               ['6.4.0', '6.4.0-SNAPSHOT', '6.4.1-SNAPSHOT', '6.5.0-SNAPSHOT', '7.0.0-alpha1-SNAPSHOT']
mongo:3.2               ['windowsservercore', 'windowsservercore-1709', 'windowsservercore-1803', 'windowsservercore-ltsc2016', 'xenial']
sameersbn/gitlab:11.0.4         ['9.5.4', '9.5.5', 'latest', 'master', 'v8.9.4']
sameersbn/postgresql:10         ['9.6-1', '9.6-2', '9.6-3', '9.6-4', 'latest']
sameersbn/redis:4.0.9           ['3.0.6', '4.0.9', '4.0.9-1', 'latest']
stefanprodan/swarmprom-alertmanager:v0.14.0             ['latest', 'v0.14.0', 'v0.9.1']
stefanprodan/swarmprom-grafana:5.0.1            ['4.6.0', '4.6.3', '5.0.1', 'latest']
stefanprodan/swarmprom-node-exporter:v0.15.2            ['latest', 'v0.14.0', 'v0.15.2']
stefanprodan/swarmprom-prometheus:v2.2.0-rc.0           ['latest', 'v1.8.2', 'v2.2.0-rc.0']
traefik:v1.6.6-alpine           ['v1.7.0-rc2-alpine', 'v1.7.0-rc3', 'v1.7.0-rc3-alpine', 'v1.7.0-rc3-nanoserver','v1.7.0-rc3-nanoserver-sac2016']
```
