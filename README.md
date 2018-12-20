# Static paullaroid.pycon.fr

## Initial setup

The `db.json` file is just an extract of the CouchDB server.

```
python3 crawl.py
mkdir -p pictures/{2015,2016}
mv 2015-*.jpg pictures/2015/
mv 2016-*.jpg pictures/2016/
pip install sigal
sigal init
sigal build
```

## Rebuild

To rebuild the gallery, install `sigal` and run `sigal build`.
