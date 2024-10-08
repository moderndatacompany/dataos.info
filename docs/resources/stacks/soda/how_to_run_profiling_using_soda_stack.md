# How to run profiling using Soda Stack?

```yaml
name: profile-soda
version: v1
type: workflow
tags:
  - profile
description: this jobs profile data
workflow:
  dag:
    - name: sample-profile-soda-01
      title: Sample profile data
      spec:
        stack: soda+python:1.0
        soda:
            - dataset: dataos://icebase:retail/customer
              checks:
                - row_count between 10 and 1000:
                    attributes:
                      category: Accuracy                  
                - missing_count(birth_date) = 0:
                    attributes:
                      category: Completeness 

                # - invalid_percent(phone) < 1 %:
                #     valid format: phone number
                - invalid_count(number_cars_owned) = 0:
                    valid min: 1
                    valid max: 6
                    attributes:
                      category: Validity
                - duplicate_count(phone) = 0:
                    attributes:
                      category: Uniqueness

              profile:
                columns:
                  - "*"
              engine: minerva
            - dataset: dataos://icebase:retail/customer_360
              checks:
                - row_count between 10 and 1000
                - missing_count(birth_date) = 0
                - invalid_percent(phone) < 1 %:
                    valid format: phone number
                - invalid_count(number_cars_owned) = 0:
                    valid min: 1
                    valid max: 6
                - duplicate_count(phone) = 0
              profile:
                columns:
                  - "*"
```