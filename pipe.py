from os import path, walk
from typing import List

from bitbucket_pipes_toolkit import Pipe


def discover(folder: str) -> List[str]:
    test_reports: List[str] = []
    for (_, _, filenames) in walk(folder):
        for filename in filenames:
            if path.splitext(filename)[1][1:].lower() == "xml":
                test_reports.append(filename)

    return test_reports


variables = {
    "ARTEFACT_UPLOADER_API_KEY": {"type": "string", "required": True},
    "TEST_REPORT_LOCATION": {"type": "string", "required": True},
}

pipe = Pipe(schema=variables)
api_key = pipe.get_variable("ARTEFACT_UPLOADER_API_KEY")
test_report_location = pipe.get_variable("TEST_REPORT_LOCATION")

pipe.log_info(f"Discovering test reports in {test_report_location}...")

reports = discover(test_report_location)

pipe.log_info(f"Discovered test reports: {reports}.")

pipe.success(message="Success!")
