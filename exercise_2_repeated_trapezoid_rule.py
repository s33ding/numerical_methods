# Import pandas library
import pandas as pd
from shared_func.repeated_trapezoid_rule_func import calculate_cross_section_area

challenge = """The determination of the area of cross-sections of rivers and lakes is important in flood prevention projects (for the calculation of water flow) and in reservoir projects (for the calculation of the total water volume). Unless devices, such as sonar, are used to obtain the profile of the bottom of rivers/lakes, the engineer must work with depth values, obtained at discrete points on the surface. A typical example of a river's cross-section is shown by the following values."""

print("CHALLENGE:", challenge)
print("====================================================")

# Create a DataFrame
x = "Distance_from_left_bank"
lst_x = list(range(0, 21, 2))
y = "Depth"
lst_y = [0, 1.8, 2, 4, 4, 6, 4, 3.6, 3.4, 2.8, 0]

data = {
    x: lst_x,
    y: lst_y
}

df = pd.DataFrame(data)

trapezoid_areas = calculate_cross_section_area(df)
total_area = abs(sum(trapezoid_areas))
print("total_area:", total_area )
