##首先需要在google cloud project 建立了项目，并且加入adsense api权限
##此项目只需配置参数即可运行获取报告
###启动依赖
    1、首先运行install_run.py对依赖包进行安装
    2、如果是线上把base_prd.yaml文件内容覆盖到base_dev.yaml
    3、ggads_run.py启动需要client_id和client_secret，调起浏览器进行oauth2认证，然后生成ggads_conf.yaml
    4、adsense_run.py启动需要client_secrets.json文件生成dat文件

##yaml文件说明
    # google project client id
    client_id: xxxxxxxxxxxxxx
    # google project client_secret
    client_secret: xxxxxxxxxxx
    
    # admanager developer_token
    developer_token: xxxxxxxxxx
    # admanager id
    login_customer_id: xxxxxxxxxx
    以上为测试环境配置，正式使用base_prd.yaml
##googleads_service用来读取广告发布信息和支出
    google ads 和google adwords api合并为ads
    使用xxxxxxxx@gmail.com创建的谷歌云项目的ak和sk
    ggads_conf.yaml配置了访问权限信息，login_customer_id配置广告经理ID，程序里填写管理的客户账户ID
##adsense_service 用来读取广告收益报告
    google adsense 和 google admob api合并为adsense
    使用jingbo.xi@gmail.com创建的谷歌云项目的ak和sk
##使用步骤
    测试环境创建测试广告经理
    https://adwords.google.com/um/Welcome/Home?a=1&sf=mt&authuser=0#ta
    正式环境创建广告经理
    https://ads.google.com/home/tools/manager-accounts/
    正式令牌申请表（首先要在API CENTER获得测试令牌 settings -> api center ）
    https://services.google.com/fb/forms/newtoken/
#启动：
    - env为dev或prd 
    
    1、在没有环境的情况下先安装依赖包
       python install_run.py

    2、# python report_collector.py env=dev segment=YESTERDAY

Resource fields : 查询条件 where
Segments : 分组 group by
Metrics : 查询的字段

###自定义日期范围

    您可以使用 ISO 8601(YYYY-MM-DD) 格式指定日期：
    
    segments.date BETWEEN '2019-01-01' AND '2019-01-31'
    
    segments.date >= '2019-01-01' AND segments.date <= '2019-01-31'

###日期范围	所生成报告的日期范围
#####https://developers.google.com/google-ads/api/docs/query/date-ranges
    自定义日期范围
    您可以使用 ISO 8601(YYYY-MM-DD) 格式指定日期：
    
    segments.date BETWEEN '2019-01-01' AND '2019-01-31'
    
    segments.date >= '2019-01-01' AND segments.date <= '2019-01-31'
    
    - TODAY	仅限今天。
    - YESTERDAY	仅限昨天。
    - LAST_7_DAYS	过去 7 天（不包含今天）。
    - LAST_BUSINESS_WEEK	上个工作周周一至周五为期五天的时间段。
    - THIS_MONTH	当月所有日期。 
    - LAST_MONTH	上个月所有日期。
    - LAST_14_DAYS	过去 14 天（不包含今天）。
    - LAST_30_DAYS	过去 30 天（不包含今天）。
    - THIS_WEEK_SUN_TODAY	上周日到当天的时间段。
    - THIS_WEEK_MON_TODAY	上周一到当天的时间段。
    - LAST_WEEK_SUN_SAT	从上周日开始为期 7 天的时间段。
    - LAST_WEEK_MON_SUN	从上周一开始为期 7 天的时间段。



###查询结构
    您可以将针对资源、细分和指标字段的查询发送到 GoogleAdsService.Search。要使用 Google Ads 查询语言构建查询，
    您需要使用语言语法。一个查询由许多子句组成，包括：
    
    SELECT
    FROM
    WHERE
    ORDER BY
    LIMIT
    PARAMETERS
    这些子句会使用字段名称、资源名称、运算符、条件和排序，帮您选出正确的数据。在将它们合并为一个查询后，就可以使用 Google Ads API 发出请求。让我们看看如何使用每个子句。
    
    要点：GoogleAdsFieldService 为 Google Ads 查询语言客户端提供了一个目录，其中包含有关所有资源字段、细分字段和指标的元数据，还包含它们之间的关系以及在每个子句中的可用性，如下所述。如需了解更多详情，请参阅 GoogleAdsField 的文档。
    子句
    SELECT
    SELECT 子句指定要在请求中获取的一组字段。SELECT 会获取以英文逗号分隔的资源字段、细分字段和指标列表，然后在响应中返回值。SELECT 子句在查询中是必需子句。
    
    要获取广告系列的 ID 和名称，您可以使用以下查询：
    
    SELECT
      campaign.id,
      campaign.name
    FROM campaign
    在单个请求中，可以请求不同的字段类型，例如：
    
    资源字段
    
    campaign.id
    campaign.name
    ad_group.name
    细分字段
    
    segments.device
    指标
    
    metrics.impressions
    metrics.clicks