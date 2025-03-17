from qgis.core import QgsPathResolver,QgsProject
import re

def processor(path):
    # Replace GPKG datasource if project is stored in GPKG
    if re.search('[^/]+\.gpkg',path,flags=re.IGNORECASE):
      m = re.search('[^/]+\.gpkg',QgsProject.instance().fileName(),flags=re.IGNORECASE)
      if m and not re.search(m.group(0),path,flags=re.IGNORECASE):
          print('Repl. Old: %s' % path)
          path = re.sub('[^/]+\.gpkg',m.group(0),path,flags=re.IGNORECASE)
          print('With  New: %s' % path)
    return path

class changeGpkgPath:
    def __init__(self, iface):
        pass

    def initGui(self):
        self.processor = QgsPathResolver.setPathPreprocessor(processor)

    def unload(self):
        QgsPathResolver.removePathPreprocessor(self.processor)