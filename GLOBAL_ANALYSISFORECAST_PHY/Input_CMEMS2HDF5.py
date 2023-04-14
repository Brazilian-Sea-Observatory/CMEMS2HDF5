import datetime, os

dirpath = os.getcwd()
download_dir = (dirpath+"/CMEMS_Download")
ConvertToHdf5_dir = (dirpath+"/ConvertToHdf5")
backup_path =  (dirpath+"/Backup")

#1-day forecast (6-hourly instanataneous)
#product_id = ["cmems_mod_glo_phy_anfc_0.083deg_PT1H-m","cmems_mod_glo_phy-cur_anfc_0.083deg_PT6H-i","cmems_mod_glo_phy-so_anfc_0.083deg_PT6H-i","cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i"]

#10-days forecast (daily mean)
product_id = ["cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m","cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m","cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m","cmems_mod_glo_phy_anfc_0.083deg_P1D-m"]

input_convert_file_name = ["ConvertToHDF5Action_zos.dat","ConvertToHDF5Action_cur.dat","ConvertToHDF5Action_so.dat","ConvertToHDF5Action_thetao.dat"]

#To avoid problems with cron in Linux define the entire path to python exe"
python_path = "python"

forecast_mode = 1
refday_to_start = 0 
number_of_runs = 4

#Data de início e fim se forecast_mode = 0
start = datetime.date(2023,1,29)
end = datetime.date(2023,1,30)

#fill in your details for CMEMS login
user = "YOUR USER"
password = "YOUR PASSWORD"
lon_min = "-50.69"
lon_max = "-38.36"
lat_min = "-30.81"
lat_max = "-20.55"
#lon_min = "-60."
#lon_max = "-20."
#lat_min = "-40"
#lat_max = "10"
start_depth = "0.494"
end_depth = "5727.9171"
output_file_name = "CMEMS"

clean_null_values = 1
#Tempo de espera para uma nova tentativa de download do arquivo (em segundos)
wait_time = 300
#Tempo de espera total em s para o download do arquivo (em segundos) 
wait_total_time = 1800
#Tamanho mínimo do arquivo em Bytes
min_file_size = 10000

telegram_messages = 0
TOKEN = "YOUR TELEGRAM BOT TOKEN"
chat_id = "YOUR CHAT ID"