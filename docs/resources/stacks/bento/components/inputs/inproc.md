# inproc

```yaml
# Config fields, showing default values
input:
  label: ""
  inproc: ""
```

Directly connect to an output within a Bento process by referencing it by a chosen ID. This allows you to hook up isolated streams whilst running Bento in streams mode, it is NOT recommended that you connect the inputs of a stream with an output of the same stream, as feedback loops can lead to deadlocks in your message flow.

It is possible to connect multiple inputs to the same inproc ID, resulting in messages dispatching in a round-robin fashion to connected inputs. However, only one output can assume an inproc ID, and will replace existing outputs if a collision occurs.