WEBEX-9417: As a developer, I want to Qlik report for F7295
===========================================================

Recording
---------

#. How to use Qlik to create a telemetry report
	+ https://alpha.webex.com/alpha/lsr.php?RCID=994917d155e8481eb825de1694bd5f10
	+ vWTYVM9A

#. Data Process Framework training by Jeffrey on 3/8/2018 recording 
	+ https://go.webex.com/go/ldr.php?RCID=37181711525e79cf6f4864388404099b
	
#. Data Process Framework training by Jeffrey on 3/21/2018
	+ https://go.webex.com/go/ldr.php?RCID=26b9e76b2745b7795bef39d555db02b4

#. 20190109
	+ https://cisco.webex.com/cisco/lsr.php?RCID=608a616ec4bf48dea41da16a8baaa2aa
	+ Recording password: 9xSY2RG2

Table
-----

#. signservice_forgrad

#. signserviceaggr_forgrad

#. ATS Script
 
 ::
 
    create external table telemetry.tdssvr_signservice_ats_dap_json (
    path string,
    `@timestamp` string,
    component string,
    `@version` string,
    host string,
    eventtype string,
    message struct<requests:int, failed:int, success:int, timestamp:string>,
    type string
    )
    PARTITIONED BY (day string)
    ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
    WITH SERDEPROPERTIES ("ignore.malformed.json" = "true")
    stored as
    INPUTFORMAT'com.hadoop.mapred.DeprecatedLzoTextInputFormat'
    
    OUTPUTFORMAT'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
    
    location '/kafka/logstash_meeting_hdfs/tdssvr/others-others/';

#. BTS Script
 
::
 
    create external table telemetry.signservice_forgrad(
    path string,
    `@timestamp` string,
    component string,
    `@version` string,
    host string,
    eventtype string,
    message struct<requests:int, failed:int, success:int, timestamp:string>,
    type string
    )
    PARTITIONED BY (day string)
    ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
    WITH SERDEPROPERTIES ("ignore.malformed.json" = "true")
    stored as
    INPUTFORMAT'com.hadoop.mapred.DeprecatedLzoTextInputFormat'

    OUTPUTFORMAT'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'

    location '/kafka/logstash_meeting_hdfs/tdssvr-forgrad/others-others/';


Example
-------

#. CMP Job Exploration
	+ Eureka_SessUserJoin_Meeting_Hive
	+ https://oneportal.webex.com/oneportal/?entry-point=clops#/job/jobExcution

#. count(hour) and the date is 2019.1.12
	::
	 
	 select count(*) from mjs_join where year(`date`) = 2019 and month(`date`) = 1 and day(`date`)=12 group by hour(rcvtime);

#. query from 2018-06-01 to 2019-01-03 and join way is 5 
	::
	 
	 select `date` as date1, count(*) as cnt  from mjs_join where unix_timestamp(`date`,'yyyy-MM-dd') between unix_timestamp('2018-06-01','yyyy-MM-dd') and unix_timestamp('2019-01-23','yyyy-MM-dd') and joinway = 5 group by `date` order by date1;

#. List confcount, date and sitename, the date is from 2019-01-01 to 2019-01-20
	::
	 
	 select count(distinct confid) as confCount, `date`, sitename from mjs_join where unix_timestamp(`date`,'yyyy-MM-dd') between unix_timestamp('2019-01-01','yyyy-MM-dd') and unix_timestamp('2019-01-20','yyyy-MM-dd') group by `date` , sitename;
	 

CMP job
-------

#. In lab environment: 
	+ your job must Template on: agg_1telemetry_base_job

#. BTS:
	+ template on: agg_1telemetry_base_job_bts1

#. PROD
	+ template on: agg_1telemetry_base_job


Resource
--------

#. Repo
	+ https://sqbu-github.cisco.com/PDA/PDA-DATA-ANALYZE

#. Qlik
	+ ATS and BTS
		- https://qlkbts.webex.com
	+ PROD
		- https://qlikinternal.webex.com

#. Hue
	+ BTS
		- http://rpbt1rpd001.webex.com:8888/hue/editor/?type=hive

	+ PROD
		- http://rpsj1rpd101.webex.com:8888/hue/

#. CMP
	+ PROD
		- https://oneportal.webex.com

	+ QA
		- https://oneportal.webex.com

#. Hue demo online
	+ http://demo.gethue.com/hue/editor/?type=hive

#. Kibana
	+ BTS
		- logs.webex.com
		- type: tdssvr
		
#. AppToken Knowledge Sharing From Bo Ren
	+ https://go.webex.com/go-sc/lsr.php?RCID=39e43f2aa9e1453fbcdfe3e64dec6a80
	+ SfhUtrH3

Reference
---------

#. How to create a data connection for Qlik
	+ https://wiki.cisco.com/x/9-JjD

#. Hand Book
	+ https://wiki.cisco.com/x/N5xJDg
	
#. Qlik Metrics Aggregation App
	+ https://wiki.cisco.com/x/-U-lCw
	
#. How to use Qlik to create a telemetry report
	+ https://wiki.cisco.com/x/D4tBCw	
	
#. Line Chat
	+ https://help.qlik.com/en-US/search/?q=Line+Chat	
	
#. Qlik Help
	+ https://help.qlik.com/zh-CN/sense/November2018/Subsystems/Hub/Content/Sense_Hub/Dimensions/dimensions.htm
	
#. Hive Help
	+ https://support.treasuredata.com/hc/en-us/articles/360001457347-Hive-Query-Language
	+ https://cwiki.apache.org/confluence/display/Hive/LanguageManual
	
#. Hive Tutorial
	+ https://cwiki.apache.org/confluence/display/Hive/Tutorial
	
#. WME Example
	+ https://wiki.cisco.com/x/7ha2Bw

#. Qlik 集合表达式 ( {$<Year={2009}>} )
	+ https://help.qlik.com/zh-CN/qlikview/November2017/Subsystems/Client/Content/ChartFunctions/SetAnalysis/set-analysis-expressions.htm

#. 如何设定y轴的起始位置从自定义的开始？而不是默认的0开始
	+ https://github.com/apache/incubator-echarts/issues/6525

#. RAW Table存放的地方 HUE, 可以在这里通过sql语句查询，修改，以及drop数据库表
	+ lab：http://sap-namenode1:8888/hue/metastore/tables/telemetry/
	+ bts ：http://rpbt1rpd001.webex.com:8888/hue
	+ production：http://rpsj1rpd101.webex.com:8888/hue