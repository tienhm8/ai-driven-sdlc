# Exception handling

Preserve the endpoint's status, error code, and response shape. Check the app's configured `CommonExceptionFilter` and `TransformResponseInterceptor`, then follow the closest route that exposes the same kind of failure. Map known domain failures to the documented client error; unexpected failures should not reveal implementation detail. Correlate diagnostics with the existing request context and keep credentials, stack traces, and raw database errors out of responses. Do not assume that an HTTP error mapping is the wire contract for gRPC or TCP.
