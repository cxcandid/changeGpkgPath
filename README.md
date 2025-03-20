# ![image](https://github.com/cxcandid/changeGpkgPath/blob/main/gpkg_repair.jpg) 

# Change GPKG Path

This plugin automatically repairs GPKG data source paths within a QGIS GPKG project file if they have been lost due to file renaming.
It consists of only a few lines of Python code and uses the QgsPathResolver for data repair. 

"Change GPKG Path" has been an indispensable companion for me for a long time. Above all, it shows that even a few lines of code can achieve a lot.
It was originally inspired by this QGIS issue: https://github.com/qgis/QGIS/issues/37440

I assume that it will be replaced by an internal function at some point.


**Author:** Christoph Candido, Vienna

**email:** *christoph.candido@gmx.at*

**Change GPKG Path license:**

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
