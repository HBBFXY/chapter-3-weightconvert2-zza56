# 地球体重初始值（单位：公斤）
earth_weight = float(input("请输入您当前的体重（kg）：")) #字符串转换为浮点数
# 月球体重占地球体重的16.5%
moon_ratio = 0.165
print("\n年份\t地球体重(kg)\t月球体重(kg)")
print("-" * 30)
for year in range(1, 11):
    # 每年增长0.5公斤
    current_earth_weight = earth_weight + 0.5 * year
    current_moon_weight = current_earth_weight * moon_ratio
    # 输出格式控制
    print("{:<4}\t{:>12.2f}\t{:>12.2f}".format(year, current_earth_weight, current_moon_weight))
