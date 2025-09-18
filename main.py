annual_increase = 0.5  # 每年地球体重增加量(kg)
moon_percentage = 0.165  # 月球体重是地球的百分比
years = 10  # 计算未来10年

# 打印表头
print(f"{'年份':<6} {'地球体重变化(kg)':<18} {'月球体重变化(kg)':<18}")
print("-" * 50)

# 计算并打印每年的体重变化
for year in range(years + 1):
    earth_change = annual_increase * year
    moon_change = earth_change * moon_percentage
    print(f"{year:<6} {earth_change:<18.2f} {moon_change:<18.2f}")
