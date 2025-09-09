input_str = input()
num = float(input_str[:-2])
unit = input_str[-2:]
kg_to_pd = 2.2046
if unit == "kg":
   result = num * kg_to_pd
   print(f"对应的英制重量为{result:.3f}磅")
elif unit == "pd":
   result = num / kg_to_pd
   print(f"对应的公制重量为{result:.3f}公斤")
