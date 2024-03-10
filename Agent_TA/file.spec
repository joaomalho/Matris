# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Configurações do executável
exe = EXE(main_script='Main.py',  # Specify the main script here
          exclude_binaries=True,
          name='matriz',
          debug=False,
          console=True)

# Dependências e outros arquivos
additional_files = [
    ('C:\\Users\\joaom\\Matris\\TradingRobot\\Pyrobot\\Application\\Matriz\\Agent_TA\\Utils', '.'),
    ('C:\\Users\\joaom\\Matris\\TradingRobot\\Pyrobot\\Application\\Matriz\\Agent_TA\\Decision', '.'),
    ('C:\\Users\\joaom\\Matris\\TradingRobot\\Pyrobot\\Application\\Matriz\\Agent_TA\\connections', '.'),
    ('C:\\Users\\joaom\\Matris\\TradingRobot\\Pyrobot\\Application\\Matriz\\Agent_TA\\RiskManager', '.'),
    ('C:\\Users\\joaom\\Matris\\TradingRobot\\Pyrobot\\Application\\Matriz\\Agent_TA\\TrendMetrics', '.'),
    ('C:\\Users\\joaom\\Matris\\TradingRobot\\Pyrobot\\Application\\Matriz\\Agent_TA\\CandlesPatterns', '.'),
    ('C:\\Users\\joaom\\Matris\\TradingRobot\\Pyrobot\\Application\\Matriz\\Agent_TA\\TailingStoploss', '.'),
    ('C:\\Users\\joaom\\Matris\\TradingRobot\\Pyrobot\\Application\\Matriz\\Agent_TA\\MarketOrder', '.'),
    ('C:\\Users\\joaom\\Matris\\TradingRobot\\Pyrobot\\Application\\Matriz\\Agent_TA\\ParameterOptimizer', '.')
]

# Configurações de compilação
# coll = COLLECT(exe,
#               a.binaries,
#               a.zipfiles,
#               a.datas + collect_data_files('matplotlib') + collect_submodules('ta'),
#               strip=False,
#               upx=True,
#               name='matriz')

# Ajustes adicionais (opcional)
# Por exemplo, você pode definir o nível de recursão aqui
import sys
sys.setrecursionlimit(5000)


# NOTE:
## Executavel criado, mas como tem a interação pelo cmd fecha diretamente, após GUI criado será superado