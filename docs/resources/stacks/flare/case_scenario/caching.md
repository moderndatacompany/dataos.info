# Caching


Caching puts a copy of intermediately transformed dataset into memory, allowing us to repeatedly access it at a much lower cost than running the entire pipeline again.

## Code Snippet

```yaml
version: v1
name: connect-labor-history-new
type: workflow
tags:
  - Report-Table
description: Labor History enriched data workflow
title: Labor History New Enriched
workflow:
  dag:
    - name: connect-labor-history-load-new
      title: Labor History Enriched
      description: This job creates Labor history New enriched data
      spec:
        tags:
          - Report-Table
        stack: flare:5.0
        tempVolume: 500Gi
        stackSpec:
          driver:
            coreLimit: 3500m
            cores: 1
            memory: 4000m
          executor:
            coreLimit: 7000m
            cores: 3
            instances: 2
            memory: 18000m
          job:
            explain: true
            inputs:
              - name: labor_history_new
                dataset: dataos://icebase:temp_view/labor_history
                format: iceberg
              - name: labor_history_amount
                dataset: dataos://icebase:report/labor_history_amount
                format: iceberg
              - name: currency_type
                dataset: dataos://icebase:gcdcore_bronze/gcdcore_currency_type
                format: iceberg
              - name: fiscal_period
                dataset: dataos://icebase:report/fiscal_period
                format: iceberg
              - name: fiscal_week
                dataset: dataos://icebase:report/fiscal_week
                format: iceberg
              - name: employee_history
                dataset: dataos://icebase:report/employee_history
                format: iceberg
              - name: project
                dataset: dataos://icebase:report/gcdcore_project_current
                format: iceberg
              - name: currency_exchange_consolidation
                dataset: dataos://icebase:report/currency_exchange_consolidation
                format: iceberg
              - name: organization_new
                dataset: dataos://icebase:gcdcore_silver_new/gcdcore_organization
                format: iceberg

            logLevel: ERROR
            outputs:
              - name: enriched
                depot: dataos://icebase:report?acl=rw
            steps:
              - sequence:
                  - name: labor_history_helper
                    sql: >
                      SELECT DISTINCT
                          *,
                          CASE
                            WHEN
                              (
                                post_trans_type IN ('BL','LA')
                                OR
                                ( post_trans_type IS NULL AND xfer_project_id IS NOT NULL )
                                OR
                                ( post_trans_type IN ('BL','LA') AND bill_status = 'T' )
                              )
                              AND is_project_cost = 1
                              THEN 1
                            ELSE 0
                          END AS flag_hours_transferred,
                          CASE
                            WHEN (
                                post_trans_type NOT IN ('BL','LA')
                                OR
                                (
                                  post_trans_type IS NULL
                                  AND xfer_project_id IS NULL
                                )
                              )
                              AND is_project_cost = 1
                              THEN 1
                            ELSE 0
                          END AS flag_costs_available_to_bill,
                          CASE
                            WHEN (
                                post_trans_type IN ('BL','LA')
                                OR
                                (
                                  post_trans_type IS NULL
                                  AND xfer_project_id IS NOT NULL
                                )
                                OR
                                (
                                  post_trans_type IN ('BL','LA')
                                  AND bill_status = 'T'
                                )
                              )
                              AND is_project_cost = 1
                              THEN 0
                            ELSE 1
                          END AS flag_hours_non_transferred
                        FROM labor_history_new
                    functions:
                      - name: drop
                        columns:
                          - rn
                  - name: lh_hlper
                    sql: >
                      select *,
                      IFNULL(MIN(CASE WHEN batch != 'TimeKeeper' AND post_trans_type = 'TS' THEN 1
                                  WHEN batch = 'TimeKeeper' AND post_trans_type = 'TS' THEN 0
                                  ELSE NULL
                                END)
                            OVER(PARTITION BY fiscal_period_id_trans,fiscal_week_id_trans, employee_id),0)  is_timecard_manual
                      from labor_history_helper
                  - name: currency_type_billing
                    sql: SELECT currency_type_id FROM currency_type WHERE value = 'billing'

                  - name: currency_type_functional
                    sql: SELECT currency_type_id FROM currency_type WHERE value = 'functional'

                  - name: currency_type_enterprise
                    sql: SELECT currency_type_id FROM currency_type WHERE value = 'enterprise'

                  - name: currency_type_reporting1
                    sql: SELECT currency_type_id FROM currency_type WHERE value = 'reporting_1'

                  - name: currency_type_reporting2
                    sql: SELECT currency_type_id FROM currency_type WHERE value = 'reporting_2'
                  - name: labor_history_amount_transposed
                    sql: >
                      SELECT distinct
                          labor_history_id,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_billing)
                                THEN CAST(cost_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS cost_amount_billing,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_billing)
                                THEN CAST(bill_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS bill_amount_billing,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_functional)
                                THEN CAST(cost_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS cost_amount_functional,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_functional)
                                THEN CAST(bill_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS bill_amount_functional,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_enterprise)
                                THEN CAST(cost_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS cost_amount_report_usd,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_enterprise)
                                THEN CAST(bill_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS bill_amount_report_usd,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_reporting1)
                                THEN CAST(cost_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS cost_amount_report_gbp,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_reporting1)
                                THEN CAST(bill_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS bill_amount_report_gbp,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_reporting2)
                                THEN CAST(cost_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS cost_amount_report_cny,
                          SUM(CASE WHEN currency_type_id = (SELECT * FROM currency_type_reporting2)
                                THEN CAST(bill_amount AS NUMERIC(19,4))
                              ELSE 0
                            END) AS bill_amount_report_cny
                          FROM  labor_history_amount
                          GROUP BY labor_history_id

                  - name: df_fpp
                    sql: >
                      SELECT DISTINCT
                        lh.labor_history_id,
                        lh.period,
                        lh.postseq,
                        lh.pkey,
                        lh.trans_date,
                        lh.trans_type,
                        lh.is_timecard_manual,
                        CASE
                          WHEN lh.batch != 'TimeKeeper' AND lh.post_trans_type = 'TS'
                              AND lh.is_timecard_manual = 0
                            THEN 1
                          ELSE 0
                        END AS is_timecard_correction,
                        lh.post_date,
                        lh.post_trans_type,
                        lh.fiscal_period_id_post,
                        lh.fiscal_period_id_trans,
                        lh.fiscal_period_id_xfer,
                        lh.employee_productivity_code AS  employee_productivity_type,
                        lh.admin_tech   AS  employee_admin_technical,
                        lh.employee_productivity_code AS employee_productivity_type_post,
                        lh.admin_tech   AS employee_admin_technical_post,
                        lh.total_hours,
                        CASE
                        WHEN lh.flag_hours_transferred = 1
                          THEN lh.total_hours
                        ELSE 0
                        END AS total_hours_transferred,
                        lh.timecard_comment,
                        CASE
                          WHEN lh.admin_tech = 'technical' THEN lh.total_hours
                          ELSE 0
                        END AS tech_employee_hours,
                        CASE
                          WHEN lh.admin_tech = 'admin' THEN lh.total_hours
                          ELSE 0
                        END AS admin_employee_hours,
                        lh.level1_labor_code,
                        lh.level1_labor_code_label,
                        lh.level2_labor_code,
                        lh.level2_labor_code_label,
                        lh.level3_labor_code,
                        lh.level3_labor_code_label,
                        lh.level4_labor_code,
                        lh.level4_labor_code_label,
                        lh.is_project_cost,
                        lh.bill_status,

                        lh.xfer_project_id,
                        lh.office_id_employee,
                        lh.flag_hours_transferred,
                        lh.flag_costs_available_to_bill,
                        lh.flag_hours_non_transferred,
                        lh.project_id,
                        lh.admin_tech,
                        lh.fiscal_week_id_post,
                        lh.fiscal_week_id_trans,
                        lh.employee_id,

                        fpp.fiscal_year_id AS fiscal_year_id_post,
                        fpp.fiscal_year_period_code AS fiscal_year_period_code_post,
                        fpp.fiscal_year_code AS fiscal_year_code_post,
                        fpp.fiscal_year_start_date AS fiscal_year_start_date_post,
                        fpp.fiscal_year_end_date AS fiscal_year_end_date_post,
                        fpp.fiscal_period_code AS fiscal_period_code_post,
                        fpp.fiscal_period_start_date AS fiscal_period_start_date_post,
                        fpp.fiscal_period_end_date AS fiscal_period_end_date_post,
                        fpp.fiscal_period_is_closed AS fiscal_period_post_is_closed,
                        fpp.fiscal_period_weeks_count AS fiscal_period_weeks_count_post,

                        fpp.fiscal_period_calendar_month_name AS fiscal_period_calendar_month_name_post,
                        fpp.fiscal_period_calendar_month_abbreviated AS fiscal_period_calendar_month_abbreviated_post,
                        fpp.fiscal_period_calendar_year4 AS fiscal_period_calendar_year4_post,
                        fpp.fiscal_period_calendar_year2 AS fiscal_period_calendar_year2_post,
                        fpp.fiscal_period_calendar_month_year AS fiscal_period_calendar_month_year_post,

                        fpp.index_yoy_fiscal_year_to_date_current AS index_yoy_fiscal_year_to_date_current_post,
                        fpp.index_yoy_3_period_current AS index_yoy_3_period_current_post,
                        fpp.index_yoy_6_period_current AS index_yoy_6_period_current_post,
                        fpp.index_yoy_12_period_current AS index_yoy_12_period_current_post,
                        fpp.index_rolling_3_fiscal_year_current AS index_rolling_3_fiscal_year_current_post,
                        fpp.index_rolling_5_fiscal_year_current AS index_rolling_5_fiscal_year_current_post,

                        fpp.index_yoy_fiscal_year_to_date_max_closed AS index_yoy_fiscal_year_to_date_max_closed_post,
                        fpp.index_yoy_3_period_max_closed AS index_yoy_3_period_max_closed_post,
                        fpp.index_yoy_6_period_max_closed AS index_yoy_6_period_max_closed_post,
                        fpp.index_yoy_12_period_max_closed AS index_yoy_12_period_max_closed_post,
                        fpp.index_rolling_3_fiscal_year_max_closed AS index_rolling_3_fiscal_year_max_closed_post,
                        fpp.index_rolling_5_fiscal_year_max_closed AS index_rolling_5_fiscal_year_max_closed_post,

                        fpp.current_period_basis_date,
                        fpp.fiscal_year_period_code_current,
                        fpp.fiscal_year_code_current,
                        fpp.fiscal_period_start_date_current,
                        fpp.fiscal_period_end_date_current,
                        fpp.fiscal_year_start_date_current,
                        fpp.fiscal_year_end_date_current,

                        fpp.fiscal_period_distance_current,
                        fpp.fiscal_year_distance_current,

                        fpp.fiscal_year_period_code_min_open,
                        fpp.fiscal_year_period_code_max_closed,
                        fpp.fiscal_year_code_max_closed,
                        fpp.fiscal_period_start_date_max_closed,
                        fpp.fiscal_period_end_date_max_closed,

                        fpp.fiscal_period_distance_max_closed,
                        fpp.fiscal_year_distance_max_closed

                        FROM lh_hlper lh
                        LEFT JOIN fiscal_period fpp
                        ON lh.fiscal_period_id_post = fpp.fiscal_period_id
                  - name: df_fpt
                    sql: >
                      SELECT DISTINCT lh.*,
                        fpt.fiscal_year_period_code AS fiscal_year_period_code_trans,
                        fpt.fiscal_year_code AS fiscal_year_code_trans,
                        fpt.fiscal_year_start_date AS fiscal_year_start_date_trans,
                        fpt.fiscal_year_end_date AS fiscal_year_end_date_trans,
                        fpt.fiscal_period_code AS fiscal_period_code_trans,
                        fpt.fiscal_period_start_date AS fiscal_period_start_date_trans,
                        fpt.fiscal_period_end_date AS fiscal_period_end_date_trans,
                        fpt.fiscal_period_is_closed AS fiscal_period_trans_is_closed,
                        fpt.fiscal_period_weeks_count AS fiscal_period_weeks_count_trans,

                        fpt.fiscal_period_calendar_month_name AS fiscal_period_calendar_month_name_trans,
                        fpt.fiscal_period_calendar_month_abbreviated AS fiscal_period_calendar_month_abbreviated_trans,
                        fpt.fiscal_period_calendar_year4 AS fiscal_period_calendar_year4_trans,
                        fpt.fiscal_period_calendar_year2 AS fiscal_period_calendar_year2_trans,
                        fpt.fiscal_period_calendar_month_year AS fiscal_period_calendar_month_year_trans,

                        fpt.index_yoy_fiscal_year_to_date_current AS index_yoy_fiscal_year_to_date_current_trans,
                        fpt.index_yoy_3_period_current AS index_yoy_3_period_current_trans,
                        fpt.index_yoy_6_period_current AS index_yoy_6_period_current_trans,
                        fpt.index_yoy_12_period_current AS index_yoy_12_period_current_trans,
                        fpt.index_rolling_3_fiscal_year_current AS index_rolling_3_fiscal_year_current_trans,
                        fpt.index_rolling_5_fiscal_year_current AS index_rolling_5_fiscal_year_current_trans,

                        fpt.index_yoy_fiscal_year_to_date_max_closed AS index_yoy_fiscal_year_to_date_max_closed_trans,
                        fpt.index_yoy_3_period_max_closed AS index_yoy_3_period_max_closed_trans,
                        fpt.index_yoy_6_period_max_closed AS index_yoy_6_period_max_closed_trans,
                        fpt.index_yoy_12_period_max_closed AS index_yoy_12_period_max_closed_trans,
                        fpt.index_rolling_3_fiscal_year_max_closed AS index_rolling_3_fiscal_year_max_closed_trans,
                        fpt.index_rolling_5_fiscal_year_max_closed AS index_rolling_5_fiscal_year_max_closed_trans

                        from df_fpp lh
                        LEFT JOIN fiscal_period fpt
                        ON lh.fiscal_period_id_trans = fpt.fiscal_period_id

                  - name: df_fpx
                    sql: >
                      SELECT DISTINCT lh.*,
                        fpx.fiscal_year_period_code AS fiscal_year_period_code_xfer,
                        fpx.fiscal_year_code AS fiscal_year_code_xfer,
                        fpx.fiscal_year_start_date AS fiscal_year_start_date_xfer,
                        fpx.fiscal_year_end_date AS fiscal_year_end_date_xfer,
                        fpx.fiscal_period_code AS fiscal_period_code_xfer,
                        fpx.fiscal_period_start_date AS fiscal_period_start_date_xfer,
                        fpx.fiscal_period_end_date AS fiscal_period_end_date_xfer,
                        fpx.fiscal_period_is_closed AS fiscal_period_xfer_is_closed,
                        fpx.fiscal_period_weeks_count AS fiscal_period_weeks_count_xfer,

                        fpx.fiscal_period_calendar_month_name AS fiscal_period_calendar_month_name_xfer,
                        fpx.fiscal_period_calendar_month_abbreviated AS fiscal_period_calendar_month_abbreviated_xfer,
                        fpx.fiscal_period_calendar_year4 AS fiscal_period_calendar_year4_xfer,
                        fpx.fiscal_period_calendar_year2 AS fiscal_period_calendar_year2_xfer,
                        fpx.fiscal_period_calendar_month_year AS fiscal_period_calendar_month_year_xfer,

                        fpx.index_yoy_fiscal_year_to_date_current AS index_yoy_fiscal_year_to_date_current_xfer,
                        fpx.index_yoy_3_period_current AS index_yoy_3_period_current_xfer,
                        fpx.index_yoy_6_period_current AS index_yoy_6_period_current_xfer,
                        fpx.index_yoy_12_period_current AS index_yoy_12_period_current_xfer,
                        fpx.index_rolling_3_fiscal_year_current AS index_rolling_3_fiscal_year_current_xfer,
                        fpx.index_rolling_5_fiscal_year_current AS index_rolling_5_fiscal_year_current_xfer,

                        fpx.index_yoy_fiscal_year_to_date_max_closed AS index_yoy_fiscal_year_to_date_max_closed_xfer,
                        fpx.index_yoy_3_period_max_closed AS index_yoy_3_period_max_closed_xfer,
                        fpx.index_yoy_6_period_max_closed AS index_yoy_6_period_max_closed_xfer,
                        fpx.index_yoy_12_period_max_closed AS index_yoy_12_period_max_closed_xfer,
                        fpx.index_rolling_3_fiscal_year_max_closed AS index_rolling_3_fiscal_year_max_closed_xfer,
                        fpx.index_rolling_5_fiscal_year_max_closed AS index_rolling_5_fiscal_year_max_closed_xfer

                        from df_fpt lh
                        LEFT JOIN fiscal_period fpx
                        ON lh.fiscal_period_id_xfer = fpx.fiscal_period_id

                  - name: df_fw_post
                    sql: >
                      SELECT DISTINCT lh.*,
                      fw_post.fiscal_week_id AS fw_post_fiscal_week_id_post,
                      fw_post.fiscal_year_week_number AS fiscal_year_week_number_post,
                      fw_post.fiscal_period_week_number AS fiscal_period_week_number_post,
                      fw_post.week_start_date AS week_start_date_post,
                      fw_post.week_end_date AS week_end_date_post,

                      fw_post.calender_year_week_number AS calendar_year_week_number_post,
                      fw_post.calendar_period_month_name AS calendar_period_month_name_post,
                      fw_post.calendar_week_month_name AS calendar_week_month_name_post,

                      fw_post.fiscal_year_week_number_current AS fiscal_year_week_number_current_post,
                      fw_post.fiscal_period_week_number_current AS fiscal_period_week_number_current_post,
                      fw_post.week_start_date_current AS week_start_date_current_post,
                      fw_post.week_end_date_current AS week_end_date_current_post,

                      fw_post.week_distance_current AS week_distance_current_post,
                      fw_post.index_rolling_4_week_current AS index_rolling_4_week_current_post,
                      fw_post.index_rolling_8_week_current AS index_rolling_8_week_current_post,
                      fw_post.index_rolling_12_week_current AS index_rolling_12_week_current_post,
                      fw_post.index_rolling_16_week_current AS index_rolling_16_week_current_post

                      from df_fpx lh
                      LEFT JOIN fiscal_week fw_post
                      ON lh.fiscal_week_id_post = fw_post.fiscal_week_id
                    functions:
                      - name: drop
                        columns:
                          - fiscal_week_id_post
                      - name: rename_all
                        columns:
                          fw_post_fiscal_week_id_post: fiscal_week_id_post

                  - name: df_fw_tran
                    sql: >
                      SELECT DISTINCT lh.*,
                      fw_tran.fiscal_week_id AS fw_tran_fiscal_week_id_trans,
                      fw_tran.fiscal_year_week_number AS fiscal_year_week_number_trans,
                      fw_tran.fiscal_period_week_number AS fiscal_period_week_number_trans,
                      fw_tran.week_start_date  AS week_start_date_trans,
                      fw_tran.week_end_date AS week_end_date_trans,

                      fw_tran.calender_year_week_number AS calendar_year_week_number_trans,
                      fw_tran.calendar_period_month_name AS calendar_period_month_name_trans,
                      fw_tran.calendar_week_month_name  AS calendar_week_month_name_trans,

                      fw_tran.fiscal_year_week_number_current  AS fiscal_year_week_number_current_trans,
                      fw_tran.fiscal_period_week_number_current  AS fiscal_period_week_number_current_trans,
                      fw_tran.week_start_date_current AS week_start_date_current_trans,
                      fw_tran.week_end_date_current AS  week_end_date_current_trans,

                      fw_tran.week_distance_current  AS week_distance_current_trans,
                      fw_tran.index_rolling_4_week_current  AS index_rolling_4_week_current_trans,
                      fw_tran.index_rolling_8_week_current  ASindex_rolling_8_week_current_trans,
                      fw_tran.index_rolling_12_week_current AS index_rolling_12_week_current_trans,
                      fw_tran.index_rolling_16_week_current AS index_rolling_16_week_current_trans

                      from df_fw_post lh
                      LEFT JOIN fiscal_week fw_tran
                      ON lh.fiscal_week_id_trans = fw_tran.fiscal_week_id

                    functions:
                      - name: drop
                        columns:
                          - fiscal_week_id_trans
                      - name: rename_all
                        columns:
                          fw_tran_fiscal_week_id_trans: fiscal_week_id_trans

                  - name: df_e1
                    sql: >
                      SELECT DISTINCT lh.*,
                      eh.employee_id eid,
                      eh.start_date AS  employee_start_date,
                      IFNULL(eh.first_name_preferred,eh.first_name_legal) AS employee_first_name,
                      IFNULL(eh.last_name_preferred,eh.last_name_legal) AS  employee_last_name,

                      eh.full_name AS employee_full_name,
                      eh.is_current_record  AS employee_is_current_record,

                      eh.office_hours_per_week  AS  employee_office_hours_per_week,
                      eh.hours_per_week AS  employee_hours_per_week,
                      eh.pay_type   AS  employee_pay_type,
                      eh.pay_rate_type AS employee_pay_rate_type,
                      eh.target_ratio   AS employee_target_ratio,
                      eh.fee_multiplier AS  employee_fee_multiplier,
                      eh.principal_staff  AS mployee_principal_staff,
                      eh.full_part_time AS  employee_full_part_time,
                      eh.regular_temp   AS employee_regular_temp,

                      eh.studio_name as eh_studio_name,
                      eh.practice_area_1_name as eh_practice_area_1_name,
                      eh.market_sector_1_name as eh_market_sector_1_name,

                      eh.worker_type,
                      eh.employee_type_vision,
                      eh.employee_type_name_vision,
                      eh.status_name  AS  employee_status_name,
                      eh.employee_number_base,
                      eh.employee_number_vision,
                      CAST(eh.bill_rate AS NUMERIC(19,4)) AS  employee_bill_rate,

                      eh.job_profile_name AS  employee_job_profile_name,
                      eh.physical_location  AS  employee_physical_location,
                      eh.employee_number_base_supervisor  AS employee_supervisor_number_base,
                      eh.employee_number_vision_supervisor AS employee_supervisor_number_vision,
                      eh.first_name_supervisor AS employee_supervisor_first_name,
                      eh.last_name_supervisor AS employee_supervisor_last_name,

                      eh.full_name_supervisor AS employee_supervisor_full_name,
                      eh.employee_supervisor_studio_name  AS employee_supervisor_studio_name,
                      eh.employee_supervisor_office_name  AS employee_supervisor_office_name,
                      eh.employee_supervisor_office_name_current AS employee_supervisor_office_name_current,
                      eh.studio_name  AS employee_supervisor_studio_name_current,
                      CAST(CASE WHEN lh.total_hours > eh.hours_per_week THEN lh.total_hours - eh.hours_per_week
                              ELSE 0
                            END AS NUMERIC(19,4))   overtime_hours,
                      eh.start_date esd,
                      eh.end_date eed,
                      eh.business_entity_code ebec
                      from df_fw_tran lh
                      LEFT JOIN employee_history eh
                      ON lh.employee_id = eh.employee_id

                    functions:
                      - name: drop
                        columns:
                          - employee_id
                      - name: rename_all
                        columns:
                          eid: employee_id
                  - name: df_eh
                    sql: >
                      select
                      distinct lh.*
                      from df_e1 lh
                      where lh.trans_date >= lh.esd
                      AND lh.trans_date <= lh.eed OR lh.eed IS NULL
                      AND LEFT(lh.ebec,1) != '9'
                    functions:
                      - name: drop
                        columns:
                          - esd
                          - eed
                          - ebec
                  - name: df_eh_post1
                    sql: >
                      SELECT DISTINCT lh.*,
                      eh_post.start_date                      employee_start_date_post,
                      eh_post.office_hours_per_week AS employee_office_hours_per_week_post,
                      eh_post.hours_per_week  AS employee_hours_per_week_post,
                      eh_post.pay_type    AS employee_pay_type_post,

                      eh_post.studio_name               eh_post_studio_name,
                      eh_post.studio_status_name        eh_post_studio_status_name,
                      eh_post.practice_area_1_name      eh_post_practice_area_1_name,
                      eh_post.market_sector_1_name      eh_post_market_sector_1_name,
                      eh_post.target_ratio  AS employee_target_ratio_post,
                      eh_post.fee_multiplier AS employee_fee_multiplier_post,
                      eh_post.principal_staff AS employee_principal_staff_post,
                      eh_post.full_part_time  AS employee_full_part_time_post,
                      eh_post.regular_temp  AS employee_regular_temp_post,
                      eh_post.worker_type   AS worker_type_post,
                      eh_post.employee_type_vision  AS employee_type_vision_post,
                      eh_post.employee_type_name_vision AS employee_type_name_vision_post,
                      eh_post.status_name   AS employee_status_name_post,
                      eh_post.employee_number_base AS employee_number_base_post,
                      eh_post.employee_number_vision AS employee_number_vision_post,
                      CAST(eh_post.bill_rate AS NUMERIC(19,4)) AS employee_bill_rate_post,

                      eh_post.studio_id,
                      eh_post.start_date epsd,
                      eh_post.end_date eped,
                      eh_post.business_entity_code epbec
                      from df_eh lh
                      LEFT JOIN employee_history eh_post
                      ON lh.employee_id = eh_post.employee_id

                  - name: df_eh_post
                    sql: >
                      select
                      distinct lh.*
                      from df_eh_post1 lh
                      where lh.trans_date >= lh.epsd
                      AND lh.trans_date <= lh.eped OR lh.eped IS NULL
                      AND LEFT(lh.epbec,1) != '9'
                    functions:
                      - name: drop
                        columns:
                          - epsd
                          - eped
                          - epbec

                  - name: emp_base
                    sql: SELECT DISTINCT employee_id FROM employee_history WHERE employee_number_base = '92367'
                  - name: df_emp
                    sql: cache table emp_base
                  - name: df_pr1
                    sql: >
                      SELECT DISTINCT lh.*,
                      pr.studio_name,
                      pr.practice_area_name,
                      pr.market_sector_name,
                      pr.studio_status_name,
                      pr.use_separate_terms,

                      pr.project_id              pr_project_id,
                      pr.project_number_1,
                      pr.project_name,
                      pr.project_name_long,
                      pr.org_code,
                      pr.org_code AS project_org_code,
                      pr.business_entity_code,
                      pr.business_entity_code AS project_business_entity_code,
                      pr.business_entity_name,
                      pr.business_entity_name AS project_business_entity_name,
                      pr.region_code,
                      pr.region_code AS project_region_code,
                      pr.region_name,
                      pr.region_name AS project_region_name,
                      pr.office_code,
                      pr.office_code AS project_office_code,
                      pr.office_name,
                      pr.office_name AS project_office_name,

                      pr.studio_name  AS project_studio_name,
                      pr.studio_status_name AS project_studio_status_name,

                      pr.country_name,
                      pr.country_name AS project_country_name,

                      pr.practice_area_industry_name  AS project_practice_area_industry_name,
                      pr.practice_area_name AS project_practice_area_name,
                      pr.market_sector_name AS project_market_sector_name,

                      pr.project_type_name,
                      pr.service_name   AS project_service_name,
                      pr.service_sub_name AS project_service_sub_name,
                      pr.delivery_approach_name AS project_delivery_approach_name,
                      pr.government_funded_name AS project_government_funded_name,
                      pr.is_residential   AS project_is_residential,
                      pr.status_name  AS project_status_name,
                      pr.charge_type_name,
                      pr.charge_type_name AS project_charge_type_name,

                      pr.fiscal_year_period_code_last_activity  AS project_fiscal_year_period_code_last_activity,

                      pr.base_project_number,
                      pr.base_project_name,

                      pr.billing_group_parent_project_number_1,
                      pr.billing_group_parent_project_name,

                      pr.currency_id_billing,
                      pr.currency_code_billing,
                      pr.currency_name_billing,

                      pr.currency_id_functional,
                      pr.currency_code_functional,
                      pr.currency_name_functional,

                      pr.currency_id_report_usd,
                      pr.currency_code_report_usd,
                      pr.currency_name_report_usd,

                      pr.currency_id_report_gbp,
                      pr.currency_code_report_gbp,
                      pr.currency_name_report_gbp,

                      pr.currency_id_report_cny,
                      pr.currency_code_report_cny,
                      pr.currency_name_report_cny

                      from df_eh_post lh
                      LEFT JOIN project pr
                      ON lh.project_id = pr.project_id
                    functions:
                      - name: drop
                        columns:
                          - project_id
                      - name: rename_all
                        columns:
                          pr_project_id: project_id
                  - name: df_pr
                    sql: >
                      select distinct pr.*,
                      CASE WHEN pr.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN pr.studio_name ELSE pr.eh_studio_name END                        employee_studio_name,
                      CASE WHEN pr.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN pr.practice_area_name ELSE pr.eh_practice_area_1_name END                employee_practice_area_1_name,
                      CASE WHEN pr.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN pr.market_sector_name ELSE pr.eh_market_sector_1_name END                employee_market_sector_1_name,

                      CASE WHEN pr.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN pr.studio_name ELSE pr.eh_post_studio_name END                        employee_studio_name_post,
                      CASE WHEN pr.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN pr.studio_status_name ELSE pr.eh_post_studio_status_name END                  employee_studio_status_name_post,
                      CASE WHEN pr.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN pr.practice_area_name ELSE pr.eh_post_practice_area_1_name END                employee_practice_area_1_name_post,
                      CASE WHEN pr.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN pr.market_sector_name ELSE pr.eh_post_market_sector_1_name END                employee_market_sector_1_name_post,

                      CASE
                            WHEN pr.flag_hours_transferred = 1
                              AND pr.charge_type_name = 'Billable'
                              THEN pr.total_hours
                            ELSE 0
                          END AS direct_hours_transferred,

                      CASE  WHEN pr.charge_type_name = 'Billable' THEN pr.total_hours
                            WHEN pr.charge_type_name IS NULL THEN NULL
                            ELSE 0
                        END AS direct_hours,
                        CASE  WHEN
                                pr.charge_type_name = 'Billable'
                                AND pr.admin_tech = 'technical'
                              THEN pr.total_hours
                            WHEN pr.charge_type_name IS NULL THEN NULL
                            ELSE 0
                        END AS tech_direct_hours,
                        CASE  WHEN
                                pr.charge_type_name = 'Billable'
                                AND pr.admin_tech = 'admin'
                              THEN pr.total_hours
                            WHEN pr.charge_type_name IS NULL THEN NULL
                            ELSE 0
                        END AS admin_direct_hours,

                        CASE
                            WHEN pr.charge_type_name = 'Billable' THEN 0
                            WHEN pr.charge_type_name IS NULL THEN NULL
                            ELSE pr.total_hours
                        END AS indirect_hours,
                        CASE
                            WHEN
                                pr.charge_type_name != 'Billable'
                                AND pr.admin_tech = 'technical'
                              THEN pr.total_hours
                            WHEN pr.charge_type_name IS NULL THEN NULL
                            ELSE 0
                        END AS tech_indirect_hours,
                        CASE

                            WHEN
                                pr.charge_type_name != 'Billable'
                                AND pr.admin_tech = 'admin'
                              THEN pr.total_hours
                            WHEN pr.charge_type_name IS NULL THEN NULL
                            ELSE 0
                        END AS admin_indirect_hours,

                        CASE  WHEN pr.charge_type_name = 'Promo'
                              THEN pr.total_hours
                            ELSE 0
                          END AS promotional_hours_total
                      from df_pr1 pr
                    functions:
                      - name: drop
                        columns:
                          - project_id
                          - eh_post_studio_name
                          - eh_post_studio_status_name
                          - eh_post_practice_area_1_name
                          - eh_post_market_sector_1_name
                  - name: df_lha_xp
                    sql: >
                      SELECT DISTINCT
                      lh.*,
                      CAST(lh.flag_costs_available_to_bill * lha_xp.bill_amount_billing AS NUMERIC(19,4))   labor_costs_available_to_bill_billing,

                      CAST(lh.flag_costs_available_to_bill * lha_xp.bill_amount_functional AS NUMERIC(19,4))  labor_costs_available_to_bill_functional,

                      CAST(lh.flag_costs_available_to_bill * lha_xp.bill_amount_report_usd AS NUMERIC(19,4))  labor_costs_available_to_bill_report_usd,

                      CAST(lh.flag_costs_available_to_bill * lha_xp.bill_amount_report_gbp AS NUMERIC(19,4))  labor_costs_available_to_bill_report_gbp,

                      CAST( lh.flag_costs_available_to_bill * lha_xp.bill_amount_report_cny AS NUMERIC(19,4)) labor_costs_available_to_bill_report_cny,

                      CASE WHEN lh.total_hours = 0
                      THEN CAST(employee_bill_rate AS NUMERIC(19,4))
                      ELSE CAST(lha_xp.bill_amount_billing/lh.total_hours AS NUMERIC(19,4))
                      END                               employee_override_rate,
                      CASE WHEN lh.total_hours = 0
                      THEN CAST(employee_bill_rate_post AS NUMERIC(19,4))
                      ELSE CAST(lha_xp.bill_amount_billing/lh.total_hours AS NUMERIC(19,4))
                      END                               employee_override_rate_post,
                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.cost_amount_billing ELSE 0 END AS  direct_cost_amount_billing,
                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.bill_amount_billing ELSE 0 END AS direct_bill_amount_billing,
                      CASE WHEN lh.charge_type_name = 'Billable' THEN 0
                      WHEN lh.charge_type_name IS NULL THEN NULL
                      ELSE lha_xp.cost_amount_billing
                      END                                         indirect_cost_amount_billing,
                      CASE WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE lha_xp.bill_amount_billing
                      END                                         indirect_bill_amount_billing,

                      lha_xp.bill_amount_billing                                total_bill_amount_billing,

                      CAST(lh.flag_hours_transferred * lha_xp.bill_amount_billing AS NUMERIC(19,4))     labor_costs_transferred_billing,
                      CAST(lh.flag_hours_non_transferred * lha_xp.bill_amount_billing AS NUMERIC(19,4))   labor_costs_non_transferred_billing,

                      lha_xp.cost_amount_functional,
                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.cost_amount_functional ELSE 0 END  direct_cost_amount_functional,
                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.bill_amount_functional ELSE 0 END  direct_bill_amount_functional,
                      CASE  WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE lha_xp.cost_amount_functional
                      END                                             indirect_cost_amount_functional,
                      CASE  WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE lha_xp.bill_amount_functional
                      END                                             indirect_bill_amount_functional,

                      lha_xp.bill_amount_functional,

                      lha_xp.bill_amount_functional                               total_bill_amount_functional,

                      CAST(lh.flag_hours_transferred * lha_xp.bill_amount_functional AS NUMERIC(19,4))    labor_costs_transferred_functional,
                      CAST(lh.flag_hours_non_transferred * lha_xp.bill_amount_functional AS NUMERIC(19,4))  labor_costs_non_transferred_functional,

                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.cost_amount_report_usd ELSE 0 END  direct_cost_amount_report_usd,
                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.bill_amount_report_usd ELSE 0 END  direct_bill_amount_report_usd,
                      CASE  WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE lha_xp.cost_amount_report_usd
                      END                                             indirect_cost_amount_report_usd,
                      CASE  WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE lha_xp.bill_amount_report_usd
                      END                                             indirect_bill_amount_report_usd,

                      lha_xp.bill_amount_report_usd                               total_bill_amount_report_usd,

                      CAST(lh.flag_hours_transferred * lha_xp.bill_amount_report_usd AS NUMERIC(19,4))    labor_costs_transferred_report_usd,
                      CAST(lh.flag_hours_non_transferred * lha_xp.bill_amount_report_usd AS NUMERIC(19,4))  labor_costs_non_transferred_report_usd,

                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.cost_amount_report_gbp ELSE 0 END  direct_cost_amount_report_gbp,
                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.bill_amount_report_gbp ELSE 0 END  direct_bill_amount_report_gbp,
                      CASE  WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE lha_xp.cost_amount_report_gbp
                      END                                             indirect_cost_amount_report_gbp,
                      CASE  WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE lha_xp.bill_amount_report_gbp
                      END                                             indirect_bill_amount_report_gbp,

                      lha_xp.bill_amount_report_gbp                               total_bill_amount_report_gbp,

                      CAST(lh.flag_hours_transferred * lha_xp.bill_amount_report_gbp AS NUMERIC(19,4))    labor_costs_transferred_report_gbp,
                      CAST(lh.flag_hours_non_transferred * lha_xp.bill_amount_report_gbp AS NUMERIC(19,4))  labor_costs_non_transferred_report_gbp,

                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.cost_amount_report_cny ELSE 0 END  direct_cost_amount_report_cny,
                      CASE lh.charge_type_name WHEN 'Billable' THEN lha_xp.bill_amount_report_cny ELSE 0 END  direct_bill_amount_report_cny,
                      CASE  WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE lha_xp.cost_amount_report_cny
                      END                                             indirect_cost_amount_report_cny,
                      CASE  WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE lha_xp.bill_amount_report_cny
                      END                                             indirect_bill_amount_report_cny,

                      lha_xp.bill_amount_report_cny                               total_bill_amount_report_cny,

                      CAST(lh.flag_hours_transferred * lha_xp.bill_amount_report_cny AS NUMERIC(19,4))    labor_costs_transferred_report_cny,
                      CAST(lh.flag_hours_non_transferred * lha_xp.bill_amount_report_cny AS NUMERIC(19,4))  labor_costs_non_transferred_report_cny

                      FROM
                      df_pr lh
                      LEFT JOIN labor_history_amount_transposed lha_xp  ON lh.labor_history_id = lha_xp.labor_history_id

                  - name: df_xfer_pr
                    sql: >
                      SELECT DISTINCT
                      lh.*,
                      xfer_pr.project_id                                xfer_from_project_id,
                      xfer_pr.project_number_1                              xfer_from_project_number_1,
                      xfer_pr.project_name                                xfer_from_project_name,
                      xfer_pr.project_name_long                             xfer_from_project_name_long,
                      xfer_pr.org_code                                  xfer_from_project_org_code,

                      xfer_pr.business_entity_code                            xfer_from_project_business_entity_code,
                      xfer_pr.business_entity_name                            xfer_from_project_business_entity_name,
                      xfer_pr.region_code                               xfer_from_project_region_code,
                      xfer_pr.region_name                               xfer_from_project_region_name,
                      xfer_pr.office_code                               xfer_from_project_office_code,
                      xfer_pr.office_name                               xfer_from_project_office_name,
                      xfer_pr.studio_name                               xfer_from_project_studio_name,
                      xfer_pr.practice_area_name                            xfer_from_project_practice_area_name,
                      xfer_pr.market_sector_name                            xfer_from_project_market_sector_name,

                      xfer_pr.project_type_name                             xfer_from_project_type_name,
                      xfer_pr.service_name                                xfer_from_project_service_name,
                      xfer_pr.service_sub_name                              xfer_from_project_service_sub_name,
                      xfer_pr.delivery_approach_name                          xfer_from_project_delivery_approach_name,
                      xfer_pr.government_funded_name                          xfer_from_project_government_funded_name,
                      xfer_pr.is_residential                              xfer_from_project_is_residential,
                      xfer_pr.status_name                               xfer_from_project_status_name,
                      xfer_pr.charge_type_name                              xfer_from_project_charge_type_name

                      FROM df_lha_xp lh
                      LEFT JOIN project xfer_pr ON lh.xfer_project_id = xfer_pr.project_id

                  - name: df_fx_pr_org_rollup_cur
                    sql: >
                      SELECT DISTINCT
                      lh.*,
                      CAST( lh.flag_costs_available_to_bill *lh.bill_amount_functional * fx_pr_org_rollup_cur.exchange_rate_avg AS NUMERIC(19,4))
                        labor_costs_available_to_bill_report_functional_rollup_standard,

                      CASE lh.charge_type_name
                        WHEN 'Billable'
                        THEN CAST(lh.cost_amount_functional * fx_pr_org_rollup_cur.exchange_rate_avg AS NUMERIC(19,4))
                        ELSE 0
                      END                                             direct_cost_amount_report_functional_rollup_standard,

                      CASE lh.charge_type_name
                        WHEN 'Billable'
                        THEN CAST(lh.bill_amount_functional * fx_pr_org_rollup_cur.exchange_rate_avg AS NUMERIC(19,4))
                        ELSE 0
                      END                                             direct_bill_amount_report_functional_rollup_standard,
                      CASE WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE CAST(lh.cost_amount_functional * fx_pr_org_rollup_cur.exchange_rate_avg AS NUMERIC(19,4))
                      END                                             indirect_cost_amount_report_functional_rollup_standard,
                      CASE WHEN lh.charge_type_name = 'Billable' THEN 0
                        WHEN lh.charge_type_name IS NULL THEN NULL
                        ELSE CAST(lh.bill_amount_functional * fx_pr_org_rollup_cur.exchange_rate_avg AS NUMERIC(19,4))
                      END                                             indirect_bill_amount_report_functional_rollup_standard,
                      CAST(lh.flag_hours_transferred
                        *lh.bill_amount_functional
                        * fx_pr_org_rollup_cur.exchange_rate_avg
                        AS NUMERIC(19,4))                                   labor_costs_transferred_report_functional_rollup_standard,

                      CAST(lh.flag_hours_non_transferred
                        *lh.bill_amount_functional
                        * fx_pr_org_rollup_cur.exchange_rate_avg
                        AS NUMERIC(19,4)) labor_costs_non_transferred_report_functional_rollup_standard,

                      lh.bill_amount_functional * fx_pr_org_rollup_cur.exchange_rate_avg          total_bill_amount_report_functional_rollup_standard

                      FROM df_xfer_pr lh
                      LEFT JOIN currency_exchange_consolidation fx_pr_org_rollup_cur
                      ON fx_pr_org_rollup_cur.currency_id_from = lh.currency_id_functional

                      AND fx_pr_org_rollup_cur.fiscal_period_id = lh.fiscal_period_id_post
                  - name: df_eh_current
                    sql: >
                      SELECT DISTINCT
                      lh.*,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.org_code ELSE eh_current.org_code END                       employee_org_code_current,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.region_code ELSE eh_current.region_code END                   employee_region_code_current,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.region_name ELSE eh_current.region_name END                   employee_region_name_current,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.office_code ELSE eh_current.office_code END                   employee_office_code_current,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.office_name ELSE eh_current.office_name END                   employee_office_name_current,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.studio_name ELSE eh_current.studio_name END                   employee_studio_name_current,

                      eh_current.status_name                    employee_status_name_current

                      FROM
                      df_fx_pr_org_rollup_cur lh
                      LEFT JOIN employee_history eh_current ON eh_current.employee_id = lh.employee_id
                      AND eh_current.is_current_record = 1

                  - name: labor_history_final
                    sql: >
                      SELECT DISTINCT
                      lh.*,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.org_code ELSE lh_org_emp.org_code END                                     employee_org_code,

                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.business_entity_code ELSE lh_org_emp.business_entity_code END                         employee_business_entity_code,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.business_entity_name ELSE lh_org_emp.business_entity_name END                         employee_business_entity_name,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.region_code ELSE lh_org_emp.region_code END                                 employee_region_code,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.region_name ELSE lh_org_emp.region_name END                                 employee_region_name,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.office_code ELSE lh_org_emp.office_code END                                 employee_office_code,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.office_name ELSE lh_org_emp.office_name
                      END   employee_office_name,

                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.org_code ELSE lh_org_emp.org_code END   employee_org_code_post,

                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.business_entity_code ELSE lh_org_emp.business_entity_code END                       employee_business_entity_code_post,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.business_entity_name ELSE lh_org_emp.business_entity_name END                       employee_business_entity_name_post,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.region_code ELSE lh_org_emp.region_code END                                 employee_region_code_post,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.region_name ELSE lh_org_emp.region_name END                                 employee_region_name_post,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.office_code ELSE lh_org_emp.office_code END                                 employee_office_code_post,
                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.office_name ELSE lh_org_emp.office_name END                                 employee_office_name_post,

                      CASE WHEN lh.employee_id = (SELECT DISTINCT employee_id FROM emp_base)
                      THEN lh.country_name ELSE lh_org_emp.country_id END                                 employee_country_id

                      FROM
                      df_eh_current lh
                      LEFT JOIN organization_new lh_org_emp
                      ON lh.office_id_employee = lh_org_emp.office_id

                sink:
                  - sequenceName: df_pr1
                    datasetName: labor_history
                    outputName: enriched
                    outputType: Iceberg
                    description: Labor History Enriched data from GCD ingested datasets
                    outputOptions:
                      saveMode: overwrite

                      iceberg:
                        properties:
                          write.format.default: parquet
                          write.metadata.compression-codec: gzip

                    tags:
                      - Report-Table
                    title: Labor History Enriched
          sparkConf:
            - spark.sql.autoBroadcastJoinThreshold: 300m
            - spark.sql.shuffle.partitions: 600
            - spark.default.parallelism: 400
    - name: dt-labor-history-l-n
      spec:
        stack: toolbox
        stackSpec:
          dataset: dataos://icebase:report/labor_history?acl=rw
          action:
            name: set_version
            value: latest
      dependencies:
        - connect-labor-history-load-new
```