# How to run Soda checks on a specific branch of Iceberg dataset?

```yaml
name: soda-city-01
version: v1
type: workflow
tags:
  - workflow
  - soda-checks
description: Random User Console
workspace: public
workflow:
  dag:
    - name: soda-job-v2
      title: soda Sample Test Job
      description: This is sample job for soda dataos sdk
      spec:
        stack: soda+python:1.0
        compute: runnable-default
        resources:
          requests:
            cpu: 250m
            memory: 250Mi
          limits:
            cpu: 1000m
            memory: 250Mi
        logLevel: DEBUG # WARNING, ERROR, DEBUG
        stackSpec:
          inputs:
            - dataset: dataos://icebase:retail/city?acl=rw
              options:
                branchName: b1 # branch name
                engine: minerva
                clusterName: miniature
              profile:
                columns:
                  - "*"
              checks:
                - row_count between 10 and 1000
                - missing_count(zip_code) = 0
                - invalid_count(zip_code) < 0:
                    valid min: 500
                    valid max: 99403
                    filter: state_code = 'AL'
                - duplicate_count(zip_code) = 0
                - duplicate_count(zip_code) > 10
                - duplicate_percent(zip_code) < 0.10
                - failed rows:
                    samples limit: 70
                    fail condition: zip_code < 18  and zip_code >= 50
                - freshness(ts_city) < 1d
                - max_length(state_name) = 8
                - schema:
                    name: Confirm that required columns are present
                    warn:
                      when required column missing: [city_name, city_name]
                    fail:
                      when required column missing:
                        - city_id
                        - no_phone
                - schema:
                    fail:
                      when forbidden column present: [Pii*]
                      when wrong column type:
                        state_code: DOUBLE
```