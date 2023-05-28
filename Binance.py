# Api Binance
import pandas as pd
from binance.client import Client
from datetime import datetime
import time
import os
import sys

#Crear una colección de datos de 1 minuto de los últimos 3 meses de BTCUSDT
