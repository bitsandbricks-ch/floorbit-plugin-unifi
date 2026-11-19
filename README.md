# UniFi for Floorbit

[![Test and release](https://github.com/bitsandbricks-ch/floorbit-plugin-unifi/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/bitsandbricks-ch/floorbit-plugin-unifi/actions/workflows/release.yml?query=branch%3Amain)

The `unifi` plugin for [Floorbit](https://github.com/bitsandbricks-ch/floorbit): UniFi as a monitoring source: switch status, ports and traffic, and which switch port an IP or MAC is on.
Install it under Settings > Plugins > Marketplace; how to set it up is in Floorbit's
[docs/plugins.md](https://github.com/bitsandbricks-ch/floorbit/blob/master/docs/plugins.md).

## What is where

| File | What |
| --- | --- |
| `plugin.yaml` | The manifest: settings and what it may touch. |
| `plugin.py` | The plugin. Floorbit runs it on the local agent in the hall, which reaches UniFi on the event network. |
| `tests/` | Tests against a fake UniFi, with Floorbit at the commit in `FLOORBIT_REF`. No network. |

## Testing

```
git clone https://github.com/bitsandbricks-ch/floorbit ../floorbit
git -C ../floorbit checkout "$(cat FLOORBIT_REF)"
pip install -r ../floorbit/requirements.txt pytest ruff
ruff check --config ../floorbit/pyproject.toml --config 'lint.isort.known-third-party=["floorbit"]' .
PYTHONPATH=../floorbit python -m pytest -q tests
```

## Releasing

Put the new version into `plugin.yaml`, add a `## <version>` section to `CHANGELOG.md`, merge, then
push the tag (or `mason release tag floorbit-plugin-unifi`):

```
git tag v1.0.0 && git push origin v1.0.0
```

The [workflow](.github/workflows/release.yml) tests it, signs `unifi-<version>.tar.gz` with the
Floorbit plugin key (environment `plugin-signing`, secret `FLOORBIT_PLUGIN_SIGNING_KEY`) and
attaches it to the GitHub release. The Marketplace picks it up within the hour. A version is
withdrawn in [floorbit-plugins](https://github.com/bitsandbricks-ch/floorbit-plugins)' `plugins.yaml`,
never by deleting the release.
