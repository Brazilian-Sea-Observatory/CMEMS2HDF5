export PATH=$PATH:$NETCDF/bin:$NETCDF/lib:$NETCDF/include

export NETCDF_ROOT=$NETCDF
export NETCDF4_ROOT=$NETCDF
export NETCDF_LIB=$NETCDF/lib
export NETCDF_INC=$NETCDF/include

export NETCDF_GF_ROOT=$NETCDF
export NETCDF4_GF_ROOT=$NETCDF
export NETCDF_GF_LIB=$NETCDF/lib
export NETCDF_GF_INC=$NETCDF/include

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$NETCDF_LIB

export CPPFLAGS="$CPPFLAGS -I$NETCDF_INC"
export LDFLAGS="$LDFLAGS -L$NETCDF_LIB"

###### zlib-1.2.13 #########
ZLIB=/home/guilherme.franz/apps_intel/zlib-1.2.13
export PATH=$PATH:$ZLIB/lib:$ZLIB/include
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ZLIB/lib

# Vai para o diretório de execução do script
cd /home/guilherme.franz/Aplica/work/CMEMS/GLOBAL_ANALYSIS_FORECAST_PHY


# Executa
python3 /home/guilherme.franz/Aplica/work/CMEMS/GLOBAL_ANALYSIS_FORECAST_PHY/CMEMS2HDF5.py >> /home/guilherme.franz/Aplica/work/CMEMS/GLOBAL_ANALYSIS_FORECAST_PHY/CMEMS2HDF5.log 2>&1
