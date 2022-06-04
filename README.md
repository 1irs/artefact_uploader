# Bitbucket Pipelines Pipe:  1IRS Test Reports Uploader

Uploads test reports to AWS S3 along with additional metadata.

## YAML Definition

Add the following snippet to the script section of your `bitbucket-pipelines.yml` file:

```yaml
- pipe: obrizan/artefact_uploader
  variables:
    ARTEFACT_UPLOADER_API_KEY: '<string>'
    TEST_REPORT_LOCATION: '<string>'
```

## Variables

| Variable                      | Usage                                 |
|-------------------------------|---------------------------------------|
| ARTEFACT_UPLOADER_API_KEY (*) | API key to use the service.           |
| TEST_REPORT_LOCATION (*)      | folder where test reports are stored. |

_(*) = required variable._

## Details

It looks for JUnit XML reports in TEST_REPORT_LOCATION, compresses and uploads to the 
Test Report Analytical system.

## Examples

Basic example:
    
```yaml
script:
  - pipe: obrizan/artefact_uploader
    variables:
      ARTEFACT_UPLOADER_API_KEY: $ARTEFACT_UPLOADER_API_KEY
      TEST_REPORT_LOCATION: 'test_reports'
```

## Support

info@1irs.net

