import os

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import ProxyTracerProvider  # noqa


def setup_telemetry():
    existing_provider = trace.get_tracer_provider()
    if not isinstance(existing_provider, ProxyTracerProvider):
        print("Provider already configured not reconfiguring...")
    else:
        DjangoInstrumentor().instrument()
        LoggingInstrumentor().instrument()
        resource = Resource.create(
            {
                SERVICE_NAME: 'webapp',
            }
        )
        endpoint = f"http://{os.getenv('TRACING_HOST')}:{os.getenv('TRACING_PORT')}"
        provider = TracerProvider(resource=resource)
        provider.add_span_processor(
            BatchSpanProcessor(
                OTLPSpanExporter(
                    endpoint=endpoint,
                    insecure=True
                )
            )
        )
        trace.set_tracer_provider(provider)
