程序用于测试DNSPod受攻击域名所用流量的费用。
-------------------------------------------
1、选择域名所属套餐
2、依次填写各个服务器受攻击流量数（直接填
写数字即可，比如攻击量为1024QPS，则直接
填写1024即可）
3、如果某个服务器没有流量，则不需要填写，
保留默认0即可
4、因为采取python flask web服务器，并为
单线程作业，故流量较大时计算可能稍慢。
------------------------------------------
From：Wicky Dong
