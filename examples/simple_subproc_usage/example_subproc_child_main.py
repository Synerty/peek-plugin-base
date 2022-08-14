import logging
import sys

from twisted.internet import reactor
from twisted.internet._posixstdio import StandardIO

from examples.simple_subproc_usage.example_subproc_class import (
    ExampleSubprocClass,
)
from peek_plugin_base.simple_subproc.simple_subproc_child_protocol import (
    SimpleSubprocChildProtocol,
)

logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)


if __name__ == "__main__":
    # Create a class to construct.
    StandardIO(SimpleSubprocChildProtocol(ExampleSubprocClass))

    reactor.run()
