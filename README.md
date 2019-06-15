## Target Score 

Reads a message from the global_events topic and if the message is a "target_hit" event then it increases the score of the hits associate with that target.

Assumes the message to be in a JSON format as below:

```
{  
   "event_name":"target_hit",
   "target_id":"target_1",
   "time":"14:53:12"
}
```