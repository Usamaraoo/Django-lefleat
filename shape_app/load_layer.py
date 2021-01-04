from pathlib import Path
import os
from django.contrib.gis.utils import LayerMapping
from .models import Pakistan

pakistan_mapping = {

    'name': 'NAME_3',
    'geom': 'MULTIPOLYGON',
}
pak_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), "data/PAK_adm3.shp"))


def run(verbose=True):
    lm = LayerMapping(Pakistan, str(pak_shp), pakistan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
