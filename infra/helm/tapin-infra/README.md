Tapin Infra Helm chart

This chart provides a starting point to deploy the components required for Tapin-live on Kubernetes.

Included components:
- LiveKit server
- coturn
- backend (FastAPI)
- Postgres (stateful)
- Redis

Usage (dev/local):
1. Customize infra/helm/tapin-infra/values.yaml with appropriate image tags, LIVEKIT keys, and coturn external IP.
2. Install the chart:
   helm install tapin-infra infra/helm/tapin-infra
3. Verify pods and services are running:
   kubectl get pods
   kubectl get svc

Production notes:
- Use Secrets objects (Kubernetes Secret) for database and LiveKit credentials rather than plain values.yaml.
- Configure a proper PersistentVolume for Postgres (and backups).
- Expose LiveKit and backend through an ingress with TLS; use cert-manager or managed certs.
- Tune resource requests/limits and enable autoscaling for LiveKit based on CPU.
- coturn must be configured with a stable external IP and firewall rules that allow UDP/TCP 3478 and relayed ports.
