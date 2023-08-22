from pyecharts import options as opts
from pyecharts.charts import Map

province_dis = {'宁夏':55,'河南': 145, '北京': 137, '河北': 121, '辽宁': 112, '江西': 16, '上海':120, '安徽': 110, '江苏': 116, '湖南': 119,'浙江': 113, '海南': 12, '广东': 212, '湖北': 18, '黑龙江': 111, '澳门': 11, '陕西': 111, '四川': 17, '内蒙古': 13, '重庆': 13,'广西':81,'云南': 16, '贵州': 21, '吉林': 31, '山西': 11, '山东': 111, '福建': 41, '青海': 51, '天津': 11,'新疆':150,'西藏':170,'甘肃':120,'台湾':31}

provice = list(province_dis.keys())
values = list(province_dis.values())

china = (
    Map()
    .add("", [list(z) for z in zip(provice, values)], "china")
    .set_global_opts(title_opts=opts.TitleOpts(title="中国地图"), visualmap_opts=opts.VisualMapOpts())
)

# 打开html
china.render("render.html")