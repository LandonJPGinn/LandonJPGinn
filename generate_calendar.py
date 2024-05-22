import datetime
import pandas as pd
import svgwrite

# Read dates from CSV file
dates_csv = 'dates.csv'
special_dates = pd.read_csv(dates_csv, header=None, names=['date'])
special_dates['date'] = pd.to_datetime(special_dates['date'])

# Get current date
today = datetime.datetime.now().date()

# SVG drawing setup
dwg = svgwrite.Drawing('calendar.svg', profile='full', size=(800, 600))

# Calendar setup
start_date = today.replace(day=1)
end_date = (start_date + pd.offsets.MonthEnd(1)).date()

# Isometric calendar grid
def draw_isometric_calendar(dwg, start_date, end_date, special_dates, today):
    x_start, y_start = 100, 50
    x_offset, y_offset = 50, 30

    current_date = start_date
    while current_date <= end_date:
        day = current_date.day
        x = x_start + ((day - 1) % 7) * x_offset
        y = y_start + ((day - 1) // 7) * y_offset

        # Draw the day
        dwg.add(dwg.text(str(day), insert=(x, y), fill='black'))

        # Highlight today in red
        if current_date == today:
            dwg.add(dwg.circle(center=(x, y - 5), r=10, fill='none', stroke='red', stroke_width=2))

        # Highlight special dates in blue
        if current_date in special_dates['date'].values:
            dwg.add(dwg.circle(center=(x, y - 5), r=10, fill='none', stroke='blue', stroke_width=2))

        current_date += datetime.timedelta(days=1)

# Draw the calendar
draw_isometric_calendar(dwg, start_date, end_date, special_dates, today)

# Save the SVG file
dwg.save()
