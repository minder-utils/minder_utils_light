import os
from pathlib import Path
from minder_utils.util.util import reformat_path
import yaml

p = Path(os.path.join(os.path.dirname(__file__), 'confidential'))
if not p.exists():
    os.mkdir(reformat_path(p))

data_path = os.path.join(os.path.dirname(__file__), 'confidential', 'data_path.txt')
token_path = os.path.join(os.path.dirname(__file__), 'confidential', 'token_real.json')
dates_path = os.path.join(os.path.dirname(__file__), 'confidential', 'dates.json')
delta_path = os.path.join(os.path.dirname(__file__), 'confidential', 'delta.txt')
tihm_data_path = os.path.join(os.path.dirname(__file__), 'confidential', 'tihm_data_path.txt')

