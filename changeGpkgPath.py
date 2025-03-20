from qgis.core import QgsPathResolver, QgsProject, QgsMessageLog, Qgis
import re

class changeGpkgPath:
    def __init__(self, iface):
        self.iface = iface
        pass

    def initGui(self):
        self.printed = False
        self.processor = QgsPathResolver.setPathPreprocessor(self.my_processor)

    def unload(self):
        QgsPathResolver.removePathPreprocessor(self.processor)
        
    def my_processor(self,path):
        # Replace GPKG datasource if project is stored in GPKG
        if re.search('[^/]+\.gpkg',path,flags=re.IGNORECASE):
          m = re.search('[^/]+\.gpkg',QgsProject.instance().fileName(),flags=re.IGNORECASE)
          if m and not re.search(m.group(0),path,flags=re.IGNORECASE):
              if not self.printed:
                self.iface.messageBar().pushMessage("changeGpkgPath Plugin", "Replaced GPKG Layer Source! - see Log Messages", level=Qgis.Info)
                QgsMessageLog.logMessage('Replaced GPKG Layer Source: %s' % path,'changeGpkgPath',Qgis.Info)
              path = re.sub('[^/]+\.gpkg',m.group(0),path,flags=re.IGNORECASE)
              if not self.printed:
                QgsMessageLog.logMessage('with: %s' % path,'changeGpkgPath',Qgis.Info)
              self.printed = True

        return path