import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
