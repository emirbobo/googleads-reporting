class dimensions:

    # 广告客户的ID。示例：ca - pub - 088712。
    AD_CLIENT_ID = 'AD_CLIENT_ID '

    # 广告格式的代码。示例：text、image、html。
    AD_FORMAT_CODE = 'AD_FORMAT_CODE'

    # 广告格式的名称。示例：Text、Image或Rich Media。最后一个值表示html格式。
    AD_FORMAT_NAME = 'AD_FORMAT_NAME'

    # 广告单元的代码。该值不必在多个广告客户之间保持唯一。示例：837572。
    AD_UNIT_CODE = 'AD_UNIT_CODE'

    # 广告单元的唯一ID。示例：ca - pub - 088712: 837572。
    AD_UNIT_ID = 'AD_UNIT_ID'

    # 广告单元的名称。
    AD_UNIT_NAME = 'AD_UNIT_NAME'

    # 广告单元的尺寸代码。示例：720x42或mobile_single。
    AD_UNIT_SIZE_CODE = 'AD_UNIT_SIZE_CODE'

    # 广告单元的尺寸名称。示例：720x42或Single(Mobile)。
    AD_UNIT_SIZE_NAME = 'AD_UNIT_SIZE_NAME'

    # 出价类型。示例：cpc、cpm。
    BID_TYPE_CODE = 'BID_TYPE_CODE'

    # 出价类型名称。示例：CPC bids、CPM bids。
    BID_TYPE_NAME = 'BID_TYPE_NAME'

    # 向您网站发送广告的广告联盟的ID。
    BUYER_NETWORK_ID = 'BUYER_NETWORK_ID'

    # 向您网站发送广告的广告联盟的名称。示例：Google Adwords。
    BUYER_NETWORK_NAME = 'BUYER_NETWORK_NAME'

    # CLDR地区代码。示例：US、FR。
    COUNTRY_CODE = 'COUNTRY_CODE'
    # 地区名称。示例：United States、France。
    COUNTRY_NAME = 'COUNTRY_NAME'

    # 自定义渠道的代码。
    CUSTOM_CHANNEL_CODE = 'CUSTOM_CHANNEL_CODE'

    # 自定义渠道的ID。
    CUSTOM_CHANNEL_ID = 'CUSTOM_CHANNEL_ID'

    # 自定义渠道的名称。
    CUSTOM_CHANNEL_NAME = 'CUSTOM_CHANNEL_NAME'

    # 日期，采用YYYYMMDD格式。
    DATE = 'DATE'

    # 域名。
    DOMAIN_NAME = 'DOMAIN_NAME'

    # 月份，采用YYYYMM格式。
    MONTH = 'MONTH'

    # 广告平台类型的代码。示例：HighEndMobile、Desktop。
    PLATFORM_TYPE_CODE = 'PLATFORM_TYPE_CODE'

    # 广告平台类型的名称。示例：High - end mobile devices、Desktop。
    PLATFORM_TYPE_NAME = 'PLATFORM_TYPE_NAME'

    # 产品代码。示例：AFC、AFS。
    PRODUCT_CODE = 'PRODUCT_CODE'

    # 产品代码。示例：AdSense for Content、AdSense for Search。
    PRODUCT_NAME = 'PRODUCT_NAME'

    # 定位类型代码。示例：Keyword、WebSite、Publisher。
    TARGETING_TYPE_CODE = 'TARGETING_TYPE_CODE'

    # 定位类型名称。示例：Contextual、Reservation、Publisher。
    TARGETING_TYPE_NAME = 'TARGETING_TYPE_NAME'

    # 网址渠道的ID。
    URL_CHANNEL_ID = 'URL_CHANNEL_ID'

    # 网址渠道的名称。
    URL_CHANNEL_NAME = 'URL_CHANNEL_NAME'

    # 一周第一天的日期，采用YYYYMMDD格式。
    WEEK = 'WEEK'

# #######################admob dimensions 注释掉的为重复###########################

    # 发布商ID,广告客户的ID。示例：ca - app - pub - 1234567890123456。
    # AD_CLIENT_ID = 'AD_CLIENT_ID'

    # 广告单元ID,广告单元的代码。该值不必在多个广告客户之间保持唯一。示例：1234567890。
    # AD_UNIT_CODE = 'AD_UNIT_CODE'

    # 广告单元名称,广告单元的名称。示例：“您的横幅广告名称”。
    # AD_UNIT_NAME = 'AD_UNIT_NAME'

    # 格式（代码）广告单元的格式。        示例：banner、native。
    # AD_UNIT_SIZE_CODE = 'AD_UNIT_SIZE_CODE'

    # 格式（名称）广告单元的格式名称。        示例：Banner、Native advanced。
    # AD_UNIT_SIZE_NAME = 'AD_UNIT_SIZE_NAME'

    # 应用.应用名称。此字段的字符数不得超过80个，而且即使应用商店中的应用名称发生变化，此字段也不会随之更新。 示例：Line Up、Flood - It!。
    APP_NAME = 'APP_NAME'

    # Google Play ID / iOS 软件包 ID 应用的 Google Play ID（带有 2: 前缀）或iOS 软件包ID
    # （带有1: 前缀）。示例：2: com.labpixies.lineup、1: 476954712。
    APP_ID = 'APP_ID'

    # 平台应用平台。示例：Android、iOS。
    APP_PLATFORM = 'APP_PLATFORM'

    # 出价类型（代码）        出价类型。        示例：cpc、cpm。
    # BID_TYPE_CODE = 'BID_TYPE_CODE'

    # 出价类型（名称）出价类型名称。 示例：CPC bids、CPM bids。
    # BID_TYPE_NAME = 'BID_TYPE_NAME'

    # 国家 / 地区（代码）CLDR地区代码。        示例：US、FR。
    # COUNTRY_CODE = 'COUNTRY_CODE'

    # 国家 / 地区（名称）地区名称。示例：United States、France。
    # COUNTRY_NAME = 'COUNTRY_NAME'

    # 月 月份，采用YYYYMM格式。
    # MONTH = 'MONTH'

    # 日期 日期，采用YYYYMMDD格式。
    # DATE = 'DATE'

    # 设备（代码）平台类型的代码。示例：HighEndMobile、Tablet。
    # PLATFORM_TYPE_CODE = 'PLATFORM_TYPE_CODE'

    # 设备（名称）平台类型的名称。示例：High - end mobile devices、Tablets。
    # PLATFORM_TYPE_NAME = 'PLATFORM_TYPE_NAME'

    # 产品:产品名称。 示例：AdMob(Mobile Applications)、AdSense for Search。
    # PRODUCT_NAME = 'PRODUCT_NAME'

    # 周:一周第一天的日期，采用YYYYMMDD格式。
    # WEEK = 'WEEK'


class metrics:

    # 请求了广告（针对内容广告）或搜索查询（针对搜索广告）的广告单元的数量。
    # 一个广告请求可带来零次、一次或更多次广告展示，具体取决于广告单元的尺寸以及广告的可用情况。
    AD_REQUESTS = 'AD_REQUESTS'

    # 所请求的广告单元或查询与返回到网站的广告单元或查询的数量的比值。
    AD_REQUESTS_COVERAGE = 'AD_REQUESTS_COVERAGE'

    # 产生点击的广告请求所占的比率。
    AD_REQUESTS_CTR = 'AD_REQUESTS_CTR'

    # 每一千个广告请求的收入。计算方法：用估算收入除以广告请求数，再乘以1000。
    AD_REQUESTS_RPM = 'AD_REQUESTS_RPM'

    # 用户点击标准内容广告的次数。
    CLICKS = 'CLICKS'

    # 用户每次点击您的广告时您所获得的金额。每次点击费用的计算方法：用估算收入除以所获得的点击次数。
    COST_PER_CLICK = 'COST_PER_CLICK'

    # 发布商的估算收入。请注意，到昨天为止的所有收入都是准确的，
    # 而更近的收入是估算收入，因为可能受网络垃圾或汇率波动的影响。
    EARNINGS = 'EARNINGS'

    # 单个广告在您网站上展示的次数。广告格式不同，展示的广告数量也有所不同。
    # 例如，
    # 一个竖幅中可能包含2个或更多广告。此外，广告单元中的广告数量都不是固定的，
    # 具体取决于广告单元展示的是标准文字广告、独占型文字广告还是图片广告。
    INDIVIDUAL_AD_IMPRESSIONS = 'INDIVIDUAL_AD_IMPRESSIONS'

    # 单个广告的展示次数中带来点击的展示次数所占的比率。
    INDIVIDUAL_AD_IMPRESSIONS_CTR = 'INDIVIDUAL_AD_IMPRESSIONS_CTR'

    # 广告的每千次展示收入。计算方法：用估算收入除以单个广告展示次数，再乘以1000。
    INDIVIDUAL_AD_IMPRESSIONS_RPM = 'INDIVIDUAL_AD_IMPRESSIONS_RPM'

    # 展示了广告的广告单元数（针对内容广告）或触发广告进行展示的搜索查询数（针对搜索广告）。
    # 每个为网站至少获取一个广告的广告请求都计为一次匹配广告请求。
    MATCHED_AD_REQUESTS = 'MATCHED_AD_REQUESTS'

    # 产生点击的匹配查询所占的比率。
    MATCHED_AD_REQUESTS_CTR = 'MATCHED_AD_REQUESTS_CTR'

    # 每一千次匹配查询的收入。计算方法：用您的估算收入除以匹配的查询数，再乘以1000。
    MATCHED_AD_REQUESTS_RPM = 'MATCHED_AD_REQUESTS_RPM'

    # 网页浏览量。
    PAGE_VIEWS = 'PAGE_VIEWS'

    # 单个网页的浏览量中带来点击的浏览量所占的比率。
    PAGE_VIEWS_CTR = 'PAGE_VIEWS_CTR'

    # 每千次网页浏览量的收入。计算方法：用您的估算收入除以网页浏览量，再乘以1000。
    PAGE_VIEWS_RPM = 'PAGE_VIEWS_RPM'

# ##################admob metrics######################
    # AdMob 广告联盟估算收入
    # EARNINGS = 'EARNINGS'

    # AdMob 广告联盟请求次数
    REACHED_AD_REQUESTS = 'REACHED_AD_REQUESTS'

    # 匹配请求数
    MATCHED_REACHED_AD_REQUESTS = 'MATCHED_REACHED_AD_REQUESTS'

    # 展示次数
    VIEWED_IMPRESSIONS= 'VIEWED_IMPRESSIONS'

    # 点击次数
    # CLICKS = 'CLICKS'

    # 匹配率
    # 在所有广告请求中，获得广告填充的广告请求所占的百分比。此数值是用匹配请求数除以AdMob广告联盟请求数计算得出的。
    # 例如，如果一个应用的匹配请求数是40次，AdMob广告联盟请求总数是50次，则该应用的匹配率就是80 %。
    REACHED_AD_REQUESTS_MATCH_RATE = 'REACHED_AD_REQUESTS_MATCH_RATE'

    # 展示率
    # 在所有返回的广告中，实际在应用中展示给用户的广告所占的百分比。 该数值是用展示次数除以匹配请求数计算得出的。
    # 示例：如果匹配请求总数是 80 次，但您的应用只展示了其中的 60 次，则该应用的展示率就是 75%。
    REACHED_AD_REQUESTS_SHOW_RATE = 'REACHED_AD_REQUESTS_SHOW_RATE'
