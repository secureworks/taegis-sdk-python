import json
from dataclasses import dataclass, field, MISSING
from datetime import datetime
from typing import Any, Dict


@dataclass
class ExecutionHistory:
    """ This class is part of the execution history.
    User can track the executions during run-time"""
    query_name: str
    query_type: str
    query_arguments: Dict[str, Any]
    endpoint: str
    pretty_query: str
    duration: str = field(init=False)
    function_name: str = field(init=False)
    timestamp: float = field(default=datetime.timestamp(datetime.now()))
    execution_time: str = field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

    def as_json(self):
        """ returns the history item as json object"""
        data = {
            'query_name': self.query_name,
            'query_type': self.query_type,
            'endpoint': self.endpoint,
            'function_name': self.function_name,
            'query_arguments': self.query_arguments,
            'date_time': self.execution_time if self.execution_time else "",
            'duration': self.duration if self.duration else ""
        }

        return json.dumps(data, indent=4)
