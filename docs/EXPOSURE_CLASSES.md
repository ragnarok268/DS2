# Exposure Classes

DS2 assigns one or more exposure classes to observed packages.

- `NETWORK_SERVER`: Frameworks that expose inbound application interfaces such as FastAPI, Starlette, Flask, and Django.
- `NETWORK_CLIENT`: Packages that initiate outbound HTTP or API activity such as `requests` and `httpx`.
- `ASYNC_RUNTIME`: Async execution frameworks or packages that materially expand concurrent runtime behavior.
- `PROCESS_EXECUTION`: Subprocess launch or shell execution capability.
- `BROWSER_AUTOMATION`: Browser-driving frameworks such as Playwright and Selenium.
- `DATABASE_PERSISTENCE`: Persistent storage layers such as `sqlite3` and SQLAlchemy.
- `CACHE_OR_QUEUE`: Redis, Celery, and similar queue or cache surfaces.
- `FILESYSTEM_ACCESS`: Reserved for future finer-grained filesystem heuristics.
- `CLOUD_API`: Cloud service SDKs such as `boto3`.
- `SERIALIZATION_PARSER`: Serialization and parsing libraries that can widen ingest and parsing surface.
- `PLUGIN_OR_EXTENSION`: Plugin frameworks or extension hosts.
- `BUILD_ONLY`: Build-system dependencies not confirmed as runtime imports.
- `UNKNOWN`: Observed but not yet classified beyond package presence.
