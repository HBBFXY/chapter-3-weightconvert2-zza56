initial_weight = 60  # 初始地球体重(kg)
annual_increase = 0.5  # 每年地球体重增加量(kg)
moon_percentage = 0.165  # 月球体重是地球的百分比
years = 10  # 计算未来10年

# 打印表头
print(f"{'年份':<6} {'地球体重(kg)':<15} {'月球体重(kg)':<15}")
print("-" * 40)

# 计算并打印每年的体重
for year in range(years + 1):
    earth_weight = initial_weight + annual_increase * year
    moon_weight = earth_weight * moon_percentage
    print(f"{year:<6} {earth_weight:<15.2f} {moon_weight:<15.2f}")
