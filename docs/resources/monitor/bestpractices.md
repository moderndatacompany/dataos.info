When creating a Monitor, it is essential to follow best practices to ensure effective monitoring and incident management. Here are some recommendations:

- Always validate the Monitor condition before applying the Equation Monitor, by executing the below command.

    === "Command"

        ```bash
        dataos-ctl develop observability monitor equation -f ${{file path}}
        ```

    === "Example usage"

        ```bash
        dataos-ctl develop observability monitor equation -f /home/office/monitor/equation_monitor.yaml
        INFO[0000] 🔮 develop observability...                   
        INFO[0000] 🔮 develop observability...monitor tcp-stream...starting 
        INFO[0002] 🔮 develop observability...monitor tcp-stream...running 
        INFO[0002] 🔮 develop observability...monitor tcp-stream...stopping 
        INFO[0002] 🔮 context cancelled, monitor tcp-stream is closing. 
        INFO[0003] 🔮 develop observability...complete           

        RESULT (maxRows: 10, totalRows:1): 🟩 monitor condition met

          EXP VAL (LEFT) |      OP      | EXP VAL (RIGHT) |      {POD="COLAEXP-SS-0"}      | CONSTANT (RIGHT-COMP)  
                        |              |                 |          (LEFT-COMP)           |                        
        -----------------|--------------|-----------------|--------------------------------|------------------------
          95.48          | greater_than | 80.00           | 95.48                          | 1.00                   

        ```

    This allows you to verify that the Monitor's logic and thresholds are set up correctly, ensuring that the monitor will behave as expected when actually applied in the DataOS environment.

- When using `dataos-ctl develop observability` command to validate conditions before applying:

    - '🟩': Condition met successfully.

    - '🟨': Condition not met at the moment of execution, but the monitor logic is valid.

    - '🟥': Condition invalid, likely due to incorrect valueJqFilter, unsupported operator, or missing field in the payload.

    This validation step ensures that the monitor behaves as expected in DataOS and helps avoid false incidents or broken monitors.
