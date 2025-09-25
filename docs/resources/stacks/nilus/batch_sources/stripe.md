# Stripe

Stripe is a financial infrastructure platform that enables businesses to accept online payments and manage their financial processes. It acts as a payment processor, allowing businesses to integrate payment processing into their websites, apps, and other online platforms.

!!! info
    Stripe does not support Depot. To configure connections, use service account credentials provided through the Instance Secret Resource in URI.


## Prerequisites

The following are the requirements for enabling Batch Data Movement in Stripe:

* A valid **Stripe API key** (must start with `sk_`)
* API keys should be stored securely, preferably in a **DataOS Instance Secret.**

!!! info
    - To create a Nilus Workflow for batch data movement in Stripe, an active API key is essential. Create a Stripe API key using the following document: [API Key](https://docs.stripe.com/keys).
    - To create an Instance Secret for your Nilus Workflow, contact the DataOS admin or DataOS Operator


Nilus also supports ingestion from multiple Stripe endpoints, which are described below:

??? note "Supported Endpoints"

    **Payments & Billing**

    | Endpoint         | Description                     |
    | ---------------- | ------------------------------- |
    | `charge`         | Payment charges                 |
    | `payment_intent` | Payment intents for processing  |
    | `payment_method` | Payment methods                 |
    | `refund`         | Refunds for charges             |
    | `payout`         | Transfers to connected accounts |

    **Customer Management**

    | Endpoint                | Description                    |
    | ----------------------- | ------------------------------ |
    | `customer`              | Customer details               |
    | `subscription`          | Customer subscriptions         |
    | `subscription_item`     | Individual subscription items  |
    | `subscription_schedule` | Scheduled subscription updates |

    **Products & Pricing**

    | Endpoint         | Description           |
    | ---------------- | --------------------- |
    | `product`        | Product catalog items |
    | `price`          | Product pricing       |
    | `coupon`         | Discount coupons      |
    | `promotion_code` | Promotional codes     |

    **Invoicing & Billing**

    | Endpoint       | Description              |
    | -------------- | ------------------------ |
    | `invoice`      | Customer invoices        |
    | `invoice_item` | Individual invoice items |
    | `credit_note`  | Credit notes             |
    | `tax_rate`     | Tax rate definitions     |

    **Additional Resources**

    | Endpoint              | Description               |
    | --------------------- | ------------------------- |
    | `event`               | Webhook events            |
    | `balance_transaction` | Balance history           |
    | `webhook_endpoint`    | Webhook configurations    |
    | `setup_intent`        | Setup for future payments |



## Sample workflow Config

The Stripe connector doesn't support Depot, so the user must pass the API key in the connection URI, as shown below.

```yaml
name: stripe-test
version: v1
type: workflow
tags:
    - stripe_source
    - nilus_batch
workflow:
  dag:
    - name: stripe-source
      spec:
        stack: nilus:1.0
        compute: runnable-default
        envs:
          - DATAOS_WORK_DIR: /etc/dataos/work
          - HEIMDALL_URL: "<https://pro-alien.dataos.app/heimdall>"
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
        logLevel: INFO
        stackSpec:
          source:
            address: "stripe://?api_key=<api-key-here>"
            options:
              source-table: "customer"
              max-table-nesting: "0"
          sink:
            address: dataos://testawslh:sandbox/strip_test?acl=rw  
            options:  
              incremental-strategy: replace  
```

!!! info
    Ensure that all placeholder values and required fields (e.g., connection `addresses`, `compute`, and access credentials) are properly updated before applying the configuration to a DataOS workspace.


Deploy the manifest file using the following command:

```bash
dataos-ctl resource apply -f ${{path to the Nilus Workflow YAML}}
```

## Supported Attribute Details

Nilus supports the following source options for Stripe:

| Option         | Required | Description                                                                      |
| -------------- | -------- | -------------------------------------------------------------------------------- |
| `source-table` | Yes      | Stripe endpoint (e.g., `charges`, `customers:sync`, `invoices:sync:incremental`) |
