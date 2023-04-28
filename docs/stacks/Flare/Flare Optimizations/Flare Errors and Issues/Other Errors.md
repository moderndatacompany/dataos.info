# **Other Errors**

## **Error: Caused by Read time out / connection time out**

**Message**

Read time out

```bash
				at org.apache.spark.deploy.SparkSubmit.main(SparkSubmit.s
Caused by: java.net.SocketTimeoutException: Read timed out
				at java.net.SocketInputStream.socketRead0(Native Method)
				at java.net.SocketInputStream.socketRead(SocketInputStream....
				at java.net.SocketInputStream.read(SocketInputStream.java.....
				at java.net.SocketInputStream.read(SocketInputStream.java.....
				at sun.security.ssl.SSLSocketInputRecord.read(SSL.SocketInput..
```

Connection time out

```bash
				at org.apache.spark.deploy.SparkSUbmit.main(SparkSubmit.scala)
Caused by: java.net.SocketTimeoutException: connect timed out
				at java.net.PlainSocketImpl.socketConnect(Native Method)
				at java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java
				at java.net.PlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java
				at java.net.PlainSocketImpl.connect(AbstractPlainSocketImpl.java
				at java.net.SocksSocketImpl.connect(AbstractPlainSocketImpl.java:392)
```

**What went wrong?**

Metis Client Error