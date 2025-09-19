import requests
import openpyxl

url = 'https://coastwatch.pfeg.noaa.gov/erddap/griddap/NCEP_Global_Best.csv?ugrd10m%5B(2025-09-16):1:(2025-09-25T12:00:00Z)%5D%5B(5):1:(15)%5D%5B(100):1:(116)%5D,vgrd10m%5B(2025-09-16):1:(2025-09-25T12:00:00Z)%5D%5B(5):1:(15)%5D%5B(100):1:(116)%5D,prmslmsl%5B(2025-09-16):1:(2025-09-25T12:00:00Z)%5D%5B(5):1:(15)%5D%5B(100):1:(116)%5D'  # Link dữ liệu
outputFile = 'wind_data_2025.csv'  # Tên file lưu dữ liệu

# Download the file
response = requests.get(url)
response.raise_for_status()  # Raise an error if the request failed

# Save the file locally
with open(outputFile, 'wb') as file:
    file.write(response.content)


print(f"File saved as {outputFile}")
