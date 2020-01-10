# 暂不使用
class dimensions:

    # 发布商ID,广告客户的ID。示例：ca - app - pub - 1234567890123456。
    AD_CLIENT_ID = 'AD_CLIENT_ID'

    # 广告单元ID,广告单元的代码。该值不必在多个广告客户之间保持唯一。示例：1234567890。
    AD_UNIT_CODE = 'AD_UNIT_CODE'

    # 广告单元名称,广告单元的名称。示例：“您的横幅广告名称”。
    AD_UNIT_NAME = 'AD_UNIT_NAME'

    # 格式（代码）广告单元的格式。        示例：banner、native。
    AD_UNIT_SIZE_CODE = 'AD_UNIT_SIZE_CODE'

    # 格式（名称）广告单元的格式名称。        示例：Banner、Native advanced。
    AD_UNIT_SIZE_NAME = 'AD_UNIT_SIZE_NAME'

    # 应用.应用名称。此字段的字符数不得超过80个，而且即使应用商店中的应用名称发生变化，此字段也不会随之更新。 示例：Line Up、Flood - It!。
    APP_NAME = 'APP_NAME'

    # Google Play ID / iOS 软件包 ID 应用的 Google Play ID（带有 2: 前缀）或iOS 软件包ID
    # （带有1: 前缀）。示例：2: com.labpixies.lineup、1: 476954712。
    APP_ID = 'APP_ID'

    # 平台应用平台。示例：Android、iOS。
    APP_PLATFORM = 'APP_PLATFORM'

    # 出价类型（代码）        出价类型。        示例：cpc、cpm。
    BID_TYPE_CODE = 'BID_TYPE_CODE'

    # 出价类型（名称）出价类型名称。 示例：CPC bids、CPM bids。
    BID_TYPE_NAME = 'BID_TYPE_NAME'

    # 国家 / 地区（代码）CLDR地区代码。        示例：US、FR。
    COUNTRY_CODE = 'COUNTRY_CODE'

    # 国家 / 地区（名称）地区名称。示例：United States、France。
    COUNTRY_NAME = 'COUNTRY_NAME'

    # 月 月份，采用YYYYMM格式。
    MONTH = 'MONTH'

    # 日期 日期，采用YYYYMMDD格式。
    DATE = 'DATE'

    # 设备（代码）平台类型的代码。示例：HighEndMobile、Tablet。
    PLATFORM_TYPE_CODE = 'PLATFORM_TYPE_CODE'

    # 设备（名称）平台类型的名称。示例：High - end mobile devices、Tablets。
    PLATFORM_TYPE_NAME = 'PLATFORM_TYPE_NAME'

    # 产品:产品名称。 示例：AdMob(Mobile Applications)、AdSense for Search。
    PRODUCT_NAME = 'PRODUCT_NAME'

    # 周:一周第一天的日期，采用YYYYMMDD格式。
    WEEK = 'WEEK'


class metrics:

    # AdMob 广告联盟估算收入
    EARNINGS = 'EARNINGS'

    # AdMob 广告联盟请求次数
    REACHED_AD_REQUESTS = 'REACHED_AD_REQUESTS'

    # 匹配请求数
    MATCHED_REACHED_AD_REQUESTS = 'MATCHED_REACHED_AD_REQUESTS'

    # 展示次数
    VIEWED_IMPRESSIONS= 'VIEWED_IMPRESSIONS'

    # 点击次数
    CLICKS = 'CLICKS'

    # 匹配率
    # 在所有广告请求中，获得广告填充的广告请求所占的百分比。此数值是用匹配请求数除以AdMob广告联盟请求数计算得出的。
    # 例如，如果一个应用的匹配请求数是40次，AdMob广告联盟请求总数是50次，则该应用的匹配率就是80 %。
    REACHED_AD_REQUESTS_MATCH_RATE = 'REACHED_AD_REQUESTS_MATCH_RATE'

    # 展示率
    # 在所有返回的广告中，实际在应用中展示给用户的广告所占的百分比。 该数值是用展示次数除以匹配请求数计算得出的。
    # 示例：如果匹配请求总数是 80 次，但您的应用只展示了其中的 60 次，则该应用的展示率就是 75%。
    REACHED_AD_REQUESTS_SHOW_RATE = 'REACHED_AD_REQUESTS_SHOW_RATE'
