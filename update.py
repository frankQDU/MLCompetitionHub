import traceback
from datetime import datetime

from jinja2 import Environment, PackageLoader

from source import dcjingsai, kaggle, tianchi, turingtopia, biendata

# 获取数据
datas = []

try:
    datas.append(kaggle.get_data())
except Exception:
    traceback.print_exc()

try:
    datas.append(tianchi.get_data())
except Exception:
    traceback.print_exc()

try:
    datas.append(turingtopia.get_data())
except Exception:
    traceback.print_exc()

try:
    datas.append(dcjingsai.get_data())
except Exception:
    traceback.print_exc()

try:
    datas.append(biendata.get_data())
except Exception:
    traceback.print_exc()

env = Environment(loader=PackageLoader('source'))
update = datetime.utcnow().isoformat()
# 生成 README.md
template = env.get_template('main.j2')
content = template.render(datas=datas, update=update)

with open('README.md', 'w') as f:
    f.write(content)

# 生成 RSS
template = env.get_template('rss.j2')
content = template.render(datas=datas, update=update)

with open('rss.atom', 'w') as f:
    f.write(content)
